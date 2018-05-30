# Setup
```sh
virtualenv env  
. env/bin/activate  
pip install -r requirements.txt  
sudo apt-get install sqlitebrowser  
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