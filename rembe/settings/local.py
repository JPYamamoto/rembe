import environ

env = environ.Env(
    GH_ACTIONS=(bool, False)
)
environ.Env.read_env()

SECRET_KEY = 'django-insecure-i-oass(559zhi#-3g(p$ot5x=kf!w-qj(2_a-*g__l%7)21aqd'

ENV_ALLOWED_HOSTS = ['localhost',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

if env('GH_ACTIONS'):
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
