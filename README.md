Texaco   [![Build Status](https://travis-ci.org/abnerpc/texaco.svg?branch=master)](https://travis-ci.org/abnerpc/texaco)
======

Texaco is an application for calculate best routes.


Dependences
===========

Texaco is built using Flask framework. There are requirement files for each environment such as development and production.
The development environment contains libraries for debug and tests.


Instalation
===========

First of all, create a python virtual environment and activate it:

```bash
$ virtualenv env
$ source env/bin/activate
```

To install de dependences run the following commands:

> Development environment

```bash
$ make requirements-dev
```

> Production environment

```bash
$ make requirements
```

Also, for production, you will find configuration files for nginx, gunicorn and supervisor in contrib folder.
Use it as you wish ;).


Running
=======

Before running it, remember to activate the virtual environment.

```bash
$ make run
```

Yeah, that is it.


Running the tests
=================

Again, remember to activate the virtual environment.

```bash
$ make test
```

Right!

==================
![python](https://www.python.org/static/community_logos/python-logo.png)
&nbsp;
![flask](http://flask.pocoo.org/static/badges/flask-powered.png)