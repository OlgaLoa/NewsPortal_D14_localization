import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gsh+ih2q-g0l-z)2f_7&#odg4k$-k-)rtmg#%x7v28vpd&5&wa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # приложение для перевода моделей
    'modeltranslation', # обязательно перед админом

    'django.contrib.admin',
     # встроенное прил. Django, которое добавляет пользователей
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # встроенное прил. Django, которое добавляет сообщения
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # встроенное прил. Django, которое добавляет настройки сайта
    'django.contrib.sites',
    'django.contrib.flatpages',

    'newapp.apps.NewappConfig', # назв приложения.apps.из app.ru приложения
    'django_filters',

    #приложения из пакета allauth (три обязательных приложения для работы allauth и одно,
    # которое добавит поддержку входа с помощью Yandex).
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',

    'django_apscheduler', # пакет использует указание времени периодического выполнения задач в стиле сron
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',

    # локализация
    'django.middleware.locale.LocaleMiddleware',
    'project.middlewares.TimezoneMiddleware',  # add that middleware!

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',

                # `allauth` обязательно нужен этот контекстный процессор
                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# интернационализация будет поддерживаться в нашем приложении
USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/news"
# нам нужно «включить» аутентификацию как по #username, так и специфичную по email или сервис-провайдеру
#Далее нам необходимо добавить бэкенды аутентификации:
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', #встроенный бэкенд Django
    'allauth.account.auth_backends.AuthenticationBackend', #бэкенд аутентификации, предоставленный пакетом allauth
]

ACCOUNT_EMAIL_REQUIRED = True #поле email является обязательным
ACCOUNT_UNIQUE_EMAIL = True  #поле email является уникальным.
ACCOUNT_USERNAME_REQUIRED = False #username необязательный
ACCOUNT_AUTHENTICATION_METHOD = 'email'  #аутентификация будет происходить посредством электронной почты.
ACCOUNT_EMAIL_VERIFICATION = 'none'#верификация почты отсутствует


ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSignupForm'}
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'#печать писем в консоль
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #отправка писем на адрес
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "olgalo-a@yandex.ru"
EMAIL_HOST_PASSWORD = "password"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "olgalo-a@yandex.ru" #будет использоваться как значение по умолчанию для поля from в письме.

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"#формат,в кот будет передаваться при рассылке
APSCHEDULER_RUN_NOW_TIMEOUT = 25 #кол-во секунд, за кот функция д вып-ся

SITE_URL ='http://127.0.0.1:8000'

CELERY_BROKER_URL = 'redis://localhost:6379' #указывает на URL брокера сообщений (Redis). По умолчанию он находится на порту 6379.
CELERY_RESULT_BACKEND = 'redis://localhost:6379' #указывает на хранилище результатов выполнения задач.

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache', #FileBasedCache класс, кот б подключать кэширование к Джанго (логика)
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    } # это склейка пути на компьютере + cache_files
}
# админы для отправки на почту при логировании
ADMINS = [('Olga', 'olgalo-aa@yandex.ru'),('Sveta', 'sveta-aa@yandex.ru')]
#для получения писем об ошибках
SERVER_EMAIL = EMAIL_HOST_USER

