## FUNCTIONS
## Customer
- Customer can view/search products without login.
- Customer can also add/remove product to cart without login
- When customer try to purchase product, then he/she must login to system.
- After creating account and login to system, he/she can place order.
- There is a payment page also (just for demo,need not fill your card details there , website do not save that details though)
- If customer click on pay button, then their payment will be successful and their order will be placed.
- Customer can check their ordered details by clicking on orders button.
- Customer can see the order status (Pending, Confirmed, Delivered) for each order  
- Customer can Download their order invoice for each order
- Customer can send feedback to admin (without login)
---
### Admin
- First admin will login ( for username/password run following command in cmd )
```
py manage.py createsuperuser
```
- Give username, email, password and your admin account will be created.
- After login, there is a dashboard where admin can see how many customers are registered, how many products are there for sale, how many orders placed.
- Admin can add/delete/view/edit the products.
- Admin can view/edit/delete customer details.
- Admin can view/delete orders.
- Admin can change status of order (order is pending, confirmed, out for delivery, delivered)
- Admin can view the feedbacks sent by customers.
---
### Other Features
- customer places order and admin deleted that user(fraud detection), then their orders will automatically deleted
- If user click on purchase button without having products in their cart, then website will ask to add atleast one product to cart first.



## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf

```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```