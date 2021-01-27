import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/eastvale-ca-92880/1000-to-2000',
        'https://www.apartments.com/rancho-cucamonga-ca-91730/1000-to-2000',
        'https://www.apartments.com/titusville-fl-32796/1000-to-2000',
        'https://www.apartments.com/titusville-fl-32780/1000-to-2000',
        'https://www.apartments.com/conroe-tx-77301/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95814/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45237/1000-to-2000',
        'https://www.apartments.com/crum-lynne-pa-19022/1000-to-2000',
        'https://www.apartments.com/concord-nc-28027/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28208/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28217/1000-to-2000',
        'https://www.apartments.com/surprise-az-85374/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43206/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90804/1000-to-2000',
        'https://www.apartments.com/dothan-al-36301/1000-to-2000',
        'https://www.apartments.com/winter-haven-fl-33881/1000-to-2000',
        'https://www.apartments.com/cape-coral-fl-33990/1000-to-2000',
        'https://www.apartments.com/louisville-ky-40216/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90813/1000-to-2000',
        'https://www.apartments.com/dade-city-fl-33525/1000-to-2000',
        'https://www.apartments.com/houston-tx-77061/1000-to-2000',
        'https://www.apartments.com/houston-tx-77033/1000-to-2000',
        'https://www.apartments.com/houston-tx-77048/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19134/1000-to-2000',
        'https://www.apartments.com/lithonia-ga-30058/1000-to-2000',
        'https://www.apartments.com/pensacola-fl-32504/1000-to-2000'

        
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
