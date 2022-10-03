"""
1. Definition and Usage of Django REST

Interface -> RESTful API -> Database

- Toolkit for building WEB APIs
- Defines how other systems can use it
- Defines the allowed requests
- Auth policies -> Packages OAuth1a and Oauth2
- Serialization that supports ORM and non-ORM data source
- Used by many companies
- Unified way to work with the backend

API: Functionalities
REST: Representational state transfer

RESTful API => CRUD by JSON -
GET - ListAPIView,
POST - CreateAPIView, RetrieveAPIView - DetailView,
PUT - UpdateAPIView,
DELETE - DestroyAPIView

- Serializers -
Allow us to convert comp[lex data to native Python data types that can be rendered into JSON/XML,
They provide deserialization, for parsed data to be converted back


2. Requirements and Installation
pip install djangorestframework
pip install markdown
pip install django-filter
Add to INSTALLED_APPS
Add DRF settings to settings.py

3. Creating simple RESTful API
"""
