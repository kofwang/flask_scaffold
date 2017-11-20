# About Flask scaffold
### Structure
 - project root
   - ```start.sh``` # a bash script that starts up http server for developing
   - ```manage.py``` # the entrance of project
   - ```requirements.txt``` # python dependency
   - ```Makefile``` # automation script
   - ```config``` # where configuration are placed, includes config for development\staging\production
     - ```default.py``` # where default configuration are placed
     - ```development.py``` # where development configuration are placed
     - ```staging.py``` # where staging configuration are placed
     - ```production.py``` # where production configration are placed
   - ```app``` # where real application is placed
     - ```url.py``` # where router are defined, includes restful api and url
     - ```views``` # where normal views are defined
     - ```api_views``` # where restful api view are defined
     - ```tests``` # where unit test cases are placed
     - ```models``` # where database schema are placed
     - ```templates``` # where html templates are placed
### Preparation of your project
#### Make a virtual environment
TODO
#### Install dependency
```
$ cd flask_scaffold
$ make env
```
### Development
#### Start your http server
```
$ ./start.sh
```
#### Run your unit test case
```
$ make test
```
#### How to customize your flask config
Default configuration of Flask should be placed inside ```config/default.py```, for example: 
```py
...
DEBUG = False
SECRET_KEY = 'abcdefg'
SESSION_TYPE = 'filesystem'
...
```
```config/development.py``` are used to define configuration of development enviornment, which can overwrite ```config/default.py```
#### How to add view routing
View routing are defined in ```app/url.py```
```py
def init_view_url(app):
    """
    Place your www router here
    """
    from .views.helloworld import www_index
    app.add_url_rule('/', 'www_index', www_index)
    app.add_url_rule('/test/', 'www_index', www_index)
```
All you need to do is just put your routing inside init_view_url like the example above. Dont forget define your views inside ```app/views/```.
#### How to add api routing
Api routing are defined in ```app/url.py```
```py
def init_api_url(api):
    """
    Place your api router here
    """
    from .api_views.helloworld import HelloWorld
    api.add_resource(HelloWorld, '/helloworld')
```
Like view routing, all you need to do is just put api routing inside init_api_url, and put your api view inside ```app/api_views/```.
#### How to add unit test case
All UT cases are placed in ```app/tests/```. Scaffold are using ```unittest``` as its UT framework, so you have to make sure every test case you write is following rules of ```unittest```. And we also suggest that files that put in ```app/tests``` should name with prefix ```test_```, so that test case can be discovered automatically by ```unittest```.
#### How to write end to end test case
TODO
#### How to manage your static files
TODO
