Monopoly
---

A monopoly game simulation for 4 players strategy.

## Architecture
I opted for DDD simplified architecture in this project. We have the **entities/**
dir where are stored all the entities and its game rules. At **usecases/** dir
are stored all operations that could be made in entities. we also have a class 
GameEngine responsible for orchestrate de usecases.


## Building
For build I sugest to use python **virtualenv**.
``` bash
$ cd monopoly/
$ python -m pip install virtualenv
$ python -m virtualenv venv
```

Activate virtual env
``` bash
$ source ./venv/bin/activate
```

Install dependencies
``` bash
$ python -m pip install -r requirements.txt
```

## Running
execute: 
``` bash
$ python ./monopoly.py
```
or
``` bash
$ chmod +x ./monopoly.py
$ ./monopoly.py
```

## Test
For test we are using py test, so just run:
``` bash
$ pytest
```