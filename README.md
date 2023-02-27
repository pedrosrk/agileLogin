# agileWebSite

## Env 
- python -m venv agl 
- .\agl\Scripts\activate

## install libraries
- pip install flask
- pip install flask-mysqldb
- pip install -r requirements.txt

## set flask
- set FLASK_APP=main.py
- set FLASK_DEBUG=1
- flask --app main run
- flask --app main --debug run 

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

CREATE TABLE `pythonlogin`.`iterations` (
  `id` INT NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `msg` VARCHAR(1255) NOT NULL,
  `score` VARCHAR(100) NOT NULL,
  `agree` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

## Requeriments
pip freeze > requirements.txt

## Deploy AWS
- rm -rf agileWebSite/
- pm2 save
- git clone ... cd agileWebSite/
- pm2 start main.py --interpreter python3 --watch --name agilim
- pm2 save


## CSS
* {
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "segoe ui", roboto, oxygen, ubuntu, cantarell, "fira sans", "droid sans", "helvetica neue", Arial, sans-serif;
    font-size: 16px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
body {
    background-color: #435165;
    margin: 0;
}
.login, .register {
    width: 400px;
    background-color: #ffffff;
    box-shadow: 0 0 9px 0 rgba(0, 0, 0, 0.3);
    margin: 100px auto;
}
.login h1, .register h1 {
    text-align: center;
    color: #5b6574;
    font-size: 24px;
    padding: 20px 0 20px 0;
    border-bottom: 1px solid #dee0e4;
}
.login .links, .register .links {
    display: flex;
    padding: 0 15px;
}
.login .links a, .register .links a {
    color: #adb2ba;
    text-decoration: none;
    display: inline-flex;
    padding: 0 10px 10px 10px;
    font-weight: bold;
}
.login .links a:hover, .register .links a:hover {
    color: #9da3ac;
}
.login .links a.active, .register .links a.active {
    border-bottom: 3px solid #2a6e62;
    color: #2a6e62;
}
.login form, .register form {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding-top: 20px;
}
.login form label, .register form label {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 50px;
    background-color: #2a6e62;
    color: #ffffff;
}
.login form input[type="password"], .login form input[type="text"], .login form input[type="email"], .register form input[type="password"], .register form input[type="text"], .register form input[type="email"] {
    width: 310px;
    height: 50px;
    border: 1px solid #dee0e4;
    margin-bottom: 20px;
    padding: 0 15px;
}
.login form input[type="submit"], .register form input[type="submit"] {
    width: 100%;
    padding: 15px;
    margin-top: 20px;
    background-color: #2a6e62;
    border: 0;
    cursor: pointer;
    font-weight: bold;
    color: #ffffff;
    transition: background-color 0.2s;
}
.login form input[type="submit"]:hover, .register form input[type="submit"]:hover {
    background-color: #2a6e62;
    transition: background-color 0.2s;
}
.navtop {
    background-color: #2f3947;
    height: 60px;
    width: 100%;
    border: 0;
}
.navtop div {
    display: flex;
    margin: 0 auto;
    width: 1000px;
    height: 100%;
}
.navtop div h1, .navtop div a {
    display: inline-flex;
    align-items: center;
}
.navtop div h1 {
    flex: 1;
    font-size: 24px;
    padding: 0;
   margin: 0;
    color: #eaebed;
    font-weight: normal;
}
.navtop div a {
    padding: 0 20px;
    text-decoration: none;
    color: #c1c4c8;
    font-weight: bold;
}
.navtop div a i {
    padding: 2px 8px 0 0;
}
.navtop div a:hover {
    color: #eaebed;
}
body.loggedin {
    background-color: #f3f4f7;
}
.content {
    width: 1000px;
    margin: 0 auto;
}
.content h2 {
    margin: 0;
    padding: 25px 0;
    font-size: 22px;
    border-bottom: 1px solid #e0e0e3;
    color: #4a536e;
}
.content > p, .content > div {
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.1);
    margin: 25px 0;
    padding: 25px;
  background-color: #fff;
}
.content > p table td, .content > div table td {
  padding: 5px;
}
.content > p table td:first-child, .content > div table td:first-child {
  font-weight: bold;
  color: #4a536e;
  padding-right: 15px;
}
.content > div p {
  padding: 5px;
  margin: 0 0 10px 0;
}