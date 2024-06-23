#### Download the zip file of code ###
#### Now install python 3.10 from below command ###
```sudo apt update ```
```sudo apt install python3.10```
<br>
<br>
Extract the code
<br>
Go inside the code directory
<br>
create virtual env by below command
<br>
``virtualenv -p python3 blogenv``
<br>
<br>
activate virtual env from below command
<br>
```source blogenv/bin/activate```
<br>
<br>
Now install requirements by below command
<br>
``pip install -r requirements.txt``
<br>
<br>
Now migrate the models, by below command
<br>
``python manage.py migrate``
<br>
<br>
Now run below command, to run server
<br>
``python manage.py runserver``
<br>
<br>
## Using JWT based token authentication ##
## Signup Api ##

```commandline
curl --location --request POST 'http://127.0.0.1:8000/blogapi/signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "utkarshrastgi9627@lgmllla.collmmm",
    "password": "123456789"
}'
```

## LOGIN API ##
```commandline
curl --location --request POST 'http://127.0.0.1:8000/blogapi/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "utkarshrastogi9627@gmlail.colmm",
    "password": "123456789"
}'
```


## CREATE POST ##
```commandline
curl --location --request POST 'http://127.0.0.1:8000/blogapi/create-post/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MDg3MzM1LCJpYXQiOjE3MTkwODM3MzUsImp0aSI6IjQ5NGUyMmVhMmVlOTRiNjQ4NjNmMTIwODFkNzMzY2UwIiwidXNlcl9pZCI6MX0.GSB_dFwWOVEzVXNoheDHpwgGGHv_ieH5_3KrWS9eDic' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title":"iuiuiui",
    "content": "utka",
    "author": "08989"
}'
```

## UPDATE POST ##
```commandline
curl --location --request PATCH 'http://127.0.0.1:8000/blogapi/update-post/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MDk0MDgwLCJpYXQiOjE3MTkwOTA0ODAsImp0aSI6IjdiNTMyOGFiMjk0MTQ0OTM5YmYyY2UyMmY5ZDhhMzEwIiwidXNlcl9pZCI6MX0.ZBfEKHHa10eIMgNF7OgY5uskvTYmIdo5CgWSeoiqSEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title":"utkarsh",
    "content": "utka",
    "author": "08989"
}'
```

## DELETE POST ##
```commandline
curl --location --request DELETE 'http://127.0.0.1:8000/blogapi/delete-post/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MDA1Njg0LCJpYXQiOjE3MTkwMDIwODQsImp0aSI6ImI1MTdmMDcwYjMyMzQyYjk4NjE5ZGZiNmJhZjU3YjIwIiwidXNlcl9pZCI6Nn0.VULFz8SkAclnQZfUmKWHgGEnr1cMRQWb1zcQKAbZf8s'
```

## CRETAE COMMENT ##
```commandline
curl --location --request POST 'http://127.0.0.1:8000/blogapi/create-comment/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MDg4MzM1LCJpYXQiOjE3MTkwODQ3MzUsImp0aSI6IjQyYzdkNDViY2I0NDQ2ZTg5MGJhNDliYTlhZTgxNzUzIiwidXNlcl9pZCI6NH0.B4XiJ23Hnlq0MYcAm4ajJEwIQRclx4rdmkkXQrXiJLI' \
--header 'Content-Type: application/json' \
--data-raw '{
"author":"jgjllhgjh",
"text": "kjhkkkkkkjkjj"
}'
```

## UPDATE COMMENT ##
```commandline
curl --location --request PATCH 'http://127.0.0.1:8000/blogapi/update-comment/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MDk0MDgwLCJpYXQiOjE3MTkwOTA0ODAsImp0aSI6IjdiNTMyOGFiMjk0MTQ0OTM5YmYyY2UyMmY5ZDhhMzEwIiwidXNlcl9pZCI6MX0.ZBfEKHHa10eIMgNF7OgY5uskvTYmIdo5CgWSeoiqSEY' \
--header 'Content-Type: application/json' \
--data-raw '{
"author":"utkarsh",
"text": "utkars0999hkkkkkkkkkkkkkkkkk"

}'
```

## DELETE COMMENT ##
```commandline
curl --location --request DELETE 'http://127.0.0.1:8000/blogapi/delete-comment/8/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MDA5NDM3LCJpYXQiOjE3MTkwMDU4MzcsImp0aSI6ImMyZjQwMGYxNmViOTQ3NjRiNWVmZjFmZmYzZGY0YzNlIiwidXNlcl9pZCI6N30.5iyjuqCFQvLoqTNbexelE_QXSfFdajt3gR4fqG3Oyf0'
```

## POST LISTING API ##
```commandline
curl --location --request GET 'http://127.0.0.1:8000/blogapi/post-list-with-comment-like-count/?page=1'
```

## POST RETREIVE API ##
```commandline
curl --location --request GET 'http://127.0.0.1:8000/blogapi/single-post-retrieve-with-comment-like-count/1/'
```

## LIKE POST API ##
```commandline
curl --location --request POST 'http://127.0.0.1:8000/blogapi/like-post/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MDg4MzM1LCJpYXQiOjE3MTkwODQ3MzUsImp0aSI6IjQyYzdkNDViY2I0NDQ2ZTg5MGJhNDliYTlhZTgxNzUzIiwidXNlcl9pZCI6NH0.B4XiJ23Hnlq0MYcAm4ajJEwIQRclx4rdmkkXQrXiJLI'
```


