# Django Sentence Splitter API

![alt text](https://media.tenor.com/AKHj5e7v4pcAAAAi/cute.gif)

Welcome to the Django Sentence Splitter API project. This is a simple RESTful API built on Python Django that provides functionality forallowing you to split sentences on spaces and dashes
as well as splitting the words based on input line length. Adds a new line after every words. Saves the input in a database for later to be recovered.


## Getting Started

```bash
python .\manage.py makemigrations djangoProject
python manage.py migrate  
python manage.py runserver   
```


## Endpoints
POST /format  requires a json object in body with fields: "input" and "lineLength". Input is a sentence to split, line length is a limit of how long a word can be
GET /all returns all previous formats you have done

