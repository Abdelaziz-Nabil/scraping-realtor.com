import scrapy
import random
from scrapy.http import HtmlResponse
from time import sleep

class NewYorkSpider(scrapy.Spider):
    name = "New_York"
    allowed_domains = ["www.realtor.com"]
    start_urls = ["https://www.realtor.com/realestateandhomes-search/New-York"]
   
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    ]
    
    def start_requests(self):
        for url in self.start_urls:
            # Randomly select a user agent
            user_agent = random.choice(self.USER_AGENTS)
            headers = {'User-Agent': user_agent}
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        
        request_user_agent = response.request.headers.get('User-Agent').decode('utf-8')
        # Print the user agent
        print("request User Agent:", request_user_agent)

        # Check the response status
        if response.status == 200:
            cards = response.css('div.BasePropertyCard_propertyCardWrap__J0xUj')
            for card in cards:
                owner = card.css('span.BrokerTitle_titleText__20u1P::text').get()
                status= card.css('div.StatusBadgestyles__StyledStatusBadge-rui__sc-1wog16p-0.bFsBVL div::text').get()
                price= card.css('div.price-wrapper div::text').get()
                link= card.css('.CardContent__StyledCardContent-rui__sc-7ptz1z-0 a::attr(href)').get()
                bed= card.css('li.PropertyBedMetastyles__StyledPropertyBedMeta-rui__a4nnof-0.cHVLag span::text').get()
                bath= card.css('li.PropertyBathMetastyles__StyledPropertyBathMeta-rui__sc-67m6bo-0.bSPXLm span::text').get()
                Sqft= card.css('li.PropertySqftMetastyles__StyledPropertySqftMeta-rui__sc-1gdau7i-0.fnhaOV span::text').get()
                acre= card.css('li.PropertyLotSizeMetastyles__StyledPropertyLotSizeMeta-rui__sc-1cz4zco-0.cNMyen span.VisuallyHiddenstyles__StyledVisuallyHidden-rui__aoql8k-0.bszylW::text').get()
                
                yield {
                    'owner' : owner.replace('Brokered by ', '') if owner is not None else None, 
                    'status' : status.replace('For ', '') if status is not None else None,
                    'price': price,
                    'link' : response.urljoin(link),
                    'bed': bed,
                    'bath': bath,
                    'Sqft': Sqft,
                    'acre': (acre.replace(' acre lot', '')).replace(" square foot lot", '') if acre is not None else None,
                }
                
            next_page = response.urljoin(response.css("a[aria-label='Go to next page']::attr(href)").get())
            if next_page:
            # Randomly select a user agent for the next request
                user_agent = random.choice(self.USER_AGENTS)
                headers = {'User-Agent': user_agent}
                yield scrapy.Request(url=next_page, headers=headers, callback=self.parse)
        else:
            # Retry the request with a delay
            print(f"Request failed with status code {response.status}. Retrying...")
            sleep(5)  # Delay for 5 seconds
            user_agent = random.choice(self.USER_AGENTS)
            headers = {'User-Agent': user_agent}
            yield scrapy.Request(url=response.url, headers=headers, callback=self.parse)