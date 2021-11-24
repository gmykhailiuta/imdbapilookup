#!/usr/bin/env python3
import requests
import os
import sys
import argparse
from pprint import pprint

user_id = os.getenv('OMDB_USER_ID')
api_key = os.getenv('OMDB_API_KEY')
url = "http://www.omdbapi.com/"


def lookup(movie_name: str, verbose: bool = False):
    params = {
        "i": user_id,
        "apikey": api_key,
        "t": movie_name
    }
    response_raw = requests.get(url, params=params)
    if response_raw.status_code != 200:
        print("OMDB API returned code {}".format(response_raw.status_code))
        sys.exit(1)
    response = response_raw.json()

    if verbose:
        pprint(response)
    if "Ratings" not in response:
        print("There's no ratings for such movie or movie not found")
        sys.exit(1)
    ratings = response['Ratings']

    rt_rating_raw = next((x for x in ratings if x["Source"] == "Rotten Tomatoes"), None)

    if rt_rating_raw:
        rt_rating = int(rt_rating_raw['Value'][:-1])
        if rt_rating < 50:
            print("Rotten Tomatoes rating for the movie {n} is {r}%. Perhaps, it's not worth the time".format(n=movie_name, r=rt_rating))
        elif rt_rating >=50 and rt_rating < 70:
            print("Rotten Tomatoes rating for the movie {n} is {r}%. Perhaps, it's not worth the time".format(n=movie_name, r=rt_rating))
        else:
            print("Rotten Tomatoes rating for the movie {n} is {r}%. Good choice!".format(n=movie_name, r=rt_rating))
    else:
        print("There's no Rotten Tomatoes rating for this movie, but there're next ones instead:")
        for r in ratings:
            print("{} - {}".format(r["Source"],r['Value']))

def main():
    if not (user_id and api_key):
        print("Please, set both OMDB_USER_ID and OMDB_API_KEY environment variables")
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("movie", type=str, action="store",
                        help="Movie name to lookup ratings for")
    parser.add_argument("-v", "--verbose", action="store_true",
                        dest="verbose", default=False,
                        help="Print full response from server")
    args = parser.parse_args()

    if args.movie:
        lookup(args.movie, args.verbose)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()