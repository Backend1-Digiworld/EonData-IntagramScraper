SQL_SERVER_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

START_DATE_FOR_GET_ALL_POSTS = '2020-08-01 00:00:00'

POST_ID_CHECK = 'CSFobZzgH9c'

DATA_PER_REQUEST = 10

MAX_COMMENTS_FOR_CHECK = 40

MAX_POSTS = 10000

MAX_COMMENTS = 10000

SLEEP_TIME_BETWEEN_CHANGE_ACCOUNT = 60

MAX_REQUEST_BEFORE_CHANGE_ACCOUNT = 500

MAX_FOLLOWERS = 10000

DELAY_GET_LIST_FOLLOWERS = 100

PATH_TO_CACHE = 'sessions'

DATABASE = {
    'ENGINE': 'mssql',
    'DRIVER': 'pymssql',
    'SERVER': 'instancia-eondata-slqstandard.cgfqzq6uafae.us-east-1.rds.amazonaws.com',
    'NAME': 'BD_INSTAGRAM',
    'USER': 'User_SL',
    'PASSWORD': 'user202204',
    'PORT': 1433
}

DATABASE_URL = (f"{DATABASE['ENGINE']}"
                f"+{DATABASE['DRIVER']}"
                f"://{DATABASE['USER']}"
                f":{DATABASE['PASSWORD']}"
                f"@{DATABASE['SERVER']}"
                f":{DATABASE['PORT']}"
                f"/{DATABASE['NAME']}")
