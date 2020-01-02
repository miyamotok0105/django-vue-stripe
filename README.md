
# [WIP] Simple payment system

This sample is simple payment system.    


- frontend    
vue.js    

- backend    
django restframework    

- middleware    
stripe    

- infra    
Choose what you like.    


# TODO



# Architecture

Dependency flow.    
repositories -> entities -> service -> views.py


```
├── backend
│   └── app
│       └── catalog
│           ├── domain
│           │   ├── entities
│           │   │   └── [Innermost Domain Layer.]
│           │   ├── repositories
│           │   │   └── [Infra Repository Layer.]
│           │   └── service
│           │       └── [Domain Service Layer.]
│           └── migrations
│           └── views.py []
└── frontend
    ├── config
    ├── src
    │   ├── assets
    │   ├── components
    │   └── router
    └── static
```


This post is very good to study for me. But i don't adopt the architecture this time, because very large architecture. Consider at the next opportunity    

[Clean Architecture in Django](https://engineering.21buttons.com/clean-architecture-in-django-d326a4ab86a9)

# MEMO


```
cd backend/app/
python ../../manage.py startapp catalog

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

npm install -g vue-cli
vue init webpack frontend
npm run dev
```

Check RFC 7519 about jwt.


# Reference

[Stripe Elements for the web](https://stripe.com/docs/stripe-js)

[Accept a payment](https://stripe.com/docs/payments/accept-a-payment-charges#python)

[Vue.js で最新のアプリケーションを構築する](https://auth0.com/blog/jp-building-modern-applications-with-django-and-vuejs/#Auth0-API----------------)

[flask-vue-stripe](https://github.com/testdrivenio/flask-vue-stripe)

[Free ecommerce template for Vue.js projects](https://vuejsexamples.com/responsive-ecommerce-template-built-with-vue-js/)

- Django Sample    

[pachatary-api](https://github.com/jordifierro/pachatary-api)
[django-vue.js](https://github.com/auth0-blog/django-vue.js)

