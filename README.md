# Web Scraping Realtor.com in New York

This project demonstrates a simple web scraping process for extracting information from real estate listings on Realtor.com specifically for properties in New York. The scraping process is implemented using the Scrapy framework in Python.

## Overview
The purpose of this project is to collect data from real estate listings on Realtor.com in New York. The spider crawls through the search results pages, extracts relevant information from each property listing, and stores it for further analysis or usage.

## Prerequisites
To run the web scraping code, make sure you have the following installed:

- Python 3 (https://www.python.org/downloads/)
- Scrapy (https://scrapy.org/)

## Running the Spider
1. Clone or download the project files from the GitHub repository.
2. Open a terminal or command prompt and navigate to the project directory.
3. Execute the following command to start the spider:
* **scrapy crawl New_York -o output.json**
* This command will start the spider named "New_York" and save the extracted data to an output file named "output.json". You can choose a different output file format such as CSV or XML if desired.
4. Sit back and let the spider crawl through the pages, scraping the real estate listings and storing the data.

## Data Extracted
The spider extracts the following information from each property listing:

* Owner: The owner of the property.
* Status: The status of the listing (e.g., For Sale, Sold, Pending).
* Price: The listing price of the property.
* Link: The URL of the property listing.
* Bed: The number of bedrooms in the property.
* Bath: The number of bathrooms in the property.
* Sqft: The total square footage of the property.
* Acre: The total acreage of the property (if available).

## Handling HTTP Errors
The spider is designed to handle HTTP errors such as 403 Forbidden responses from the server. If a request receives an error status code, the spider retries the request after a delay to ensure the scraping process continues smoothly.

## Random User Agents
To avoid detection and enhance scraping efficiency, the spider randomly selects a user agent for each request from a predefined list of user agents. This helps to simulate different browsers or clients during the scraping process.

## Limitations and Usage Policy
It's important to note that web scraping should be performed responsibly and in accordance with the website's terms of service and usage policy. Before scraping Realtor.com or any other website, make sure to review their terms of service and usage policy to ensure compliance.

**This project serves as an educational demonstration of web scraping techniques and should not be used for any unauthorized or unethical activities.**

-------------------------------------------------
This README provides an overview of the project and outlines the steps to run the spider for scraping real estate listings on Realtor.com in New York. It also highlights the data extracted, error handling, and random user agent usage.

Please refer to the code files and comments within for more detailed information about the spider implementation.

For any further inquiries or assistance, feel free to reach out. Happy scraping
