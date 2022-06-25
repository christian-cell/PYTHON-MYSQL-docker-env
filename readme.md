basic docker environment to connect python application to mysql db

Prerequisites install python 3.8 or later

intall conectors to mysql

$ pip3 install mysql-connector-python

$ pip3 freeze | grep mysql-connector-python >> requirements.txt

create docker volumes an docker network to isolate

$ docker volume create mysql

$ docker volume create mysql_config

$ docker network create mysqlnet

Connect to mysql and make an insert

$ curl http://localhost:8000/initdb

$ curl http://localhost:8000/widgets

Check in phpmyadmin in localhost:8087 if inventory is created and insert is completed .