# 🎨 Etsy Bestsellers & Tags Scraper

[![Etsy Bestsellers Scraper](https://apify.com/actor-badge?actor=magic-scraper/etsy-bestsellers-tags-scraper)](https://apify.com/magic-scraper/etsy-bestsellers-tags-scraper)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![Pay-Per-Result](https://img.shields.io/badge/Pricing-$3.00%20%2F%201K%20results-blue?style=flat-square)
![No Cookies Required](https://img.shields.io/badge/Cookies-Not%20Required-success?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20Excel-orange?style=flat-square)

Python examples and API reference for the **[Etsy Bestsellers & Tags Scraper](https://apify.com/magic-scraper/etsy-bestsellers-tags-scraper)** on Apify: Etsy listings with bestseller and star-seller badges, discounts, shop info and Etsy's own keyword tags — as JSON, CSV or Excel.

> ⚡ **No code needed:** 👉 **[Run it in your browser on Apify (free $5 monthly credit)](https://apify.com/magic-scraper/etsy-bestsellers-tags-scraper)**

---

## 🎯 Who is this for?

- **Etsy sellers & POD designers** — collect the keyword tags top listings rank for.
- **Product researchers & dropshippers** — spot what sells through bestseller and star-seller badges.
- **Digital product creators** — filter `isDigitalDownload` to study best-selling templates and printables.
- **Competitor trackers** — monitor prices, discounts and bestseller badges over time.

---

## 📌 Key Facts

| | |
| :--- | :--- |
| **Pricing** | $3.00 per 1,000 listings + $0.00005 start fee (≈1,660 listings/month inside Apify's free $5 credit) |
| **Run time (measured)** | ~11 s for 5 keywords × 20 listings + 3 listing URLs (102 listings with tags) |
| **How it works** | Plain HTTP (no browser) through Apify residential proxy (Etsy uses DataDome); data read from Etsy's own listing-card and tag endpoints |
| **Tags** | Etsy's *Explore related searches* tags from the listing page, ~20–23 per listing — never guessed from the title |
| **Unknown values** | `null` (e.g. `inCartCount`: Etsy does not show the in-cart counter in guest search results) |
| **Login / cookies** | Not required |

---

## 🚀 Quickstart (Python)

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python example.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("magic-scraper/etsy-bestsellers-tags-scraper").call(run_input={
    "searchQueries": ["minimalist wall art", "leather wallet"],
    "maxResultsPerQuery": 20,
    "bestsellersOnly": True,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["isBestseller"], item["title"], item["price"], item["currency"])
    print("  tags:", ", ".join(item["tags"][:5]))
```

Direct listings instead of search:

```python
run_input = {"listingUrls": ["https://www.etsy.com/listing/1391093641"]}
```

---

## 📥 Input

| Parameter | Type | Default | Description |
| :--- | :--- | :---: | :--- |
| `searchQueries` | `array[string]` | `[]` | Keywords to search on Etsy. |
| `listingUrls` | `array[string]` | `[]` | Direct Etsy listing URLs. |
| `maxResultsPerQuery` | `integer` | `30` | Listings per keyword (1–1000). |
| `sortBy` | `string` | `most_relevant` | `most_relevant`, `price_asc`, `price_desc`, `newest`. |
| `countryCode` | `string` | `US` | Market: `US`, `GB`, `CA`, `AU`, `DE`, `FR`. |
| `bestsellersOnly` | `boolean` | `false` | Keep only listings with the Bestseller badge. |
| `onSaleOnly` | `boolean` | `false` | Keep only discounted listings. |
| `freeShippingOnly` | `boolean` | `false` | Keep only free-shipping listings. |
| `proxyConfiguration` | `object` | Apify RESIDENTIAL | Etsy blocks datacenter IPs, so residential proxy in the `countryCode` market is the default; its traffic is included in the price. |

---

## 📤 Output Fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `listingId` | `string` | Etsy listing ID. |
| `title` | `string` | Listing title. |
| `price` | `number` | Current price. |
| `originalPrice` | `number \| null` | Price before discount. |
| `currency` | `string` | Currency code of the `countryCode` market (`USD`, `EUR`, `GBP`, `CAD`, …). |
| `discountPercentage` | `number \| null` | Discount in percent. |
| `isOnSale` | `boolean` | Active discount. |
| `inCartCount` | `string \| null` | In-cart counter if Etsy shows it on the card; almost always `null` in guest search results. |
| `isBestseller` | `boolean` | Bestseller badge. |
| `isStarSeller` | `boolean` | Star Seller badge. |
| `isFreeShipping` | `boolean` | Free shipping. |
| `isDigitalDownload` | `boolean` | Digital download. |
| `isRunningAds` | `boolean` | Sponsored (ad) listing. |
| `rating` | `number \| null` | Shop star rating out of 5, as shown on the card. |
| `reviewsCount` | `integer \| null` | Shop review count as shown on the card (Etsy rounds, e.g. 19.8k → 19800). |
| `shopName` | `string` | Shop name. |
| `shopId` | `string` | Shop ID. |
| `shopUrl` | `string` | Shop URL. |
| `listingUrl` | `string` | Listing URL. |
| `imageUrl` | `string` | Main image URL. |
| `tags` | `array[string]` | Etsy related-search keyword tags. |
| `searchQuery` | `string` | Keyword that found the listing, or `direct_url`. |
| `scrapedAt` | `string` | ISO 8601 timestamp. |

### Sample record (real run, `tags` shortened)

```json
{
  "listingId": "4413275617",
  "title": "18K GOLD Chain Necklace - Thick Big Link Chain Twist Figaro Bead Herringbone Necklace Pearl Waterproof Necklace for Women Men Christmas Gift",
  "price": 29.18,
  "originalPrice": 44.9,
  "currency": "USD",
  "discountPercentage": 35,
  "isOnSale": true,
  "inCartCount": null,
  "isBestseller": true,
  "isStarSeller": true,
  "isFreeShipping": false,
  "isDigitalDownload": false,
  "isRunningAds": true,
  "rating": 4.81,
  "reviewsCount": 19800,
  "shopName": "GoldnBlonde",
  "shopId": "31814650",
  "shopUrl": "https://www.etsy.com/shop/GoldnBlonde",
  "listingUrl": "https://www.etsy.com/listing/4413275617",
  "imageUrl": "https://i.etsystatic.com/31814650/r/il/5ee12f/8760570770/il_255x319.8760570770_3ju8.jpg",
  "tags": ["Most Popular Jewelry", "18k Necklace Chain", "Gold Plated Chain"],
  "searchQuery": "gold necklace",
  "scrapedAt": "2026-10-30T10:58:43.211306+00:00"
}
```

---

## 🔗 Related Scrapers

- [Temu Trending Products & Lightning Deals Tracker](https://apify.com/magic-scraper/temu-trending-products-scraper)
- [TikTok Shop Search Scraper](https://apify.com/magic-scraper/tiktok-shop-search-scraper)
- [eBay Seller Contact Scraper](https://apify.com/magic-scraper/ebay-seller-contact-scraper)

---

## 📄 License

MIT — see [LICENSE](LICENSE). This repository contains usage examples; the scraper itself runs on [Apify](https://apify.com/magic-scraper/etsy-bestsellers-tags-scraper).
