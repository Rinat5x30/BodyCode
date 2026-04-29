// Animated Quiz Logic
class AnimatedQuiz {
  constructor() {
    this.currentQuestion = 1;
    this.totalQuestions = 8;
    this.form = document.getElementById('animated-quiz-form');
    this.questions = document.querySelectorAll('.quiz-question');
    this.nextBtn = document.getElementById('next-btn');
    this.prevBtn = document.getElementById('prev-btn');
    this.submitBtn = document.getElementById('submit-btn');
    this.progressBar = document.querySelector('.progress-bar');
    this.currentQuestionSpan = document.getElementById('current-question');
    this.trainingNowInputs = document.querySelectorAll('input[name="training_now"]');

    this.init();
  }

  init() {
    const firstInvalid = this.detectServerInvalidQuestion();
    this.showQuestion(firstInvalid || 1);
    this.attachEventListeners();
    this.syncTrainingLabel();
  }

  attachEventListeners() {
    this.nextBtn.addEventListener('click', () => this.nextQuestion());
    this.prevBtn.addEventListener('click', () => this.prevQuestion());
    this.trainingNowInputs.forEach(input => {
      input.addEventListener('change', () => this.syncTrainingLabel());
    });

    // Prevent form submission on Enter in input fields
    this.form.addEventListener('keypress', (e) => {
      if (e.key === 'Enter' && e.target.tagName === 'INPUT') {
        e.preventDefault();
        this.nextQuestion();
      }
    });

    this.form.addEventListener('submit', (e) => {
      const invalidQuestion = this.findFirstInvalidQuestion();
      if (!invalidQuestion) {
        return;
      }

      e.preventDefault();
      if (invalidQuestion !== this.currentQuestion) {
        this.currentQuestion = invalidQuestion;
        this.showQuestion(this.currentQuestion);
      }
    });
  }

  showQuestion(questionNum) {
    // Hide all questions
    this.questions.forEach(q => {
      q.classList.remove('active', 'exit-left', 'exit-right');
    });

    // Show current question
    const currentQ = document.querySelector(`[data-question="${questionNum}"]`);
    if (currentQ) {
      currentQ.classList.add('active');
    }

    // Update progress bar
    const progress = (questionNum / this.totalQuestions) * 100;
    this.progressBar.style.setProperty('--progress', progress + '%');
    const progressAfter = this.progressBar.querySelector('::after');
    if (progressAfter || this.progressBar) {
      this.progressBar.style.setProperty('width', progress + '%', 'important');
    }
    // Update progress using pseudo-element
    this.updateProgressBar();

    this.currentQuestionSpan.textContent = questionNum;

    // Update button visibility
    if (questionNum === 1) {
      this.prevBtn.style.display = 'none';
      this.nextBtn.style.display = 'flex';
      this.submitBtn.style.display = 'none';
    } else if (questionNum === this.totalQuestions) {
      this.prevBtn.style.display = 'flex';
      this.nextBtn.style.display = 'none';
      this.submitBtn.style.display = 'flex';
    } else {
      this.prevBtn.style.display = 'flex';
      this.nextBtn.style.display = 'flex';
      this.submitBtn.style.display = 'none';
    }

    if (questionNum === 6) {
      this.syncTrainingLabel();
    }

    // Focus on first focusable element in the question
    const firstInput = currentQ?.querySelector('input, textarea, select');
    if (firstInput) {
      setTimeout(() => firstInput.focus(), 100);
    }
  }

  updateProgressBar() {
    const percentage = (this.currentQuestion / this.totalQuestions) * 100;
    const style = document.createElement('style');
    style.textContent = `.progress-bar::after { width: ${percentage}% !important; }`;

    // Remove old style if exists
    const oldStyle = document.querySelector('style[data-quiz-progress]');
    if (oldStyle) oldStyle.remove();

    style.setAttribute('data-quiz-progress', 'true');
    document.head.appendChild(style);
  }

  nextQuestion() {
    if (!this.validateQuestion(this.currentQuestion)) {
      return;
    }

    if (this.currentQuestion < this.totalQuestions) {
      const currentQ = document.querySelector(`[data-question="${this.currentQuestion}"]`);
      currentQ.classList.add('exit-left');

      setTimeout(() => {
        this.currentQuestion++;
        this.showQuestion(this.currentQuestion);
      }, 300);
    }
  }

  prevQuestion() {
    if (this.currentQuestion > 1) {
      const currentQ = document.querySelector(`[data-question="${this.currentQuestion}"]`);
      currentQ.classList.add('exit-right');

      setTimeout(() => {
        this.currentQuestion--;
        this.showQuestion(this.currentQuestion);
      }, 300);
    }
  }

