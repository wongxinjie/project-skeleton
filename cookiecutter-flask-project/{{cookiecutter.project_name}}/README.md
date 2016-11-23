### {{cookiecutter.project_name}}

#### Getting Start
1. creete an virtualenv for project, install requirements and set environment value at env/bin/postactive
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
export SECRET_KEY=VALUE
export SQLALCHEMY_DATABASE_URI=VALUE
```

2. create database for project
```
CREATE DATABASE {{cookiecutter.project_db}} DEFAULT CHARSET=UTF8;
```

3. migrate databaset
```
python manage.py createdb dev
python manage.py runserver -h 0.0.0.0 -p 8014
```

#### Running Dev Server
```
python manage.py runserver -h [HOST(0.0.0.0)] -p [PORT(8000)]
```


#### Run Testing
```
py.test
```

#### Deployment
```
gunicorn -w 4 -b 0.0.0.0:8014 app.wsgi:app
```
