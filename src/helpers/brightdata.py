from selenium.webdriver import Remote, ChromeOptions  
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection  
from decouple import config
# Enter your credentials - the zone name and password  

SBR_WEBDRIVER = config('SBR_WEBDRIVER',default=None) 

  
def scrape(url=None):  
    print('Connecting to Scraping Browser...')  
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')  
    html=""
    with Remote(sbr_connection, options=ChromeOptions()) as driver:  
        print(f'Connected! Navigating...{url}')  
        driver.get(url)  # use this, or replace with URL of your choice
        print('Taking page screenshot to file page.png')  
        driver.get_screenshot_as_file('./page.png')  
        print('Navigated! Scraping page content...')  
        html = driver.page_source  
        print(html)  
    return html
  