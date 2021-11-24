# IMDB API lookup

## Introduction

This repository contains a proof-of-concept for IMDB API lookup application.

## Requirements (tested versions)

1. Linux (Arch)
2. Docker 20.10.10
3. Python3 3.9.7


## Developing and running

1. Initialize environment:

        make initvenv

2. Run locally:

        source ./.venv/bin/activate
        # Set environment variables IMDB_USER_ID and IMDB_API_KEY
        # (check env.example)
        ./imdbapilookup.py "need for speed"

3. Build docker image:
        
        make build

4. Run in docker:
        
        docker run -it \
                -e "IMDB_API_KEY=${IMDB_API_KEY}" \
                -e "IMDB_USER_ID=${IMDB_USER_ID}" \
                imdbapi "Need for speed"

        # or
        make MOVIE="Need for speed" run

5. Run tests:
        
        make inittestenv
        make test
