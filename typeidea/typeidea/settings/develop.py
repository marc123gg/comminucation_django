from .base import * # NOQA
# noqa用于告诉ｐｅｐ８规范检查工具，这个地方不需要检测
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

