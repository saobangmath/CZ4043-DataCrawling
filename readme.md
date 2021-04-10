# Trip Advisor crawler

This is a simple crawler script for Trip Advisor made for CZ4034 2021 S2. 

### Usage format:

### 1) Input new restaurant link into the restraurantlist.csv from tripadvisor in this format: 
https://www.tripadvisor.com.sg/Restaurant_Review-g294265-d13913142-Reviews-Winestone-Singapore.html

### 2) Setup Docker 
You can follow this link to setup docker on your machine: 
https://docs.docker.com/compose/gettingstarted/

### 2) Docker Build 
The Dockerfile is already provided in the project. Before running, we need to build the docker file first. To build the dockerfile, use the command below: 

Overview of Dockerfile: 
- Install Google Chrome
- Install Chrome Web driver
- Set to display port to avoid crash 
- Install selenium 
- Install data science libraries 
- Set working directory 

docker build tadvcrawler .

### 3) Docker Run
To run the python crawling sript, run the following command below: 

docker run -it tadvcrawlertwo tripadvcrawler.py 

## optional arguments:

  -h, --help            show help message and exit

  -f, --force           Force download even if already successfully downloaded

  -a {Hotel,Restaurant}, --activity {Hotel,Restaurant}
                        Type of activity to crawl (default: Hotel)

  -r MAXRETRIES, --maxretries MAXRETRIES
                        Max retries to download a file. Default: 3

  -t TIMEOUT, --timeout TIMEOUT
                        Timeout in seconds for http connections. Default: 180

  -p PAUSE, --pause PAUSE
                        Seconds to wait between http requests. Default: 0.2

  -m MAXREVIEWS, --maxreviews MAXREVIEWS
                        Maximum number of reviews per item to download.
                        Default:unlimited
