from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Bright Data cloud browser...")

    options = Options()
    # optional: run headless, disable logs, etc.
    options.add_argument("--headless=new")

    # Connect to Bright Data’s remote Selenium endpoint
    driver = webdriver.Remote(
        command_executor="https://brd-customer-hl_36fb3e41-zone-ai_scraper:dvwn9xonsu16@brd.superproxy.io:9515",
        options=options
    )

    try:
        driver.get(website)
        print("Website loading...")
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return "No body content found."


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]
 
    