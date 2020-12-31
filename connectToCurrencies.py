import requests
from bs4 import BeautifulSoup


class currencyScraper():
    """ This class focuses on scraping coindesk.com and creating different
    attributes and methods for the coins based on that."""
            
    def __init__(self, coin):
        # Define the self functions. 
        self.coin = coin
        self.url = f"https://www.coindesk.com/price/{coin}"
        
        self.webpage = requests.get(self.url)

        self.soup = BeautifulSoup(self.webpage.content, "html.parser")
        
        # Get coin price
        first_results = str(self.soup.find_all("div", class_="price-large"))  

        second_results = first_results.split("span>") 

        third_results = str(second_results[-1]).split("</div>")
        
        self.price = float(third_results[0].replace(",", ""))

    
    def __str__(self): 
        """When user prints(coin), return this"""
        return f"\nCoin: {self.coin} | Price: {self.price} | URL: {self.url}\n"
    
    def getName(self): 
        """Just get the name of the coin you're using"""
        return f"{self.coin}"

    def getPrice(self):
        """Get the current price of the chosen coin"""
        return f"{self.coin} price: {self.price}"
    
    def getURL(self): 
        """Get the URL to gain more complete info"""
        return self.url

    def getInfo(self): 
        """Get a paragraph with coin information. 
        Doesn't work that well becuase not every coin has an explanation 
        and if they do, they're structured very differently in HTML"""
        first_results = str(self.soup.find_all("div", class_="coin-about-text"))

        self.info = str(first_results).strip()
        
        return self.info
    
    def set_min_and_max(self): 
        """Set the max and the min for the coin"""
        self.max = float(input(f"Max price for {self.getName()} => "))
        self.min = float(input(f"Min price for {self.getName()} => ")) 
        # Check if max and min are in the correct intervals. 
        if self.max < self.price and self.min > self.price: 
            return "ERROR: Max less than current price or min more than current price"
        # If it is set max price and min price and return the values set.  
        elif self.max > self.price and self.min < self.price: 
            return f"Max price: {self.max} | Min price: {self.min}" 


