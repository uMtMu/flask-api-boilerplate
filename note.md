# Setup
```sh
virtualenv env  
. env/bin/activate  
pip install -r requirements.txt  
./manage.py db upgrade
./manage.py runserver
```

# Tools
```sh
sudo apt-get install sqlitebrowser  
```

# REST API calls
## create user (cli)
```python
import manage  
from app.auth import models  
u = models.User("umt", password="12345")  
manage.db.session.add(u)  
manage.db.session.commit()  
```

## create user (api call)
```
POST /auth/users/ HTTP/1.1  
Host: localhost:5000  
Authorization: Token   eyJhbGciOiJIUzI1NiIsImV4cCI6MTUyNzY4NDEwMywiaWF0IjoxNTI3NjgzNTAzfQ.eyJpZCI6MX0.s8qYJdl6B1CxcoA1LyJ1zPGKzaI3IZ45RxGs1PXslAU  
Cache-Control: no-cache  
Postman-Token: f9a758bf-ed94-3143-5687-ee8a77c527fd  
Content-Type: multipart/form-data; boundary=----  WebKitFormBoundary7MA4YWxkTrZu0gW  

------WebKitFormBoundary7MA4YWxkTrZu0gW  
Content-Disposition: form-data; name="username"  
  
bob  
------WebKitFormBoundary7MA4YWxkTrZu0gW  
Content-Disposition: form-data; name="password"  
  
12345  
------WebKitFormBoundary7MA4YWxkTrZu0gW--  
```

## get token
```
POST /auth/login/ HTTP/1.1  
Host: localhost:5000  
Cache-Control: no-cache  
Postman-Token: 0993a058-5742-38d6-bac5-e8ff1118091a  
Content-Type: multipart/form-data; boundary=----  WebKitFormBoundary7MA4YWxkTrZu0gW  
  
------WebKitFormBoundary7MA4YWxkTrZu0gW  
Content-Disposition: form-data; name="username"  
  
pat  
------WebKitFormBoundary7MA4YWxkTrZu0gW  
Content-Disposition: form-data; name="password"  
  
12345  
------WebKitFormBoundary7MA4YWxkTrZu0gW--  
```

## get user details
```
GET /auth/users/pat HTTP/1.1  
Host: localhost:5000  
Authorization: Token   eyJhbGciOiJIUzI1NiIsImV4cCI6MTUyNzY4MzAxMywiaWF0IjoxNTI3NjgyNDEzfQ.eyJpZCI6MX0.I6iXqdomHhKrLu_i-dXhKbFQ7CKmhEXRCR4o7LqDSxc  
Cache-Control: no-cache  
Postman-Token: 60b8b0c9-21f2-8dfc-53ca-680fb6eb894b  
  
  
## get all users
GET /auth/users/ HTTP/1.1  
Host: localhost:5000  
Authorization: Token   eyJhbGciOiJIUzI1NiIsImV4cCI6MTUyNzY4MzAxMywiaWF0IjoxNTI3NjgyNDEzfQ.eyJpZCI6MX0.I6iXqdomHhKrLu_i-dXhKbFQ7CKmhEXRCR4o7LqDSxc  
Cache-Control: no-cache  
Postman-Token: 60b8b0c9-21f2-8dfc-53ca-680fb6eb894b  
```

# Details about code
## flask blueprints
A Blueprint object works similarly to a Flask application object, but it is not actually an application. Rather it is a blueprint of how to construct or extend an application. -> [flask-api-boilerplate/app/auth/resources.py:10](https://github.com/uMtMu/flask-api-boilerplate/blob/54ef590c7ff95804beebc24eb0de43acb4a64377/app/auth/resources.py#L10)  
app1  
--> app1_blueprint1  
--> app1_blueprint2  
--> app1_blueprint3  
app2  
--> app2_blueprint1  
--> app2_blueprint2  
  
Blueprints in Flask are intended for these cases:  
  
* Factor an application into a set of blueprints. This is ideal for larger applications; a project could instantiate an application object, initialize several extensions, and register a collection of blueprints.  
* Register a blueprint on an application at a URL prefix and/or subdomain. Parameters in the URL prefix/subdomain become common view arguments (with defaults) across all view functions in the blueprint.  
* Register a blueprint multiple times on an application with different URL rules.  
* Provide template filters, static files, templates, and other utilities through blueprints. A blueprint does not have to implement applications or view functions.  
* Register a blueprint on an application for any of these cases when initializing a Flask extension.  

[http://flask.pocoo.org/docs/0.12/blueprints/](http://flask.pocoo.org/docs/0.12/blueprints/)

## marshal_with
Tuples given keys with their values -> flask-api-boilerplate/app/auth/resources.py:54  

```python  
>>> from flask_restful import fields, marshal_with
>>> mfields = { 'a': fields.Raw, 'b': fiels.String }
>>> @marshal_with(mfields)
... def get():
...     return { 'a': 100, 'b': 'foo', 'c': 89 }
...
...
>>> get()
OrderedDict([('a', 100),('b', 'foo')])
```