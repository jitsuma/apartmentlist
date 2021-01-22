import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/tulsa-ok-74120/1000-to-2000',
        'https://www.apartments.com/oakland-ca-94619/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30083/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30088/1000-to-2000',
        'https://www.apartments.com/pell-city-al-35128/1000-to-2000',
        'https://www.apartments.com/lake-wales-fl-33853/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10469/1000-to-2000',
        'https://www.apartments.com/fayetteville-nc-28303/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10462/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30044/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43213/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19147/1000-to-2000',
        'https://www.apartments.com/norwich-ct-06360/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89121/1000-to-2000',
        'https://www.apartments.com/lowell-ma-01854/1000-to-2000',
        'https://www.apartments.com/leesburg-fl-34748/1000-to-2000',
        'https://www.apartments.com/round-rock-tx-78664/1000-to-2000',
        'https://www.apartments.com/corpus-christi-tx-78401/1000-to-2000',
        'https://www.apartments.com/harrisburg-pa-17103/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30043/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30045/1000-to-2000',
        'https://www.apartments.com/killeen-tx-76549/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30046/1000-to-2000',
        'https://www.apartments.com/muskegon-mi-49441/1000-to-2000',
        'https://www.apartments.com/gobles-mi-49055/1000-to-2000',
        'https://www.apartments.com/georgetown-tx-78628/1000-to-2000',
        'https://www.apartments.com/clinton-township-mi-48036/1000-to-2000',
        'https://www.apartments.com/victorville-ca-92392/1000-to-2000',
        'https://www.apartments.com/jonesboro-ga-30236/1000-to-2000',
        'https://www.apartments.com/stockbridge-ga-30281/1000-to-2000',
        'https://www.apartments.com/youngstown-oh-44502/1000-to-2000'


        
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
