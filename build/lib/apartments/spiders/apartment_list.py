import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/charlotte-nc-28212/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28213/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28206/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76112/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76119/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76105/1000-to-2000',
        'https://www.apartments.com/san-ysidro-ca-92173/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37212/1000-to-2000',
        'https://www.apartments.com/evansville-in-47710/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75252/1000-to-2000',
        'https://www.apartments.com/palm-harbor-fl-34683/1000-to-2000',
        'https://www.apartments.com/evansville-in-47711/1000-to-2000',
        'https://www.apartments.com/evansville-in-47715/1000-to-2000',
        'https://www.apartments.com/new-paltz-ny-12561/1000-to-2000',
        'https://www.apartments.com/port-charlotte-fl-33980/1000-to-2000',
        'https://www.apartments.com/rochester-ny-14605/1000-to-2000',
        'https://www.apartments.com/san-dimas-ca-91773/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43213/1000-to-2000',
        'https://www.apartments.com/cornelius-nc-28031/1000-to-2000',
        'https://www.apartments.com/springfield-ma-01105/1000-to-2000',
        'https://www.apartments.com/clinton-ms-39056/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43228/1000-to-2000',
        'https://www.apartments.com/springfield-oh-45503/1000-to-2000',
        'https://www.apartments.com/dayton-oh-45405/1000-to-2000',
        'https://www.apartments.com/albany-ny-12208/1000-to-2000',
        'https://www.apartments.com/albany-ny-12209/1000-to-2000',
        'https://www.apartments.com/albany-ny-12202/1000-to-2000',
        'https://www.apartments.com/albany-ny-12203/1000-to-2000',
        'https://www.apartments.com/columbus-in-47201/1000-to-2000',
        'https://www.apartments.com/providence-ri-02906/1000-to-2000',
        'https://www.apartments.com/franklin-wi-53132/1000-to-2000',
        'https://www.apartments.com/oak-creek-wi-53154/1000-to-2000',
        'https://www.apartments.com/greendale-wi-53129/1000-to-2000',
        'https://www.apartments.com/muskego-wi-53150/1000-to-2000',
        'https://www.apartments.com/cudahy-wi-53110/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53215/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53202/1000-to-2000',
        'https://www.apartments.com/greenfield-wi-53220/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53218/1000-to-2000',
        'https://www.apartments.com/des-moines-ia-50315/1000-to-2000',
        'https://www.apartments.com/chicago-il-60624/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90063/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000'

        
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
