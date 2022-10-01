"""
1. Git - Source control
- Local and remote repos
- Code distribution between the teams
- Workflow implementation
- Independent execution of each team member
- Historical code versions

- Flow ->
Push and pull strategy, merge and push back in the pipeline

- main/master branch -> Stable code
- Features are made on feature branches
- Forking -> getting the current code from main to a branch

- Commands

git add files/folders - preparation of files
git remote add origin url
git commit -m "message" - creates a commit for push
git push origin BRANCH_NAME - local to VCS
git pull origin BRANCH_NAME
git checkout -b NEW_BRANCH
git status

git clone REPO_ADDRESS
git diff

git remote get-url origin/heroku

2. GitHub
- SSH Keys auth - ls -al ~/.ssh
-
-

3. Deployment
- Push changes / update from one env to another
Local -> Development -> Staging -> Live

Heroku deployment
- Heroku GIT system
- Github
- Image

pip install whitenoise <= Static files
pip install psycopg2-binary
pip install gunicorn
pip freeze > requirements.txt

- "Procfile" -> Buildpack Error: REQUIREMENTS.TXT, PROCFILE OUTSIDE THE APP FOLDER,
Procfile content -
web: gunicorn --pythonpath <project name> <project name>.wsgi
release: python <project name>/manage.py migrate <------ Fixing the migrations

- settings.py changes with heroku info
ALLOWED_HOSTS = ["127.0.0.1", "heroku site URL",]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"
STATICFILES_DIRS = (BASE_DIR / "static",)


Heroku PostgreSQL: (HEROKU SQLite not supported)
Resources -> Database Credentials -> User, host, port, pass etc switch in settings

Static files in deployment => whitenoise config (storage) settings.py

N.B.!
DEPLOYMENT GITHUB DATABASE PRODUCTION DATA
"""