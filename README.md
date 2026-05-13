<div align="center">

# BodyCode

**Personalized workout program generator — built with Django**

[![Live](https://img.shields.io/badge/Live-bodycode.lol-FF5A1F?style=flat-square)](https://bodycode.lol)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Railway](https://img.shields.io/badge/Deployed_on-Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)](https://railway.app)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

[**→ Try it live at bodycode.lol**](https://bodycode.lol) 

</div>

---
 
## What is BodyCode?

BodyCode is a full-stack web application that builds a **personalized training program** in seconds. The user fills out a multi-step quiz — age, weight, body measurements, training experience, goals, injuries — and the backend algorithm produces a structured weekly split tailored specifically to them.

No accounts. No subscriptions. Just data in, program out.

---

## How It Works

The core logic lives in `main/program_generator.py`. Given the quiz answers, the engine:

1. **Selects a split type** based on experience level and training frequency
   - Beginner → Fullbody / Upper-Lower
   - Intermediate → Push-Pull / Push-Pull-Legs
   - Advanced → Bro-Split / PPL
2. **Filters the exercise pool** by declared injuries and contraindications
3. **Adjusts volume and intensity** based on goal (cut / bulk / maintenance) and gender
4. **Calculates calorie and macro targets** from body metrics (weight, height, age, activity level)
5. **Outputs a weekly schedule** with sets, reps, and focus muscle groups per session

---

## Features

- **Animated multi-step quiz** — smooth slide transitions, real-time client-side validation, progress bar
- **Smart program generation** — 5 split types, 50+ exercises, injury-aware filtering, gender-specific load adjustments
- **Bench press progression guide** — 12-week structured program with a collapsible week-by-week accordion UI
- **Fully custom dark UI** — no CSS framework, pure CSS3 with CSS variables, `clamp()` responsive typography, and orange accent theme
- **Production-ready** — CSRF protection, HSTS, secure cookies, `X-Frame-Options: DENY`, WhiteNoise static serving

---

## Tech Stack

| Layer | Technology | Notes |
|---|---|---|
| Backend | Django 6.0.4 | Views, forms, template engine |
| Server | Gunicorn + WhiteNoise | Production WSGI + static files |
| Deployment | Railway | Connected to GitHub, auto-deploy on push |
| Database | SQLite | Dev / lightweight prod |
| Frontend | Vanilla JS + CSS3 | No frameworks, fully custom |
| Fonts | DM Sans, Syne, Bebas Neue | Google Fonts |
| Deployment | Railway | `Procfile` included, auto-deploy on push |
| Config | python-decouple | `.env`-based secrets management |

---

## Local Setup

**Requirements:** Python 3.10+

```bash
# 1. Clone
git clone https://github.com/Rinat5x30/BodyCode.git
cd BodyCode

# 2. Virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Environment
cp .env.example .env
# Open .env and set SECRET_KEY (generate one with: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")

# 5. Migrate & run
python manage.py migrate
python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000)

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `SECRET_KEY` | Yes | Django secret key |
| `DEBUG` | No | `True` for dev, `False` for prod (default: `False`) |
| `ALLOWED_HOSTS` | No | Comma-separated hosts (default: `bodycode.lol,www.bodycode.lol`) |

---

## Project Structure

```
BodyCode/
├── bodycode_project/
│   ├── settings.py            # Config via python-decouple
│   ├── urls.py
│   └── wsgi.py
├── main/
│   ├── templates/main/
│   │   ├── quiz.html          # Standard quiz (landing page)
│   │   ├── animated_quiz.html # Animated multi-step quiz
│   │   └── guide_bench_press.html
│   ├── static/main/
│   │   ├── styles.css         # Main stylesheet (~1600 lines, custom dark theme)
│   │   ├── animated_quiz.css  # Quiz-specific overrides
│   │   └── animated_quiz.js   # Quiz step logic & result modal
│   ├── forms.py               # QuizForm — all input fields & validation
│   ├── views.py               # View functions
│   ├── program_generator.py   # Core algorithm — split selection, exercise filtering, macros
│   └── urls.py
├── .env.example
├── requirements.txt
├── Procfile
└── README.md
```

---

## Deployment (Railway)

1. Push the repo to GitHub
2. Create a new project on [railway.app](https://railway.app) → **Deploy from GitHub repo**
3. Set environment variables in the Railway dashboard:

   | Variable | Value |
   |---|---|
   | `SECRET_KEY` | generate with `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
   | `DEBUG` | `False` |
   | `ALLOWED_HOSTS` | `your-domain.up.railway.app` |

4. Railway auto-detects `Procfile` and deploys on every push to `main`

---

## License

MIT 
