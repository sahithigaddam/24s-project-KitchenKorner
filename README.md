## CS3200 Database Design Final Project
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

# KitchenKorner
This repository contains the KitchenKorner app, designed to be a social media app dedicated to sharing recipes online. This database stores data on recipes, ingredients, users, etc.; a backend flask application; and a local Appsmith server for the frontend usage of the flask APIs.

## Overview 
The purpose of KitchenKorner is to provide a platform specifically for those interested in sharing and finding new recipes. This app is designed to be usable for all levels of users, whether you're a professional chef or just a college student cooking for the first time, KitchenKorner is meant for all. Whether you want to share your recipes with others or find new favorites to save forever, KitchenKorner is the place to do it. Our app allows food lovers to share their recipes to others. You can follow your favorite influencers, fitness gurus, friends, and family and stay up to date with all the hot food trends.

## System Components
MySQL Database: Stores and manages all KitchenKorner data, including; users, recipes, ingredients, cookbooks, comments, ratings, feed, etc.<br>
Flask REST API: Enabling data operations via HTTP requests, acts as the fundamental framework for facilitating interactions between our frontend and AppSmith.<br>
AppSmith Server: The application of the HTTP request on a visual interface, representative of how the app would look like for the user.

## System Architecture
The MySQL database is built from 18 tables<br>
Users: Contains user information, such as; User_ID, Username, Email, Full_Name, and Created_At.<br>
Follows: Stores who a user follows.<br>
Posts: Stores posts made by users.<br>
Recipes: Stores the recipes that are created/posted by users.<br>
Ingredients: Stores all the possible ingredients a recipe could use.<br>
Ingredient_Details: Bridge table that connects what ingredients are used in each recipe and vice versa.<br>
Feed: Stores each user's unique feed, which contains the posts of other users they follow.<br>
Cookbook: Stores the groups of recipes that are saved by each user.<br>
Recipe_Cookbook: Bridge table that connects what recipes are in each cookbook and vice versa.<br>
Comments: Stores all the comments made by users under a post.<br>
Ratings: Stores all the different ratings (Actual_Time, Actual_Difficulty, Taste) made by users on each post.<br>
Tags: Stores which users were tagged on each post.<br>
Direct_Messages: Stores what posts users send each other and the time stamp.<br>
External_Messages: Stores what posts are being externally sent by users.<br>
Filters: Stores the keywords within each subject (Cuisine, Meal_Type, Ingredients) which can be used to filter searches for recipes.


Authors - SnacAttac<br>
Amelia Willmann - @ameliawillmann<br>
Nicole Li - @nicoleli26<br>
Sahithi Gaddam - @sahithigaddam<br>
Catherina Haast - @caphaast<br>


Video Demo<br>
[Video Demo Link<br>](https://drive.google.com/file/d/1v_4kdGJlFoV9G2ixiJED7PYkNi2LhZOw/view) 


