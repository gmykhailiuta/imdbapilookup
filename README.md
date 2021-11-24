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
        # Set environment variables OMDB_USER_ID and OMDB_API_KEY
        # (check env.example)
        ./imdbapilookup.py "need for speed"

3. Build docker image:
        
        make build

4. Run in docker:
        
        docker run -it \
                -e "OMDB_API_KEY=${OMDB_API_KEY}" \
                -e "OMDB_USER_ID=${OMDB_USER_ID}" \
                imdbapi "Need for speed"

        # or
        make MOVIE="Need for speed" run

5. Run tests:
        
        make inittestenv
        make test
