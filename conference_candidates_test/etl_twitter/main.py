
import pyodbc
from db_credentials import server, database
from sql_queries import *

from etl import etl_process

file = 'C:/Users/estoe/Downloads/Twitter Exercise- BI Exercise/Twitter Exercise- BI Exercise/Tweets DataViz Dataset - TweetsDataset.csv'

def main():
    print("ETL Started")
    print('Extracting data')

    try:
        data = etl_process(file)
    except Exception as error:
       print('ETL error, please verify file o directory')

    print("Data extracted and transformed succesfully")

    print('Loading data')
    print('Creating connection')

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Conecction=yes;')
    cursor = cnxn.cursor()

    print('Connection succeed')

    for index, row in data[0].iterrows():
        cursor.execute(insert_users, row.user_id, row.screen_name, row.name, row.description, row.followers_count, row.friends_count, row.statuses_count, row.favourites_count, row.account_created_at, row.verified, row.City )
    cnxn.commit()

    for index, row in data[1].iterrows():
        cursor.execute(insert_languages, row.user_id, row.screen_name, row.name, row.description, row.followers_count, row.friends_count, row.statuses_count, row.favourites_count, row.account_created_at, row.verified, row.City )
    cnxn.commit()

    for index, row in data[2].iterrows():
        cursor.execute(insert_locations, row.user_id, row.screen_name, row.name, row.description, row.followers_count, row.friends_count, row.statuses_count, row.favourites_count, row.account_created_at, row.verified, row.City )
    cnxn.commit()

    for index, row in data[3].iterrows():
        cursor.execute(insert_tweets, row.user_id, row.screen_name, row.name, row.description, row.followers_count, row.friends_count, row.statuses_count, row.favourites_count, row.account_created_at, row.verified, row.City )
    cnxn.commit()
    cursor.close()


    print('Data loaded successfully')



if __name__ == "__main__":
  main()



