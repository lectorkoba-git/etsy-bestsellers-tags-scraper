"""
Example: Etsy bestsellers, badges and keyword tags via the Apify Python client.
Requires: pip install apify-client   and   APIFY_TOKEN in the environment.
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "searchQueries": ["minimalist wall art", "leather wallet"],
    "maxResultsPerQuery": 20,
    "bestsellersOnly": True,
    "sortBy": "most_relevant",
    "countryCode": "US",
}

print("Running magic-scraper/etsy-bestsellers-tags-scraper on Apify...")
run = client.actor("magic-scraper/etsy-bestsellers-tags-scraper").call(run_input=run_input)
print(f"Run finished: {run['status']}\n")

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["title"])
    print(f"  Price: {item['price']} {item['currency']} | was: {item.get('originalPrice')} | discount: {item.get('discountPercentage')}%")
    print(f"  Shop:  {item['shopName']} ({item['shopUrl']})")
    print(f"  Badges: bestseller={item['isBestseller']} star_seller={item['isStarSeller']} free_shipping={item['isFreeShipping']}")
    print(f"  Tags:  {', '.join((item.get('tags') or [])[:6])}")
    print(f"  URL:   {item['listingUrl']}\n")
