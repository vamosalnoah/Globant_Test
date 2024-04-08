USE master;
GO
IF DB_ID('GlobantDB') IS NOT NULL
BEGIN
    ALTER DATABASE GlobantDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE GlobantDB;
END;
GO
CREATE DATABASE GlobantDB;
GO
USE GlobantDB;
GO

CREATE TABLE dbo.locations
(
    City VARCHAR(255) NOT NULL,
    lat INT NOT NULL,
    lng INT NOT NULL,
    CONSTRAINT [pk_locations_city]
        PRIMARY KEY NONCLUSTERED (City)
);
GO

CREATE TABLE dbo.users
(
    user_id BIGINT NOT NULL,
    screen_name VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL,
	followers_count INT NOT NULL,
    friends_count INT NOT NULL,
    statuses_count INT NOT NULL,
    favourites_count INT NOT NULL,
    account_created DATETIME NOT NULL,
    verified BIT NOT NULL,
    City VARCHAR(255) NOT NULL,
    CONSTRAINT [pk_users_screen_name]
        PRIMARY KEY NONCLUSTERED (screen_name),
    CONSTRAINT [fk_locations_city]
        FOREIGN KEY (City) REFERENCES locations (City)
);
GO

CREATE TABLE dbo.languages
(
    lang VARCHAR(2) NOT NULL,
    CONSTRAINT [pk_languages_lang]
        PRIMARY KEY NONCLUSTERED (lang)
);
GO

CREATE TABLE dbo.tweets
(
    user_id BIGINT NOT NULL,
    status_id BIGINT NOT NULL,
    created_at DATE NOT NULL,
    screen_name VARCHAR(50) NOT NULL,
	text TEXT NOT NULL,
	source VARCHAR(255) NOT NULL,
    reply_to_status_id INT NOT NULL,
    reply_to_user_id INT NOT NULL,
    is_retweet BIT NOT NULL,
	favorite_count INT NOT NULL,
    retweet_count INT NOT NULL,
    lang VARCHAR(2) NOT NULL,
	sentiment_value INT NOT NULL,
    sentiment_dictionary VARCHAR(30),
    CONSTRAINT [fk_users_screen_name]
        FOREIGN KEY (screen_name) REFERENCES users (screen_name),
    CONSTRAINT [fk_languages_lang]
        FOREIGN KEY (lang) REFERENCES languages (lang) 
);
GO

