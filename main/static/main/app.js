const trainingNowInputs = document.querySelectorAll('input[name="training_now"]');
const periodStepLabel = document.getElementById("period-step-label");

function syncTrainingLabel() {
    const selected = document.querySelector('input[name="training_now"]:checked');
    if (!selected || !periodStepLabel) {
        return;
    }

    if (selected.value === "yes") {
        periodStepLabel.textContent = "06 / Сколько времени тренируешься подряд";
    } else {
        periodStepLabel.textContent = "06 / Сколько не тренируешься";
    }
}

trainingNowInputs.forEach((input) => input.addEventListener("change", syncTrainingLabel));
syncTrainingLabel();

if (document.getElementById("dashboard")) {
    document.getElementById("dashboard").scrollIntoView({ behavior: "smooth", block: "start" });
}

const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach((item) => {
    item.addEventListener("toggle", () => {
        if (!item.open) {
            return;
        }

        faqItems.forEach((otherItem) => {
            if (otherItem !== item && otherItem.open) {
                otherItem.removeAttribute("open");
            }
        });
    });
});
