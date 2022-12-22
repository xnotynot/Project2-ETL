# Project - Extract, Transform and Load

Goal: To extract and transform FIFA 2022 World Cup Data and load structured data into PostGreSQL and MongoDB

Team Members: Anand Shankar and Conrad Urffer
[Link to the Juypter Notebook](https://github.com/xnotynot/Project2-ETL/blob/main/FIFA_2022_ETL.ipynb)

## Data Cleanup and Analysis Requirements
* Data Sources
    - [FIFA World Cup 2022 Statistics](https://www.kaggle.com/datasets/swaptr/fifa-world-cup-2022-statistics)
    - [FIFA World Cup 2022 Players](https://www.kaggle.com/datasets/swaptr/fifa-world-cup-2022-player-data)
    - [FIFA World Cup 2022 Match](https://www.kaggle.com/datasets/swaptr/fifa-world-cup-2022-match-data)
    - [Wikipedia - Stadium data](https://en.wikipedia.org/wiki/2022_FIFA_World_Cup#Venues)
    - [OpenWeather API](https://openweathermap.org/history)
 
* EXTRACT - Extracting the data from those sources.
    - Group Statistics (CSV)
    - Team Data (CSV)
    - Match Data (CSV)
    - Stadium / Venue Data (Web Scraping with Pandas from wikipedia)
    - Weather info at the statium for the respective match dates
 
* TRANSFORM - Transformation - (Cleanse, joining, filter, and aggregate)
 - Teams Data
    - Imported CSV data
    - Create sub-frame for subset of columns
    - Set proper datatypes
  - Player Data
    - Read CSV
    - Create a sub-frame
    - Rename and transform age by splitting string of a dataframe column
    - Filter records by performance number
    - Set proper datatypes
  - Match Data
    - Read CSV
    - Create a sub-frame
    - Rename and transform - convert from string data type to datetime
    - Use the weather api to get the weather info at the venues for match data
    - Set proper datatypes
  - Stadium / Venue Data
    - Call Wikipedia site for FIFA 2022 world cup page to scrape data using Pandas
    - Select the table with stadium / venue data
    - Set proper data types
    
* LOAD - Loading the data into a database
    - Load the data into PostGreSql (Teams, Match, Players)
    - Load the stadium data into MongoDB

## Snapshot of MongoDB

![Mongo DB Collection to Store Stadium Info](https://github.com/xnotynot/Project2-ETL/blob/main/screenshots/mongo_stadium_list.png)

## Snapshot of Postgre SQL Tables

* Match Table
![Match Table](https://github.com/xnotynot/Project2-ETL/blob/main/screenshots/match_table_postgresql.png)

* Teams Table
![Teams Table](https://github.com/xnotynot/Project2-ETL/blob/main/screenshots/teams_table_postgresql.png)

* Players Table
![Players Table](https://github.com/xnotynot/Project2-ETL/blob/main/screenshots/player_table_postgresql.png)

# Improvements
* Automation of Data loads
    - We could automate the extraction and load into SQL / Mongo DB by converting the static statements into dynamic function calls
    - The automation can be made possible by making the table name and field names as parameters in a python function which can also accept the database type (PostgreSQL / Oracle / MSSQL / Snowflake) and dynamically create an instance of the database engine from SQL Alchemy and perform further functions
    - It could also drop any existing tables in the schema and "CREATE" the table dynically based on the dataframe and append rows to it

* Error handling and notification
    - It would be nice for the data load program to be scheduled as a windows task and log any errors during the data load and send an email at the end of process with a brief statistics of the data load operation
    - The load program can also have conditional logic to determine the criticality of the errors and have some rudimentary decision making to decide whether to continue data loads after error or abort the process

