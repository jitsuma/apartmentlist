import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/concord-ca-94520/1000-to-2000',
        'https://www.apartments.com/calexico-ca-92231/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32209/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32208/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32206/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85020/1000-to-2000',
        'https://www.apartments.com/plano-tx-75023/1000-to-2000',
        'https://www.apartments.com/jackson-mi-49201/1000-to-2000',
        'https://www.apartments.com/plano-tx-75074/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38107/1000-to-2000',
        'https://www.apartments.com/newport-news-va-23608/1000-to-2000',
        'https://www.apartments.com/bradenton-fl-34207/1000-to-2000',
        'https://www.apartments.com/rocky-mount-nc-27804/1000-to-2000',
        'https://www.apartments.com/lake-worth-fl-33467/1000-to-2000',
        'https://www.apartments.com/conroe-tx-77301/1000-to-2000',
        'https://www.apartments.com/conroe-tx-77356/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46218/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90029/1000-to-2000',
        'https://www.apartments.com/winter-park-fl-32792/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44121/1000-to-2000',
        'https://www.apartments.com/janesville-wi-53546/1000-to-2000',
        'https://www.apartments.com/macon-ga-31206/1000-to-2000',
        'https://www.apartments.com/milledgeville-ga-31061/1000-to-2000',
        'https://www.apartments.com/macon-ga-31204/1000-to-2000',
        'https://www.apartments.com/macon-ga-31217/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75208/1000-to-2000',
        'https://www.apartments.com/little-rock-ar-72205/1000-to-2000',
        'https://www.apartments.com/lake-charles-la-70605/1000-to-2000',
        'https://www.apartments.com/lake-charles-la-70601/1000-to-2000',
        'https://www.apartments.com/ridgewood-ny-11385/1000-to-2000',
        'https://www.apartments.com/rogers-ar-72756/1000-to-2000',
        'https://www.apartments.com/pearl-city-hi-96782/1000-to-2000',
        'https://www.apartments.com/miami-fl-33126/1000-to-2000',
        'https://www.apartments.com/wilmington-de-19805/1000-to-2000'

            ]

    def parse(self, response):
        print("procesing:"+response.url)
        #Extract data using css selectors
        propertyname = response.xpath("//div[@class='property-title']/span/text()").extract()
        address=response.xpath("//div[@class='property-address js-url']/text()").extract()
        phone_number=response.xpath("//div[@class='phone-wrapper']/a/span/text()").extract()
        link_url=response.xpath("//div[@class='property-information']/a/@href").extract()

        row_data=zip(propertyname,address,phone_number,link_url)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'name':item[0],
                'address' : item[1], #item[0] means product in the list and so on, index tells what value to assign
                'phone_number' : item[2],
                'link_url' : item[3]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
