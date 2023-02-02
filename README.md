# Methods - EzShop

## Description
Shopping list prediction using KNN algorithm to get the next shopping list for a costumer.

#### We will provide a system to predict the next shopping cart for a user using past shopping carts, the system will include:
* Authentication and authorization.
* adding a new cart.
* Registration, Login, Logout, Sessions..
* Adding the predicted cart the the shopping lists.
* passwords are encricpted with Bcrypt.
* Can edit the predicted cart.

## Flow
1.  Login or registration.
    After registration you will be asked to log in.
2.  The Dashbaord will show the last shopping list and the predicted list:
    * Last shopping list: 
      - for looks, cannot edit or add again
    * predicted cart:
      - can add to cart
      - can edit then add to cart
    * adding a new cart:

## FYIs:
* the Azure Webservice we use can be slow
  - clicks work, if it looks like its not, then it just takes time (30 seconds max from our testing but allways works)
  - the first time the site is accessed it will re-build it so the first access will take upto 10 minutes.
  - if there are issues if the on-air server please conntact us so we can look at the issues with azure that are not part of our code

## Prerequisites
```bash
  Flask
```
## Run with Azure
```bash
  type in url browser: https://ezshop-methods.azurewebsites.net
```
## Local run - **not recommended**
```bash
git clone https://github.com/Iam-Shenkar/iamAssignment3.git
```
### Install
```each module
  from the requirement.txt
  build a MySQL server with a table called users
    - id - PK, AI, UQ - INT
    - username - UQ, - VARCAHR(50)
    - Password - VARCHAR(150)
    - email - UQ - VARCHAR(45)
  create an .env file
  enter in it the correct MySQL server Detail in the variables:
    - MYSQL_DATABASE_USER
    - MYSQL_DATABASE_PASSWORD
    - MYSQL_DATABASE_DB
    - MYSQL_DATABASE_HOST
```
### Start server
```bash
py flask run
```
or
```bash
py app.py
```

### Start client
```bash
type in url borwser: http://localhost:5000 
```
### Other dependancies

## Built with
* Flask
* Azure
* MySQLFreeHosting.net
* HTML
* CSS
* javascript
* Pandas
* Numpy

## Credits
* Gilad Meir :guitar:
* Shahar Ariel :tomato:

## Lecturers
* Michal Chalamish
* Yonatan Alfasi 
