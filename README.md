##  📖 Table Of Contents
- About
- How to Build
- Documentation
- Code explanation
- Feedback and Contributions
- Contacts

## 🚀 About
**DataEntry-Capstone** This project is a web scraping and automation script that extracts housing data from a Zillow clone website and automatically fills in a Google Form with the scraped data. The script uses requests and BeautifulSoup for web scraping and selenium for browser automation.

## 📝 How to Build
**Prerequisites**
  - Python 3.x
  - requests library
  - BeautifulSoup from bs4 library
  - selenium library
  - Webdriver for your browser (e.g., ChromeDriver for Google Chrome)

  **To build the project follow these steps:**
  - **installation:**

```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed
            
# Clone the repository
git clone https://github.com/Akwaowo91/DataEntry-Capstone.git
cd DataEntry-Capstone       

# Install the required package
pip install Flask
pip install requests
pip install beautifulsoup4
pip install selenium
```
  - **Download and install the appropriate WebDriver for your browser:**
      - For Google Chrome: ChromeDriver
        
  - **Running the Script:**
      - Update the Google Form URL:
          - Replace the Google Form URL in the script with your form's URL.
      - Run the script:
        ```shell
        python main.py
        ```
          - The script will open a browser, navigate to the Google Form, and start filling it with the scraped data.
            
  - **Documentation:**
      - Selenium: https://www.selenium.dev/documentation/
      - Beautiful Soup: https://beautiful-soup-4.readthedocs.io/en/latest/
      - Flask: https://flask.palletsprojects.com/en/3.0.x/

## 📄 Code Explanation
  - The script performs the following steps:
      - **Web Scraping**:
          - Sends a GET request to the Zillow clone URL.
          - Parses the HTML content using BeautifulSoup.
          - Extracts house prices, addresses, and links.
            
      - **Data Cleaning**:
          - Defines a helper function clean_price to clean the extracted price text.
          - Stores cleaned data in separate lists for house prices, addresses, and links.
            
      - **Form Automation**:
          - Configures Selenium to keep the browser open after the script completes.
          - Opens the Google Form using Selenium.
          - Iterates over the extracted data and fills in the form fields using XPath to locate elements.
          - Submits the form for each entry and clicks the "Submit another response" link if there are more items to process.
       
## 🤝 Feedback and Contributions
I have made every effort to implement all the main aspects of the DataEntry-Capstone project in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the DataEntry-Capstone project more robust and user-friendly.

Please feel free to submit an issue or open an issue on this repository, if you have any feedback or suggestions.
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.
I appreciate your support and look forward to making this product even better with your help!

## ©️ Contact
For more questions you can reach me through:  
- email: akwaowoudokop15@gmail.com
- LinkedIn: https://www.linkedin.com/in/akwaowo-udokop-474662229/
