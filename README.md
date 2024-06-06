# E-commerce Website API Scraper

## Overview

This Python script demonstrates a powerful way for scraping data from the API endpoint of an e-commerce **intersport** website. Is particularly useful for fetching product information from the API endpoint of dynamic websites built with JavaScript such as those predominantly using React. I have selected a variety of columns that may be of interest, such as product details and analytics data. This script efficiently saves data to both a JSON file and a MongoDB database.

## Features

- Scrapes product data from an API
- Handles dynamic content and pagination
- Saves data to MongoDB and a JSON file

## Requirements

- Python 3.x
- Requests
- PyMongo

## Setup Instructions

Create a virtual environment:
```
python3 -m venv venv
```
Activate the virtual environment:

On macOS and Linux:
```
source venv/bin/activate
```
On Windows:
```
venv\Scripts\activate
```

## Installation

1. Clone this repository:
```
git clone https://github.com/brankowss/E-commerce-API-Scraper.git
cd web-scraping-project
```

2. Install the required Python libraries using pip:
```
pip install -r requirements.txt
```

## Usage

Run the script:

```
python scrape_api.py
```

## File Structure

- `scrape_api.py`: The Python script for scraping the API and saving data.
- `requirements.txt`: Contains the list of required Python libraries.
- `README.md`: This file.

## Scrape Statistics

- 2024-06-06 21:43:04,826 - INFO - Data scraping completed and saved to MongoDB database
- 2024-06-06 21:43:04,827 - INFO - Total products scraped: 34209
- 2024-06-06 21:43:04,827 - INFO - Total time taken: 1696.32 seconds

## Acknowledgements

This project was inspired by the need for efficient data scraping solutions in the e-commerce industry.

## License

This project is licensed under the [MIT License](LICENSE).





