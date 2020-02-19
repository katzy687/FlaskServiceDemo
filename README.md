# FlaskServiceWin32
Python Flask sample for windows service registration.

## Requirements
  * pywin32, flask, waitress
  * Python 3.7.1 for this demo

## how to setup
  * Pip Install Requirements to python environment
  * In service class,  modify  name, display name, and description
  * admin cmd open
  * service install: `#python service_name.py install`
  * check service: `#sc query svc_name`
  * update service: `#python service_name.py update`
  * Start service: `#sc start svc_name` or `#python service_name.py start`
  * Stop service: `#sc stop svc_name` or `#python service_name.py stop`
  * If you want to delete this service: `#sc delete svc_name`
