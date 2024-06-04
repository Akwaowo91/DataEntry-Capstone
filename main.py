import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

API = "https://appbrewery.github.io/Zillow-Clone/"

# Google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSfviVEO9428dfk0_" \
#                    "LnY5wI1KpLVEKhj1sH99IQ3QMFSYYuWjg/viewform?usp=sf_link"
#
# Google_form_link_short = "https://forms.gle/xwCT4ei4KDiqfg7L9"

response = requests.get(API)
housing_webpage = response.text

soup = BeautifulSoup(housing_webpage, "html.parser")

house_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
house_address = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
house_links = soup.find_all(name="a", class_="property-card-link")
# link = house_links.get("href")
house_costs = []
links = []
house_addresses = []


# Function to clean price text
def clean_price(price_text):
    # Remove anything after the dollar amount
    clean_text = price_text.split('+')[0].split('/')[0].strip()
    return clean_text


# Extract and store house prices
for price in house_prices:
    house_cost = clean_price(price.get_text())
    house_costs.append(house_cost)

for link in house_links:
    href = link.get('href')
    links.append(href)

for address in house_address:
    house_addy = address.get_text(strip=True)
    house_addresses.append(house_addy)

# print(house_costs)
# print(links)
# print(house_addresses)

# THIS IS TO KEEP CHROME OPEN AFTER PROGRAM FINISHES
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

time.sleep(2)
driver.get("https://forms.gle/xwCT4ei4KDiqfg7L9")
time.sleep(1)


# address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/'
#                                                     'div[1]/div/div[1]/input')
# address_input.send_keys(house_addresses[0])
# time.sleep(1)
#
# price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
#                                                   '/div/div[1]/div/div[1]/input')
# price_input.send_keys(house_costs[0])
# time.sleep(1)
#
# link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
#                                                  '/div/div[1]/div/div[1]/input')
# link_input.send_keys(links[0])
# time.sleep(1)
#
# submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
# submit.click()
# time.sleep(1)
#
# submit_another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
# submit_another_response.click()


for i in range(len(house_addresses)):
    # Locate and fill in the address input
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/'
                                                        'div[1]/div/div[1]/input')
    address_input.clear()  # Clear the input field before entering new data
    address_input.send_keys(house_addresses[i])
    time.sleep(1)

    # Locate and fill in the price input
    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                      '/div/div[1]/div/div[1]/input')
    price_input.clear()  # Clear the input field before entering new data
    price_input.send_keys(house_costs[i])
    time.sleep(1)

    # Locate and fill in the link input
    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                                     '/div/div[1]/div/div[1]/input')
    link_input.clear()  # Clear the input field before entering new data
    link_input.send_keys(links[i])
    time.sleep(1)

    # Locate and click the submit button
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()
    time.sleep(1)

    # Locate and click the "Submit another response" link
    if i < len(house_addresses) - 1:  # Only click "Submit another response" if there are more items to process
        submit_another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submit_another_response.click()
        time.sleep(1)

# Close the driver after completing the task
driver.quit()
