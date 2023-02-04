# agileLogin

## Env 
python -m venv agl
.\agl\Scripts\activate

## install libraries
pip install flask
pip install flask-mysqldb

## set flask
set FLASK_APP=main.py
set FLASK_DEBUG=1
flask --app main run
flask --app main --debug run 

## Create DataBase
CREATE DATABASE IF NOT EXISTS `pythonlogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `pythonlogin`;

CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (1, 'test', 'test', 'test@test.com');

## Requeriments
pip3 freeze > requirements.txt