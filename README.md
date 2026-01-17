# Django CRM Web Application

A simple CRM-style web application built with **Django** (university project).

## Project Files

The source code is stored in the archive:

- `final_project.zip`

## Getting Started (Local Setup)

### 1) Create a folder for the project
Create any folder on your computer where you want to keep the project.

### 2) Create and activate a virtual environment

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```
macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
3) Download and extract the project
Download final_project.zip from this repository.

Extract (unzip) it inside your project folder.

After extraction, go into the folder that contains manage.py.

4) Install dependencies
If requirements.txt exists, run:

```bash
pip install -r requirements.txt
```
If requirements.txt does not exist, install Django:
```bash
pip install django
```
5) Run migrations
In the same folder as manage.py:
```bash
python manage.py migrate
```

6) Start the server
```bash
python manage.py runserver
```
Open in browser:
http://127.0.0.1:8000/
