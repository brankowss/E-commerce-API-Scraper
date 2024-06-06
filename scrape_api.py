import requests
import logging
import random
import time
import json
from pymongo import MongoClient
from bson import ObjectId

# Logging info 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Categories and their respective page ranges
categories = {
    "sportovi": 467,
    "muskarci": 214, 
    "zene": 237, 
    "deca": 109,
    "trcanje": 47,
    "intersport_preporucuje-ideja_za_poklon-snizeno-dodatni_popust-vikend_bonus-deal_of_the_day-posebna_ponuda-outlet": 338,
    "outlet": 15,
    "sportovi/novo": 28,
}

# Empty list to collect all products
all_products = []

# Base URL of the API
base_url = "https://www.intersport.rs/api/intersport/shared/Api/fetchCatalog"

# Track start time
start_time = time.time()

# Function to fetch data from API
def fetch_data(category, page_num):
    payload = {
        "path": f"\"{category}?p={page_num}\""
    }
    response = requests.get(base_url, json=payload)
    response.raise_for_status()  
    return response.json()

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['products']  

# Iterate through each category and its pages
for category, max_page in categories.items():
    for page_num in range(1, max_page + 1):
        try:
            # Fetch data from the API
            data = fetch_data(category, page_num)
            products = data.get('products', [])

            # Collect the required fields from each product 
            for product in products:
                product_data = {
                    'name': product.get('name', 'N/A'),
                    'title': product.get('title', 'N/A'),
                    'subTitle': product.get('subTitle', 'N/A'),
                    'urlKey': f"https://www.intersport.rs/{product.get('urlKey', 'N/A')}",
                    'price': product.get('sizes', [{}])[0].get('price', 'N/A'),
                    'reviewCount': product.get('reviewCount', 'N/A'),
                    'googleAnalyticsBrand': product.get('googleAnalyticsBrand', 'N/A')
                }
                
                # Convert ObjectId to string
                if '_id' in product_data:
                    product_data['_id'] = str(product_data['_id'])

                all_products.append(product_data)

            logging.info(f"Fetched data for {category} page {page_num}")

            # Random delay to avoid getting blocked
            time.sleep(random.uniform(0.5, 1.5))

        except requests.RequestException as e:
            logging.error(f"Error fetching data for {category} page {page_num}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error for {category} page {page_num}: {e}")

# Convert documents to JSON-serializable format
serialized_products = [json.loads(json.dumps(product, default=str)) for product in all_products]

# Save the serialized documents to a JSON file
json_filename = 'products.json'
with open(json_filename, 'w') as json_file:
    json.dump(serialized_products, json_file, indent=4, ensure_ascii=False)

# Insert data into MongoDB 
collection = db['products']
collection.insert_many(all_products)

# Track end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Log completion message with scrape stats and time
logging.info(f"Data scraping completed and saved to MongoDB database")
logging.info(f"Total products scraped: {len(all_products)}")
logging.info(f"Total time taken: {total_time:.2f} seconds")
