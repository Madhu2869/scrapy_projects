import requests
from bs4 import BeautifulSoup
import csv
from validate_email_address import validate_email

# Function to scrape emails from a webpage
def scrape_emails(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    emails = set()  
    for a_tag in soup.find_all("a", href=True):
        if "mailto:" in a_tag["href"]:
            email = a_tag["href"].replace("mailto:", "").strip()
            
            # ✅ Validate email before adding
            if validate_email(email, verify=True):  
                emails.add(email)
    
    return emails


# Function to save emails to CSV
def save_to_csv(emails, filename="emails.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Valid Emails"])  # header
        for email in emails:
            writer.writerow([email])


# Main execution
if __name__ == "__main__":
    url = "https://example.com"  # replace with your target URL
    scraped_emails = scrape_emails(url)
    save_to_csv(scraped_emails)
    print("Scraping & validation completed. Check emails.csv")
