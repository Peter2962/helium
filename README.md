# Helium

Python Rest API scaffold built on top of Flask and Flask Restful

## Installation
As this package is not available on pypi, it can only be cloned.
```bash
> git clone https://github.com/Peter2962/helium.git
> cd helium
> cp .env.example .env
> pip install -r requirements.txt
```

## Configuration
Note: Only MySQL database is supported at the moment.
The database can be configured in the .env file.

_MYSQL_HOST=None_
_MYSQL_USERNAME=None_
_MYSQL_PASSWORD=None_
_MYSQL_DATABASE=None_

The .env file also contains _APP_PORT_ and _APP_HOST_ env variables. This is where you set your host and port that the app will make use of.

Also note that the _APP_SECRET_ needs to be set for jwt implementation to work.

## Registering middlewares
Middlewares are located in the _/middlewares_ directory.
You can create a new middleware and register it in _config.py_ -> _middlewares_ config option.
_Middlewares_ are loaded into app automatically

## Registering models
Models are located in the _/models_ directory.
You can create a new model and register it in _config.py_ -> _models_ config option
_Models_ are loaded into app automatically

## Defining routes
All routes are defined in _config.py_ -> _routes_mapping_.
The _routes_mapping_ variable is a list of dicts and each dict defines a single route.

Each dict contains three keys:
- _path_ - Route path
- _resource_ - The controller and method that will be called for the defined route
- _method_ - Request method that is allowed for a route

An example route:
```python
{
	'path': '/api',
	'resource': 'ApiController.getData',
	'method': 'GET'
}
```