# Project - Extract, Transform and Load

Goal: To extract and transform FIFA 2022 World Cup Data and load structured data into PostGreSQL and MongoDB

Team Members: Anand Shankar and Conrad Urffer

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
