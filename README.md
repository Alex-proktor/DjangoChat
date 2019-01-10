# DjangoChat
Simple chat with tornado and redis.

Use Python 3.6

I create with this - https://habr.com/post/160123/
https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/%D0%90%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F

install redis:
```
sudo apt update
sudo apt upgrade
sudo apt install redis-server
```

test install redis
```
sudo redis-cli ping
```
In case of successful installation, the text will come back - PONG



install python packages:

```
pip install -r req.txt
```

```
python manage.py migrate

python manage.py makemigrations privatemessages
```


```
python manage.py createsuperuser
```

Install  Redis for Windows
```
Download the latest Redis.msi file from
https://github.com/MSOpenTech/redis/releases
after installation. The redis service is installed, we can use it from the Service manager
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

