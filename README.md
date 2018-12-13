# DjangoChat
Simple chat

Use Python 3.6

I create with this - https://habr.com/post/160123/

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