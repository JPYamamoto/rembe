import environ

env = environ.Env()
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
