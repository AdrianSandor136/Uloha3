# Python App for Parsing and Storing Interface Data

This application parses data from a JSON file and stores it in a PostgreSQL database. It is dockerized for easy deployment.

## Table of Contents
- [Requirements](##requirements)
- [Installation](##installation)
- [Usage](##Usage)
  

## Requirements

1. Docker
2. Docker-Compose
3. PostgreSQL



## Installation

To install and run this application, follow these steps:

1. Change the pasword in config.py file for the one provided in email.

2. Run the docker-compose command:docker-compose up



## Usage

Once the Docker containers are up and running:

- The application will create a new table in your PostgreSQL database, if it does not exist.
- It will parse the data from config.json.
- The parsed data will then be stored into the database.


