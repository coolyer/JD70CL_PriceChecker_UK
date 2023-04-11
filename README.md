# Jack Daniels Price Searcher

This Python script searches multiple online retailers for the price of Jack Daniels 70CL and prints the cheapest price found. It uses the Selenium WebDriver and Beautiful Soup libraries to automate the process of browsing to each retailer's website, searching for the product, and extracting the price.

# Installation
Clone the repository to your local machine or download the ZIP file and extract its contents.
Install the required libraries using pip. Open the terminal and run the following command:
pip install selenium webdriver_manager beautifulsoup4
    Install the latest version of the Chrome browser.

# Usage

    Open the terminal and navigate to the directory containing the script.

    Run the following command:

    python jackdaniels.py

    This will launch the script and start searching for the product on the retailers' websites.

    Wait for the script to complete. It will print the cheapest price found.

# Configuration

You can modify the product variable and sites dictionary in the script to search for a different product or add/remove retailers. Simply change the product name and update the sites dictionary with the name of the retailer and the URL of the product page.



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
# Other Work
<a href="https://github.com/coolyer/JD1L_PriceChecker_UK" target="_blank">JD 1L Price Checker UK</a>

# Please Read!
Note: some retailers may require a captcha to be completed before displaying the price. This script does not automate captcha-solving, so you will need to manually complete the captcha if prompted.

