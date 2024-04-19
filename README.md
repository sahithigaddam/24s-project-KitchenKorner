CS3200 Database Design Final Project
Amelia Willmann, Sahithi Gaddam, Nicole Li, Catherina Haast

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## First step-- setting up and starting containers
** Make sure Docker Desktop is installed **
1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 


Welcome to our final project of the semester! Our goal was to create a social media app to share recipes within the Foodie community. 

Our app allows food lovers to share their recipes to others. You can follow your favorite influencers, fitness gurus, friends, and family. You can save your favorite recipes to an unlimited amount of cookbooks



If you want to hear us explain our app and learn more about the development process: view this link.



