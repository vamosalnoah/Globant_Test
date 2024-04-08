#import modules
import pandas as pd
from datetime import datetime


def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def get_users(dataframe):
    users = dataframe.copy()
    users.drop(['status_id', 'created_at', 'text', 'source', 'reply_to_status_id', 'reply_to_user_id', 'is_retweet', 'favorite_count', 'retweet_count',	'lang', 'sentiment_value', 'sentiment_dictionary', 'lat', 'lng'], axis=1, inplace=True)
    users['account_created_at'] = datetime.strptime(users['account_created_at'], '%d/%m/%y %H:%M:%S')
    users.drop_duplicates(subset='screen_name', inplace=True, ignore_index=True)
    return users

def get_languages(dataframe):
    languages = dataframe.copy()
    languages = languages['lang']
    languages.drop_duplicates(inplace=True, ignore_index=True)
    return languages

def get_locations(dataframe):
    locations = dataframe.copy()
    locations = locations[['lat', 'lng', 'City']]
    locations.drop_duplicates(subset='City' ,inplace=True, ignore_index=True)
    return locations

def get_tweets(dataframe):
    tweets = dataframe.copy()
    tweets.drop(['name', 'description', 'followers_count', 'friends_count', 'statuses_count', 'favourites_count', 'account_created_at', 'verified', 'lat', 'lng', 'City'], axis=1, inplace=True)
    return tweets

def etl_process(route):

    df = extract_from_csv(route)
    users = get_users(df)
    languages = get_languages(df)
    locations = get_locations(df)
    tweets = get_tweets(df)

    dfs = []

    dfs.append(users)
    dfs.append(languages)
    dfs.append(locations)
    dfs.append(tweets)

    return dfs

