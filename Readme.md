# BBC News Scraper

This repository contains a scraper for BBC News. It uses the Scrapy framework to scrape sections and the latest articles from the website.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- pip

### Installing

#### 1. Clone the repository

#### 2. Install Python virtual environment

- pip install virtualenv

#### 3. Create a new virtual environment

- On Linux: `python3 -m venv env`
- On Windows: `py -3 -m venv env`
- On Mac: `python3 -m venv env`

#### 4. Activate the virtual environment

- On Linux and Mac: `source env/bin/activate`
- On Windows: `env\Scripts\activate`

#### 5. Install Scrapy

- pip install scrapy

#### 6. Change to the project directory

- cd news

#### 7. Run the spider

- scrapy crawl newsspider

