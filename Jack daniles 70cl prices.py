from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from bs4 import BeautifulSoup
import requests
import time
# set up the Chrome driver and options
# Headless must be set to false as website detect the browser as a bot.
options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# define the product so you rememeber
product = "Jack Daniels 70CL"
sites = {
    "Tesco": "https://www.tesco.com/groceries/en-GB/products/255248604",
    "B&M": "https://www.bmstores.co.uk/products/jack-daniels-whiskey-70cl-331944",
    "Asda": "https://groceries.asda.com/product/american-whiskey/jack-daniels-tennessee-whiskey/18900",
    "Sainsbury's": "https://www.sainsburys.co.uk/gol-ui/product/jack-daniels-70cl",
    "Coop": "https://www.coop.co.uk/products/jack-daniels-tennessee-whiskey-28357",
    "Prem": "https://premier-stores-crieff.co.uk/products/jack-daniels-pm2199",
    "BarginBooze": "https://www.bargainbooze.co.uk/product/jack-daniels-70cl-pm-21-99/",
    "Morrisons": "https://groceries.morrisons.com/products/jack-daniel-s-tennessee-whiskey-119493011",
}



# search each site for the product and extract the price
print("Jack daniels price searcher")
tescoprice = None
asdaprice = None
sainsprice = None
bmprice = None
coopprice = None
premprice = None
morrisonprice = None
bbprice = None
for site, url in sites.items():
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    try:
        if site == "Tesco":
            # wait for the price element to become visible
            price_elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".value")))
            # extract the price value from the element's text content
            price = "£" + price_elem.text.strip()
            tescoprice = "£" + price_elem.text.strip()
            
        elif site == "Aldi":
            price_elem = driver.find_element_by_css_selector("div.pricing")
            
        elif site == "B&M":
            price_elem = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[itemprop='price']")))
            price = "£",price_elem.get_attribute('content')
            bmprice = "£",price_elem.get_attribute('content')
        
        elif site == "Prem":
            price_elem = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[itemprop='price']")))
            price = "£",price_elem.get_attribute('content')
            premprice = "£",price_elem.get_attribute('content')
            
        elif site == "Sainsbury's":
            price_elem = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".pd__cost__retail-price")))
            # extract the price value from the element's text content
            price = price_elem.text.strip()
            sainsprice = price_elem.text.strip()
            
        elif site == "Asda":
            # wait for the price element to become visible
            price_elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "strong.co-product__price")))
            # extract the price value from the element's text content
            price_text = price_elem.text.strip()
            # remove the "now" label from the price text using regular expressions
            price = re.sub(r'\bnow\b', '', price_text).strip()
            asdaprice = re.sub(r'\bnow\b', '', price_text).strip()
         
        elif site == "Coop":
            price_elem = price_elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".coop-c-card__price")))
            price = price_elem.text.strip()
            coopprice = price_elem.text.strip()
        
        elif site == "BarginBooze":
            price_elem = price_elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-singleproduct .txt--current-price")))
            price = price_elem.text.strip()
            bbprice = price_elem.text.strip()
            
        elif site == "Morrisons":
            price_elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bop-price__current")))
            price = price_elem.text.strip()
            morrisonprice = price_elem.text.strip()
        
        
        else:
            price_elem = None
        if price_elem:
            price = price_elem.text
            print(site + ": " + price)
        else:
            price = "Price not found"
            print(site + ": " + price)
    except:
        print(site + ": Error scraping price")

# print the cheapest price found
if tescoprice is not None and asdaprice is not None and sainsprice is not None and bmprice is not None and premprice is not None and bbprice is not None and morrisonprice is not None:
    # convert prices to float if they are in the correct format
    prices = {}
    for site, price in [("Tesco", tescoprice), ("Asda", asdaprice), ("Sainsbury's", sainsprice), ("B&M", bmprice), ("Coop", coopprice), ("Prem", premprice), ("BarginBooze", bbprice), ("Morrisons", morrisonprice)]:
        if isinstance(price, str) and price.startswith("£"):
            try:
                prices[site] = float(price[1:])
            except ValueError:
                print(f"Error converting price for {site}")
        else:
            prices[site] = None
    # find the cheapest price
    valid_prices = {site: price for site, price in prices.items() if price is not None}
    if len(valid_prices) > 0:
        cheapest_price = min(valid_prices.values())
        cheapest_sites = [site for site, price in valid_prices.items() if price == cheapest_price]
        if len(cheapest_sites) == 1:
            cheapest_site = cheapest_sites[0]
            cheapest_price_str = "£{:.2f}".format(cheapest_price)
            print(f"The cheapest price for {product} is found at {cheapest_site} for {cheapest_price_str}")
        else:
            cheapest_sites_str = ", ".join(cheapest_sites)
            cheapest_price_str = "£{:.2f}".format(cheapest_price)
            print(f"The cheapest price for {product} is found at {len(cheapest_sites)} sites: {cheapest_sites_str} for {cheapest_price_str}")
    else:
        print("Error: Could not find valid prices on one or more sites.")
else:
    print("Error: Could not find prices on one or more sites.")
driver.quit()
