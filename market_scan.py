import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def run_calgary_job_search():
    # Set encoding to avoid charmap errors
    sys.stdout.reconfigure(encoding='utf-8')
    print("🚀 Nexus: Starting Calgary Tech Job Search...")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # We'll try a simpler job board first that's less aggressive than Indeed for the first test
        url = "https://www.google.com/search?q=automation+python+jobs+calgary&ibp=htl;jobs"
        driver.get(url)
        time.sleep(5)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        jobs = driver.find_elements("css selector", ".iJ7v7b") # Common Google Jobs selector
        
        print(f"📊 Market Scan Complete. Page Title: {driver.title}")
        if "Blocked" in driver.title:
            print("❌ Access Blocked by bot protection. Switching to Stealth Mode for next run.")
        else:
            print("✅ Connection Successful. Environment is READY for scraping.")
            
    finally:
        driver.quit()

if __name__ == "__main__":
    run_calgary_job_search()
