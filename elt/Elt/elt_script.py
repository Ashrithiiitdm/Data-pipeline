#This script simply transfers data from the source database to the destination database

import subprocess  #I/O control
import time

#We have to wait until the source_db and destination_db are initialised
def wait_for_db(host, max_retires = 5, delay_sec = 5):
    retries = 0
    while retries < max_retires:
        try:
            res = subprocess.run(
                ["pg_isready", "-h", host], check = True, capture_output = True, text = True)
            
            if "accepting connections" in res.stdout:
                print("Successfully connected to Postgres")
                return True
        
        except subprocess.CalledProcessError as e:
            print(f"Error connecting to Postgres:{e}")
            retries += 1
            print(f"Retrying in {delay_sec} seconds... (Attempt {retries}/{max_retires})")
            time.sleep(delay_sec)
    print("Max retries reached. Exitting")
    return False

#If some error continues to persist, exit from the process
if not wait_for_db(host = "source_postgres"):
    exit(1)

#Just in case for debugging
print("Starting ELT script...")

#Source configuration
source_config = {
    'dbname' : 'source_db',
    'user' : 'postgres',
    'password' : 'secret',
    'host' : 'source_postgres'
}

#Destination configuration
dest_config = {
    'dbname' : 'destination_db',
    'user' : 'postgres',
    'password' : 'secret',
    'host' : 'destination_postgres'
}

#Dump command used to back-up the data
dump_command = [
    #Cmd utility to back-up a PostgreSQl database
    'pg_dump',
    #specifies host
    '-h', source_config['host'],
    #specifies user
    '-U', source_config['user'],
    #specifies database
    '-d', source_config['dbname'],
    #specifies the file where the backup will be saved
    '-f', 'data_dump.sql',
    #Disables password prompts
    '-w'
]

#Password being used as an environment variable
subprocess_env = dict(PGPASSWORD = source_config['password'])

#Running the dump command
subprocess.run(dump_command, env = subprocess_env, check = True)

#Commands to load the database to the destination
load_command = [
    'psql',
    '-h', dest_config['host'],
    '-U', dest_config['user'],
    '-d', dest_config['dbname'],
    '-a','-f', 'data_dump.sql'
]

#Again Password as environment variable
subprocess_env = dict(PGPASSWORD = dest_config['password'])

#Running the load command
subprocess.run(load_command, env = subprocess_env, check = True)

#Again print statement just for debugging
print("Ending ELT script...")