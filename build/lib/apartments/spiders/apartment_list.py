import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/sacramento-ca-95824/1000-to-2000',
        'https://www.apartments.com/fullerton-ca-92832/1000-to-2000',
        'https://www.apartments.com/west-palm-beach-fl-33417/1000-to-2000',
        'https://www.apartments.com/west-palm-beach-fl-33407/1000-to-2000',
        'https://www.apartments.com/wellington-fl-33414/1000-to-2000',
        'https://www.apartments.com/bakersfield-ca-93301/1000-to-2000',
        'https://www.apartments.com/tucson-az-85745/1000-to-2000',
        'https://www.apartments.com/tucson-az-85716/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10471/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10462/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30035/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30311/1000-to-2000',
        'https://www.apartments.com/tucson-az-85712/1000-to-2000',
        'https://www.apartments.com/tucson-az-85705/1000-to-2000',
        'https://www.apartments.com/chicago-il-60619/1000-to-2000',
        'https://www.apartments.com/burlington-ia-52601/1000-to-2000',
        'https://www.apartments.com/torrance-ca-90503/1000-to-2000',
        'https://www.apartments.com/marietta-ga-30066/1000-to-2000'

        
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
