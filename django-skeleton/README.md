#### django-project-skeleton-creator
skeleton-creator is a simple python script to create and reorganize projects.It turns out to be like:
```
project-name/
    apps/
        __init__.py
        ...
    website/
        settings.py
        ...
    static/
    templates/
    tests/
    README.md
    README.rst
```

##### install
create an virtualenv first, then:
```
git clone git@github.com:wongxinjie/project-skeleton.git
cd django-skeleton
python setup.py
```

##### usage
```
# init an empty django project
django-skeleton startproject project-name
cd project-name && django-skeleton startapp app-name
```
