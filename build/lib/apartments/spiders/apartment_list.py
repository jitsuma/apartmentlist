import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/redding-ca-96001/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85020/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89101/1000-to-2000',
        'https://www.apartments.com/lake-worth-fl-33460/1000-to-2000',
        'https://www.apartments.com/springdale-ar-72764/1000-to-2000',
        'https://www.apartments.com/vancouver-wa-98661/1000-to-2000',
        'https://www.apartments.com/greenwood-in-46143/1000-to-2000',
        'https://www.apartments.com/san-jose-ca-95128/1000-to-2000',
        'https://www.apartments.com/miami-fl-33169/1000-to-2000',
        'https://www.apartments.com/victorville-ca-92394/1000-to-2000',
        'https://www.apartments.com/haines-city-fl-33844/1000-to-2000',
        'https://www.apartments.com/lake-wales-fl-33853/1000-to-2000',
        'https://www.apartments.com/palmdale-ca-93552/1000-to-2000',
        'https://www.apartments.com/henderson-nv-89015/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19147/1000-to-2000'

        
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
