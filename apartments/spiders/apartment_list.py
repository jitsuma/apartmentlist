import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/taylor-mi-48180/1000-to-2000',
        'https://www.apartments.com/daytona-beach-fl-32118/1000-to-2000',
        'https://www.apartments.com/saint-louis-mo-63107/1000-to-2000',
        'https://www.apartments.com/marietta-ga-30066/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89119/1000-to-2000',
        'https://www.apartments.com/wilkes-barre-pa-18702/1000-to-2000',
        'https://www.apartments.com/columbia-sc-29223/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92501/1000-to-2000',
        'https://www.apartments.com/lancaster-ca-93536/1000-to-2000',
        'https://www.apartments.com/lancaster-ca-93535/1000-to-2000',
        'https://www.apartments.com/palmdale-ca-93552/1000-to-2000',
        'https://www.apartments.com/palmdale-ca-93550/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28213/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28212/1000-to-2000',
        'https://www.apartments.com/victorville-ca-92392/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30309/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30339/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30308/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43229/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43213/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38122/1000-to-2000',
        'https://www.apartments.com/bethany-ok-73008/1000-to-2000',
        'https://www.apartments.com/livonia-mi-48150/1000-to-2000',
        'https://www.apartments.com/temple-hills-md-20748/1000-to-2000',
        'https://www.apartments.com/laurel-md-20708/1000-to-2000',
        'https://www.apartments.com/gainesville-fl-32607/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46201/1000-to-2000'


        
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
