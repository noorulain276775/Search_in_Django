# Search_in_Django
Implementation of a feature that allows users to search for products based on category and price range, and retrieve the matching products along with their respective details, with authentication using JWT and data stored in a MySQL database.

## Steps to Install MySQL server in your PC in linux
1. $ sudo apt update 
2. $ sudo apt install mysql-server
3. $ sudo systemctl start mysql.service

#### For fresh installations of MySQL, you’ll want to run the DBMS’s included security script. This script changes some of the less secure default options for things like remote root logins and sample users.

4. $ sudo mysql

#### Set the password for root user
5. mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<any-password>'; <br>
6. mysql> exit

#### Then Login again as a root user with the same password

7. $ mysql -u root -p

#### It is not recommended to use the root user for security reasons, so create another user using the root login and work with that.
mysql> CREATE USER 'write-username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'write-password'; <br>
mysql> GRANT CREATE, ALTER, DROP, INSERT, UPDATE, INDEX, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'username'@'localhost' WITH GRANT OPTION; <br>
mysql> FLUSH PRIVILEGES; <br>
mysql> exit <br>
mysql> mysql -u username -p <br>


## Installing MySQL workbench to view and work with your database easily

1. $ sudo snap install mysql-workbench-community

##### Run this command so that the workbench can store the passwords

2. $ sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service


## MySQL Client in Django
1. $ pip install ez_setup
2. $ sudo apt-get install python3-dev libmysqlclient-dev
3. $ pip3 install mysqlclient
