# LittleLemon

the Virtual env is set using python3 -m venv venv
so please use this command to run the virtual env - 

<pre>
source venv/bin/activate
</pre>

or create a new virtual envronment using -
<pre>
python3 -m venv venv
source venv/bin/activate
</pre>

Install all the following dependencies - 
<pre>
pip3 install django
pip3 install djangorestframework
pip3 install djangorestframework-xml
pip3 install djoser
pip3 install mysqlclient
</pre>


Please run the following commands to run the program - 
<pre>
python3 manage.py makemigrations

python3 manage.py migrate
   
python3 manage.py runserver 
</pre>

once the website opens you can use it

you can use /api/bookings/ to access booking or restaurant/booking/

also you can use  restaurant/menu/ or restaurant/menu/<Item no> 

To be able to create users, you can create a superuser and then create other users. 
This also allows you to add and delete menu -

<pre>
python3 manage.py createsuperuser   

then go to -> http://127.0.0.1:8000/admin/
</pre>

To be able to access the reservation (MySQL) you can use following commands-
<pre>
Set up MySQL

mysql -u root -p    

and manage the reservations database
</pre>

## User Manual

1. Home Page
![Home page](img/1.png)
2. About
![About](img/2.png)
3. Menu
![Login pane](img/3.png)
* Menu Item Page 
![Login pane](img/4.png)
![Login pane](img/5.png)
4. Book
![Login pane](img/6.png)
* Added functionality to not double book 
![Login pane](img/7.png)
5. Reservations
![Login pane](img/8.png)
6. ADMIN
![Login pane](img/9.png)
* UPDATE MENU
![Login pane](img/10.png)
![Login pane](img/11.png)