
# News Board Api 

#### Simple REST API builded with Django-rest-framework.

## Check Swagger documentation: 
https://news-api-board-test.herokuapp.com/redoc/

## Heroku deployment link: 
https://news-api-board-test.herokuapp.com/

# Run Locally


### Follow next steps:
1. Clone this repository to your local machine
```bash
  git clone https://github.com/Denys8887/News_API
```

2. Create virtual environment and activate it:
```bash
  python3 -m venv env
  source env/bin/activate
```

3. Open terminal in project's root directory and build Docker container with
```bash
  docker-compose build
```

4. Init database schema with
```bash
  python manage.py migrate
```

5. Create admin user to manage site with
```bash
  python manage.py createsuperuser
```

6. In settings.py write your SECRET_KEY, DEBUG = True and 
```bash
  python manage.py runserver 
```
# Tools



- Python 3
- Django and Django REST Framework
- PostgresSQL
- Formatted with Black
- Flake8 
- Swagger 
- Celery 
- Redis
- Docker 
