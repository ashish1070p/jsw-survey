# JSW Motors Training Evaluation Portal

A Django-based training evaluation system implementing the Kirkpatrick 4-Level framework for JSW Motors MT and GET trainee programmes.

## Features
- **12 survey forms** — Happy Sheet, Pre/Post Assessment, BARS Technical/Behavioural/Leadership × 2 roles (MT & GET)
- **Cloud-ready** — PostgreSQL on Render or Railway; falls back to SQLite locally
- **Admin dashboard** — view responses, filter by role, export to Excel
- **QR code generation** — for all 12 survey URLs
- **Welcome page** — routes users to the correct survey by role

## Quick Deploy

### Render (recommended)
1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New → Blueprint
3. Point to your repo — `render.yaml` handles everything automatically
4. Set env vars: `SECRET_KEY`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`

### Railway
1. Push to GitHub
2. New project → Deploy from GitHub → select repo
3. Add a PostgreSQL plugin
4. Set `DATABASE_URL` (auto-set by Railway plugin), `SECRET_KEY`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`
5. Railway reads `railway.toml` automatically

## Local Development
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # edit .env
python manage.py migrate
python manage.py runserver
```

## Environment Variables
| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | (insecure default) | Django secret key — **change in prod** |
| `DEBUG` | `False` | Set to `True` for local dev only |
| `DATABASE_URL` | SQLite | PostgreSQL connection string |
| `ADMIN_USERNAME` | `admin` | Admin dashboard login |
| `ADMIN_PASSWORD` | `JSW@Admin2024` | Admin dashboard password |
| `BASE_URL` | auto-detected | Your app's public URL (for QR codes) |

## Admin Access
- URL: `/admin-login/`
- Default credentials: `admin` / `JSW@Admin2024`
- **Change password via environment variable before deploying**

## Survey URLs
| Role | Survey | URL |
|---|---|---|
| MT | Happy Sheet | `/survey/mt/happy-sheet/` |
| MT | Pre-Assessment | `/survey/mt/pre-assessment/` |
| MT | Post-Assessment | `/survey/mt/post-assessment/` |
| MT | BARS Technical | `/survey/mt/bars-technical/` |
| MT | BARS Behavioural | `/survey/mt/bars-behavioural/` |
| MT | BARS Leadership | `/survey/mt/bars-leadership/` |
| GET | Happy Sheet | `/survey/get/happy-sheet/` |
| GET | Pre-Assessment | `/survey/get/pre-assessment/` |
| GET | Post-Assessment | `/survey/get/post-assessment/` |
| GET | BARS Technical | `/survey/get/bars-technical/` |
| GET | BARS Behavioural | `/survey/get/bars-behavioural/` |
| GET | BARS Leadership | `/survey/get/bars-leadership/` |
