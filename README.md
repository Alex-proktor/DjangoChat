# DjangoChat
Simple chat

Use Python 3.6

I create with this - https://habr.com/post/160123/
https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/%D0%90%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F

install python packages:
```
pip install -r req.txt
```

python manage.py migrate

python manage.py makemigrations privatemessages

Chenge in "venv/Lib/site-packages/brukva/client.py"
```
except Exception, e:
```
on 
```
except Exception as e:
```

```
python manage.py createsuperuser
```

Start server:
```
python manage.py runserver
python manage.py starttornadoapp
```

login/logout accounts 
```
http://127.0.0.1:8000/accounts/login/
http://127.0.0.1:8000/accounts/logout/
```