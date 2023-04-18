# Stargazr Code Challenge - Spring 2023

Welcome to the Stargazr Code Challenge for spring 2023!

## Introduction

This is a coding challenge for [tech positions](https://stargazr.ai/company#careers) at Stargazr. You can check past editions of the challenge at [challenge.stargazr.ai](https://challenge.stargazr.ai).

This project contains the back and front end of a simple Flask + Vue3 application, similar to what we use at Stargazr. Your task is to implement three simple features, zip it (don't forget to remove `.git` and `node_modules` folders to make it smaller) and send it to us at [careers@stargazr.ai](mailto:careers@stargazr.ai).

To run it:
* Install Python 3 and Node.js (we tested it with Python 3.9.1, Node v16.18.1 and npm 8.19.2)
* Install the back dependencies with `pip3 install -r requirements.txt` (or pip if you are using Windows)
* Install the front dependencies with `npm install`
* Run the back with `python3 server.py` (or python if you are using Windows), it will be available at [http://localhost:20230](http://localhost:20230)
* Run the front with `npm run dev`, it will be available at [http://localhost:2023](http://localhost:2023).
* No need to install any database, the whole thing runs with a CSV table.