# django-blog
This should be a django-blog but I decide use django functionalities to improve a personal site where you can know What day is today.

## Project installation
```
git clone https://github.com/ssoto/django-blog django-blog
cd django-blog
virtualenv env
source env/bin/activate --python=`which python3`
pip install requirements.txt
./manage.py migrate
```
You will need a django admin superuser:
```
./manage.py createsuperuser  
```
Run your django:
```
./manage.py runserver
```
And finally acces: [http://localhost:8000](http://localhost:8000)
