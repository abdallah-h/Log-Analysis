# Log Analysis
## Introduction
Building an informative summary from logs by sql database queries. Interacting with a live database both from the command line and from the python code. This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

## What are we reporting
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## System setup
1. Download Vagrant and install.
2. Download Virtual Box and install.
3. Clone this repository.
4. Download the [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and logAnalysis.py files from the respository and move them to your vagrant directory within your VM.

## how to run the program
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python logAnalysis.py``` to run the reporting program.
