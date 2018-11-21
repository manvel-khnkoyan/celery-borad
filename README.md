
# Job-Management-System

### How to run single Celery

celery -A settings --workdir=./tasks  worker -l info


### How to run using docker-compose

``` sudo docker-compose up ```


### How to test using terminal

``` 
$ python3
>> from settings import app
>> from tasks.math import *
>> a = system_math_add.delay(1,3);
>> a.get()
```

For more information follow http://docs.celeryproject.org/en/latest/getting-started/index.html


