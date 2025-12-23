# Clients & Projects

Small Django project to manage freelance clients, projects and tasks.
(REST API with Django REST Framework is planned.)
___

## 🌟 Tech Stack

- **Backend:** Django (Python)
- **Templating:** Django templates (HTML)
- **Database:** SQLite by default (PostgreSQL planned via Docker)
- **Containerization:** Docker, docker-compose
- **Forms:** Django `ModelForm` (create/update flows)
- **Styling / JS:** Basic HTML; Bootstrap / JS planned

___

## ✅ Prerequisites

To run the project you’ll need:

- **Git** – to clone the repository  
  https://git-scm.com/downloads  

- **Docker** (recommended way to run)  
  - Docker Desktop (macOS / Windows)  
  - Docker Engine (Linux)  
  https://docs.docker.com/get-docker/

Optional (only if you want to run without Docker):

- **Python 3.11+**  
  https://www.python.org/downloads/  

Any editor/IDE works:

- PyCharm Community Edition, VS Code, or any other editor that supports Python.

---

## 📥 Clone the Repository

```bash
git clone https://github.com/Annette3125/freelancer-crm.git
cd freelancer-crm
```

🚀 Option A – Run with Docker (recommended)

You don’t need a local Python setup for this option – everything runs inside Docker.

1. Environment file

Copy the sample env file:

```bash
cp .env.sample .env
```

Edit .env and set your own secret key (example):
```bash
DJANGO_SECRET_KEY=your-very-secret-key-here
DEBUG=True
```

2. Build and start the app

```bash
docker compose build
docker compose up
```

On first run, apply migrations (inside the container):
```bash
docker compose exec web python manage.py migrate

```
(If you change models and add new migrations later, you can run makemigrations + migrate in the same way.)

3. Admin user (optional)

```bash
docker compose exec -it web python manage.py createsuperuser
```

4. URLs
	•	Home: http://127.0.0.1:8002/
	•	Clients list: http://127.0.0.1:8002/clients/
	•	Projects list: http://127.0.0.1:8002/clients/projects/
	•	Admin: http://127.0.0.1:8002/admin/

To stop the app:
```bash
docker compose down
```
ℹ️ For demo purposes, the repository may include a small SQLite database 
(db.sqlite3) with sample clients and projects. If present, you’ll see example data right after starting the app.


🧪 Option B – Run locally (without Docker)

If you prefer to run Django directly on your machine.

1. Create a virtual environment

From the project root:

	•	Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

	•	Windows (PowerShell):
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

	•	Windows (CMD):
```bash
python -m venv venv
venv\Scripts\activate.bat
```

2. Upgrade pip

```bash
python -m pip install --upgrade pip
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Environment file

```bash
cp .env.sample .env
```

Edit .env:
```bash
DJANGO_SECRET_KEY=your-very-secret-key-here
DEBUG=True
```
||| The values in .env.sample are only examples, not real secrets.


5. Apply migrations and run the server

```bash
python manage.py migrate
python manage.py runserver 8002
```
Open:
	•	http://127.0.0.1:8002/


## 🌟 Features

- **Clients management**
  - Create, edit and list clients
  - Store company name, country, status, notes
  - Optional links: GitHub, LinkedIn, personal website
  - Avatar URL support

- **Projects management**
  - Create projects and link them to clients
  - Track project status (Lead / Planned / In progress / Completed)
  - Store budget, description, important notes
  - See all projects for a specific client

- **Clean relationships**
  - `Client` ↔ `Project` via `ForeignKey`
  - Reverse access: `client.projects.all()` using `related_name`

- **Basic UI**
  - HTML templates with inheritance (`base.html`)
  - Clients list, detail view, projects list
  - Simple navigation between clients and projects

- **Dockerized setup**
  - Application runs inside a Docker container
  - Easy to start and stop locally

This project is actively evolving — I’m extending it step-by-step with new features, tests and JS.


### 🔭 Planned / Next Steps

- Django REST Framework (DRF) API endpoints for clients and projects  
- Switch to PostgreSQL in Docker setup  
- Frontend improvements with Bootstrap / Tailwind and basic JavaScript  
- Simple filters (e.g. by status) and small dashboard counters  
- Basic tests (views, models, forms)

---

##### Disclaimer

This repository is part of my personal portfolio.
It is intended for educational and demonstration purposes only.
Not production-ready without further hardening and security review.


## About me

I enjoy building backend tools with Python and Django.
I like taking the time to understand how things work under the hood
and using projects like this one 🌍🪽🌱.

******
******
✨
******
******