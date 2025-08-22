import scrapy
import re

class EmailtrackSpider(scrapy.Spider):
    name = "emailtrack"
    start_urls = ["https://www.geeksforgeeks.org/"]

    def parse(self, response):
        # find emails in page
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", response.text)

        for email in emails:
            yield {"email": email}   # ✅ this makes Scrapy save into CSV/JSON

        # follow links
        for link in response.css("a::attr(href)").getall():
            if link.startswith("http"):
                yield response.follow(link, callback=self.parse)