  syncTrainingLabel() {
    const selected = document.querySelector('input[name="training_now"]:checked');
    const trainingPeriodLabel = document.querySelector('[data-question="6"] .quiz-question__title');
    const trainingGroup = document.getElementById('training-period-training');
    const pauseGroup = document.getElementById('training-period-pause');

    if (!selected || !trainingPeriodLabel) {
      return;
    }

    if (selected.value === 'yes') {
      trainingPeriodLabel.textContent = 'Сколько времени тренируешься подряд?';
      trainingGroup.style.display = '';
      pauseGroup.style.display = 'none';
      pauseGroup.querySelectorAll('input[type="radio"]').forEach(r => { r.checked = false; });
    } else {
      trainingPeriodLabel.textContent = 'Сколько не тренируешься?';
      trainingGroup.style.display = 'none';
      pauseGroup.style.display = '';
      trainingGroup.querySelectorAll('input[type="radio"]').forEach(r => { r.checked = false; });
    }
  }

  detectServerInvalidQuestion() {
    for (let i = 1; i <= this.totalQuestions; i++) {
      const question = document.querySelector(`[data-question="${i}"]`);
      if (question && question.querySelector('.errorlist li')) {
        return i;
      }
    }
    return null;
  }

  ensureErrorNode(question) {
    let node = question.querySelector('.quiz-validation-error');
    if (!node) {
      node = document.createElement('div');
      node.className = 'quiz-validation-error';
      question.appendChild(node);
    }
    return node;
  }

  showQuestionError(question, message) {
    const node = this.ensureErrorNode(question);
    node.textContent = message;
  }

  clearQuestionError(question) {
    const node = question.querySelector('.quiz-validation-error');
    if (node) {
      node.textContent = '';
    }
  }

  getValue(name) {
    const input = this.form.querySelector(`[name="${name}"]`);
    return input ? input.value.trim() : '';
  }

  getNumber(name) {
    const value = this.getValue(name);
    if (!value) {
      return null;
    }
    const n = Number(value.replace(',', '.'));
    return Number.isFinite(n) ? n : null;
  }

  isChecked(name) {
    return Boolean(this.form.querySelector(`input[name="${name}"]:checked`));
  }

  validateQuestion(questionNum) {
    const question = document.querySelector(`[data-question="${questionNum}"]`);
    if (!question) {
      return true;
    }

    this.clearQuestionError(question);
    let error = '';

    if (questionNum === 1) {
      if (!this.isChecked('gender')) {
        error = 'Выберите пол.';
      }
    }

    if (questionNum === 2) {
      const age = this.getNumber('age');
      if (age === null) {
        error = 'Введите возраст.';
      } else if (age < 12 || age > 90) {
        error = 'Возраст должен быть от 12 до 90.';
      }
    }

    if (questionNum === 3) {
      const weight = this.getNumber('weight');
      const height = this.getNumber('height');

      if (weight === null || height === null) {
        error = 'Введите вес и рост.';
      } else if (weight < 36) {
        error = 'Вес должен быть не меньше 36 кг.';
      } else if (height < 148 || height > 220) {
        error = 'Рост должен быть в диапазоне 148–220 см.';
      }
    }

    if (questionNum === 4) {
      const measureFields = ['chest', 'waist', 'hips', 'thigh', 'calves', 'biceps'];
      const missing = measureFields.some((field) => this.getNumber(field) === null);
      if (missing) {
        error = 'Заполните все поля обхватов.';
      }
    }

    if (questionNum === 5) {
      if (!this.isChecked('training_now')) {
        error = 'Выберите, тренируетесь ли вы сейчас.';
      }
    }

    if (questionNum === 6) {
      if (!this.isChecked('training_period')) {
        error = 'Выберите период тренировок/перерыва.';
      }
    }

    if (questionNum === 7) {
      if (!this.isChecked('goal')) {
        error = 'Выберите цель.';
      }
    }

    if (!error) {
      return true;
    }

    this.showQuestionError(question, error);
    return false;
  }

  findFirstInvalidQuestion() {
    for (let i = 1; i <= 7; i++) {
      if (!this.validateQuestion(i)) {
        return i;
      }
    }
    return null;
  }
}

// Initialize quiz when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new AnimatedQuiz();
  const resultOverlay = document.getElementById('quiz-result-overlay');
  const closeButton = document.getElementById('quiz-result-close');

  if (resultOverlay) {
    document.body.classList.add('modal-open');

    const closeOverlay = () => {
      resultOverlay.classList.remove('is-visible');
      document.body.classList.remove('modal-open');
    };

    if (closeButton) {
      closeButton.addEventListener('click', closeOverlay);
    }

    resultOverlay.addEventListener('click', (event) => {
      if (event.target === resultOverlay) {
        closeOverlay();
      }
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && resultOverlay.classList.contains('is-visible')) {
        closeOverlay();
      }
    });
  }
});
