# SE Project 3 

We're in the home stretch, welcome to the third and final project! The relevant details for the requirements and submission can be found in the course website. 


### Steps to run the project prototype
1. Create a `config.json` file to configure the postgresql database info with username, password, host name and database name.
2. Connect to a postgresql database and run the `db_scripts.sql` to load the data into the database.
3. To use nginx for load balancing install nginx in your system and include the `nginx.conf` file in it.
You can change the server ports as you wish.
4. Finally, to run the application use the command `python app.py <server_port_no>`.