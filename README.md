
# Job-Management-System

### How to run single Celery

celery -A settings --workdir=./tasks  worker -l info


### How to run using docker-compose

``` sudo docker-compose up ```


### How to build and run single docker image/container

Building Image: 
``` sudo docker build -t celery-image . ```

Run Container With Keep STDIN TTY (keeping terminal):

``` sudo docker run -it --network=host celery-image ```

Run Bash:
``` sudo docker run -it celery-image /bin/bash ```


### How To run Redis locally

Redis docker:

``` sudo docker run --name=redis-server -p 6379:6379 -d redis```


### How To Set up Celery-Flower 

```celery -A settings flower --port=5555```


### Run Celery locally 

``` sudo docker run -it --network=host celery-image /bin/bash ```

then:

``` celery -A settings --workdir=./tasks  worker & ```



### How to test using terminal

``` 
$ python3
>> from settings import app
>> from tasks.math import *
>> a = system_math_add.delay(1,3);
>> a.get()
```

For more information follow http://docs.celeryproject.org/en/latest/getting-started/index.html