# логирование - словарь словарей
# LOGGING = {
#      'version': 1, #1-ый ключ version всегда определяется как 1
#      'disable_existing_loggers': False, #ключ disable_existing_loggers контролирует работу существующей (стандартной) схемы логирования Django
#      'style': '{',
#
#      #форматер - формат записи сообщений
#     'formatters': {
#        #вывод сообщений в консоль
#         'console_debug_formatter': #название форматера (формат для сообщений уровня DEBUG и выше с основного логгера django)
#             {'format': ' %(asctime)s %(levelname)s %(message)s', #вывод: время, уровень логирования сообщения и само сообщение
#             'datefmt': '%d.%m.%Y %H-%M-%S'},
#
#
#         'console_warning_formatter':   # название форматера (формат для сообщений уровня WARNING и выше с основного логгера django)
#             {'format': ' %(asctime)s %(levelname)s %(message)s %(pathname)s',
#             'datefmt': '%d.%m.%Y %H-%M-%S'},
#
#         'console_error_critical_formatter':   #название форматера (формат для сообщений уровня ERROR и CRITICAL с основного логгера django)
#             {'format': ' %(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
#             'datefmt': '%d.%m.%Y %H-%M-%S',},
#
#         #вывод сообщений в файлы
#        'file_general_formatter': {  #название форматера (формат для сообщений уровня INFO и выше)
#              'format': ' %(asctime)s %(levelname)s %(module)s %(message)s',
#              'datefmt': '%d.%m.%Y %H-%M-%S',},
#
#        'file_errors_formatter': {  # название форматера (формат для сообщений уровня ERROR и CRITICAL)
#              'format': ' %(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s ',
#              'datefmt': '%d.%m.%Y %H-%M-%S',},
#
#        'file_security_formatter': {  # название форматера (только сообщения, связанные с безопасностью, те из логгера django.security)
#              'format': ' %(asctime)s %(levelname)s %(module)s %(message)s',
#              'datefmt': '%d.%m.%Y %H-%M-%S',},
#
#         # отправка сообщений на почту
#        'email_error_formatter': {  # название форматера (только сообщения уровне ERROR и выше из django.request и django.server)
#              'format': ' %(asctime)s %(levelname)s %(message)s %(pathname)s ',
#              'datefmt': '%d.%m.%Y %H-%M-%S',}
#        },
#
#     # фильтры : в консоль сообщения отправляются только при DEBUG = True, а на почту и в файл general.log — только при DEBUG = False
#     'filters':
#         {
#             'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue', },
#
#             'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse', },
#         },
#
#     #  обработчики
#     'handlers': {
#
#     #обработчики для вывода в консоль
#         'console_DEBUG_handler':
#             {'level': 'DEBUG', #отправляет сообщения уровня DEBUG и выше в консоль
#              'filters': ['require_debug_true'], #кроме того, накладывается фильтр, определенный выше
#              'class': 'logging.StreamHandler',  #класс обработчика
#              'formatter': 'console_debug_formatter' }, #используется форматер, определенный выше
#
#        'console_WARNING_handler':
#             {'level': 'WARNING', #отправляет сообщения уровня WARNING и выше в консоль
#              'filters': ['require_debug_true'], #кроме того, накладывается фильтр, определенный выше
#              'class': 'logging.StreamHandler',
#              'formatter': 'console_warning_formatter'}, #используется форматер, определенный выше
#
#       'console_ERROR_CRITICAL_handler':
#             {'level': 'ERROR', #отправляет сообщения уровня ERROR и выше в консоль
#              'filters': ['require_debug_true'], #кроме того, накладывается фильтр, определенный выше
#               'class': 'logging.StreamHandler',
#              'formatter': 'console_error_critical_formatter' }, #используется форматер, определенный выше
#
#     #обработчики отправки в файл
#         'file_general_handler':  #2-ой обработчик
#             {'level': 'INFO', #отправляет сообщения уровня  и выше в консоль
#             'filename': 'general.log',     #файл создается автоматически
#              'class': 'logging.FileHandler',
#              'formatter': 'file_general_formatter',  # используется форматер, определенный выше
#              'filters': ['require_debug_false'],}, #кроме того, накладывается фильтр, определенный выше
#
#
#        'file_errors_handler':
#             {'level': 'ERROR',
#             'filename': 'error.log',
#              'class': 'logging.FileHandler',
#              'formatter': 'file_errors_formatter',}, # используется форматер, определенный выше
#
#
#        'file_security_handler':  #сообщения, связанные с безопасностью, а значит только из логгера django.security
#             {'level': 'INFO',
#             'filename': 'error.log',
#              'class': 'logging.FileHandler',
#              'formatter': 'file_security_formatter',}, # используется форматер, определенный выше
#
#
#       #обработчики отправки на почту
#       'mail_admins_handler': {
#           'level': 'ERROR', #передает сообщения уровня ERROR на отправление по почте из django.request и django.server
#           'class': 'django.utils.log.AdminEmailHandler',
#           'formatter': 'email_error_formatter',
#           'filters': ['require_debug_false'],},
#          },
#
#       # регистраторы
#    'loggers': { #регистраторы (логгеры)
#
#    #основной регистратор
#         'django': { #основной регистратор django отправляет ВСЕ сообщения ЧЕРЕЗ ОБРАБОТЧИКИ в консоль
#             'level': 'DEBUG',  #добавляем,чтобы попадало с уровня DEBUG (по умолчанию уровень - INFO)
#              'handlers': ['console_DEBUG_handler','console_WARNING_handler', 'console_ERROR_CRITICAL_handler', 'file_general_handler'], #указывается handler 'console', определенный выше
#              'propagate': True, },
#
#    #  регистратор django.request
#        'django.request': {
#              'level': 'ERROR',
#              'handlers': ['file_errors_handler', 'mail_admins_handler'],
#              'propagate': True,},
#
#        #  регистратор django.server
#        'django.server': {
#            'level': 'ERROR',
#            'handlers': ['file_errors_handler','mail_admins_handler'],
#            'propagate': True,},
#
#        #  регистратор django.template
#        'django.template': {
#            'level': 'ERROR',
#            'handlers': ['file_errors_handler'],
#            'propagate': True,},
#
#        #  регистратор django.db.backends
#        'django.db.backends': {
#            'level': 'ERROR',
#            'handlers': ['file_errors_handler'],
#            'propagate': True,},
#
#        #  регистратор django.security
#        'django.security': {
#            'level': 'INFO',      #по умолчанию  Warning
#            'handlers': ['file_security_handler'],
#            'propagate': False,},} } # если не надо, чтобы он был дополнительно обработан родительскими Handler классами; передача управления "вверх" до родителя будет запрещена

#локализация
# и нужно создать еще папку locale для локализации
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# список доступных языков
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)
