import csv,sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("CREATE TABLE nyc (id INTEGER PRIMARY KEY,listing_url TEXT,name TEXT,host_id INT,\
                    neighbourhood_cleansed TEXT,neighbourhood_group_cleansed TEXT,\
                    city TEXT,zipcode INTEGER, latitude INTEGER,longitude INTEGER, property_type TEXT, room_type TEXT,accommodates INTEGER, \
                    amenities TEXT,price INTEGER, number_of_reviews INTEGER ,first_review date DATE,review_scores_rating INTEGER);")
        csvfile = "listings.csv"
        df = pd.read_csv(csvfile)
        print(df.head())
        df.to_sql("nyc", conn, if_exists='append', index=False)
        conn.commit()
        conn.close()
        print("Data Transfer Complete")



    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection("../db/airbnb-sqlite.db")