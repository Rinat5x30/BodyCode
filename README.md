# BodyCode

A web application that generates personalized workout programs based on user metrics, goals, and training history.

**Live:** [bodycode.lol](https://bodycode.lol)

---

## Features

- **Personalized program generation** — builds split types (Fullbody, Push-Pull, Upper-Lower, PPL, Bro-Split) based on experience level, goals, and weekly availability
- **Animated multi-step quiz** — step-by-step form with smooth transitions and real-time validation
- **Injury-aware filtering** — automatically excludes exercises based on declared contraindications
- **Gender & goal adjustments** — separate volume, intensity, and calorie targets for cut / bulk / maintenance
- **Bench press guide** — structured weekly progression guide with an accordion UI
- **Fully responsive** — custom dark-theme CSS, works on all screen sizes

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0.4, Python |
| Server | Gunicorn + WhiteNoise |
| Database | SQLite (dev) |
| Frontend | Vanilla JS, custom CSS3 |
| Deployment | Heroku |

---

## Local Setup

**Requirements:** Python 3.10+

```bash
# Clone the repo
git clone https://github.com/Rinat5x30/BodyCode.git
cd BodyCode

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and set your SECRET_KEY

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000)

---

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key | — (required) |
| `DEBUG` | Enable debug mode | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `bodycode.lol,www.bodycode.lol` |

---

## Project Structure

```
BodyCode/
├── bodycode_project/      # Django project config (settings, urls, wsgi)
├── main/                  # Main application
│   ├── templates/main/    # HTML templates
│   ├── static/main/       # CSS, JS, images
│   ├── forms.py           # Quiz form definition
│   ├── views.py           # View functions
│   ├── program_generator.py  # Core workout generation logic
│   └── urls.py
├── .env.example
├── requirements.txt
└── Procfile               # Heroku entry point
```

---

## Deployment (Heroku)

```bash
heroku create
heroku config:set SECRET_KEY=<your-key> DEBUG=False ALLOWED_HOSTS=<your-domain>
git push heroku main
heroku run python manage.py migrate
```

---

## License

MIT
