# About Flask scaffold
### Structure
 - project root
   - ```start.sh``` # a bash script that starts up http server for developing
   - ```manage.py``` # the entrance of project
   - ```requirements.txt``` # python dependency
   - ```Makefile``` # automation script
   - ```config``` # where configuration is placed, includes config for development\staging\production
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
TODO
