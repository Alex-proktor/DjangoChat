# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SESSION_ENGINE = 'redis_sessions.session'

API_KEY = '$0m3-U/\/1qu3-K3Y'

SEND_MESSAGE_API_URL = 'http://127.0.0.1:8000/messages/send_message_api'

# todo: При развёртывании на сервере не забудьте указать адрес, по которому будет доступен Tornado-сервер
# todo: (или вообще вынесите в отдельную переменную).
