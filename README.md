# Acai Exercise

##  How To Run
1. In VScode, clone repository
2. In terminal, create venv and activate it:
```
 $  python -m venv .venv
 $  source .venv/bin/activate
```
3. Insatll dependencies
```
 $  pip install -r requirements.txt
```
4. Create Superuser:
```
 $  python manage.py createsuperuser --username admin
     (follow instructions)
```
5. Make migrations and runserver:
```
 $  python manage.py makemigrations
 $  python manage.py migrate
 $  python manage.py runserver
```
5. Open url in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


##  Notes
1. admin and user groups are added in migration 0002
2. once logged in, the user page will not be visible until your username is associated with the 'admin' group via the admin portal (gear icon in nav bar)
