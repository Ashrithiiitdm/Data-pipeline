  <h1 align="center">Data-pipeline</h1>
  
## Introduction

This repository contains a custom ELT project that involves utilization of Docker and postgresql alongside with dbt.<br>
Extract - Data from a source database is extracted and is converted into a dump file.<br>
Load - The file is then loaded into a destination database using a Python script.<br>
Transform - The database can be transformed accordingly to our use.<br>

## File structure

1. `source_db_init/init.sql`: This SQL script initializes the source database. In this case, it creates the tables users, films, film_category, actors and film_actors.
2. `elt_script/elt_script.py`: This Python script performs the ELT process. It waits for the source database and then dumps into a SQL file and loads the data into the destination database.
3. `elt_script/Dockerfile`: This file installs the PostgreSQL cilent, sets up the Python environment and copies the elt script and sets it as the default command.
4. `docker-compose.yaml`: This file has the configuration to create and manage multiple containers and has the following services:
  - `source_postgres`: Source database
  - `destination_postgres`: Destination database
  - `elt_script`: The service that runs the python script.

## Setting up
Make sure that you have installed Docker desktop or Docker compose.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ashrithiiitdm/Data-pipeline.git
   cd Data-pipeline/elt
   ```
2. **Running the containers:**

   ```bash
    docker compose up
   ```
3. **After running this you can check the database by:**

   ```bash
   docker exec -it <name_of_destinationdb's_container> psql -U postgres
    ```
