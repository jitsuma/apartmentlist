import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/bakersfield-ca-93307/1000-to-2000',
        'https://www.apartments.com/bakersfield-ca-93305/1000-to-2000',
        'https://www.apartments.com/chicago-il-60619/1000-to-2000',
        'https://www.apartments.com/chicago-il-60617/1000-to-2000',
        'https://www.apartments.com/rockford-il-61104/1000-to-2000',
        'https://www.apartments.com/rockford-il-61103/1000-to-2000',
        'https://www.apartments.com/edmond-ok-73013/1000-to-2000',
        'https://www.apartments.com/mishawaka-in-46545/1000-to-2000',
        'https://www.apartments.com/fresno-ca-93710/1000-to-2000',
        'https://www.apartments.com/bartow-fl-33830/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28205/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90063/1000-to-2000',
        'https://www.apartments.com/houston-tx-77017/1000-to-2000',
        'https://www.apartments.com/houston-tx-77477/1000-to-2000',
        'https://www.apartments.com/new-rochelle-ny-10805/1000-to-2000',
        'https://www.apartments.com/ypsilanti-mi-48197/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19141/1000-to-2000',
        'https://www.apartments.com/dalton-ga-30721/1000-to-2000',
        'https://www.apartments.com/jackson-mi-49201/1000-to-2000',
        'https://www.apartments.com/conroe-tx-77304/1000-to-2000',
        'https://www.apartments.com/meridian-ms-39301/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11234/1000-to-2000',
        'https://www.apartments.com/greensboro-nc-27401/1000-to-2000',
        'https://www.apartments.com/harrisburg-pa-17103/1000-to-2000',
        'https://www.apartments.com/winston-salem-nc-27106/1000-to-2000',
        'https://www.apartments.com/saint-petersburg-fl-33714/1000-to-2000',
        'https://www.apartments.com/panama-city-fl-32404/1000-to-2000',
        'https://www.apartments.com/williamstown-ky-41097/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85035/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92507/1000-to-2000',
        'https://www.apartments.com/largo-fl-33771/1000-to-2000',
        'https://www.apartments.com/largo-fl-33770/1000-to-2000',
        'https://www.apartments.com/romulus-mi-48174/1000-to-2000',
        'https://www.apartments.com/westwego-la-70094/1000-to-2000',
        'https://www.apartments.com/jacksonville-nc-28540/1000-to-2000',
        'https://www.apartments.com/norwalk-ct-06851/1000-to-2000',
        'https://www.apartments.com/el-cajon-ca-92020/1000-to-2000'

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
