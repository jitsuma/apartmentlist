import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/ocala-fl-34470/1000-to-2000',
        'https://www.apartments.com/oklahoma-city-ok-73118/1000-to-2000',
        'https://www.apartments.com/fort-pierce-fl-34951/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30083/1000-to-2000',
        'https://www.apartments.com/victorville-ca-92394/1000-to-2000',
        'https://www.apartments.com/apple-valley-ca-92308/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45227/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45237/1000-to-2000',
        'https://www.apartments.com/chattanooga-tn-37404/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53215/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53216/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53204/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53233/1000-to-2000',
        'https://www.apartments.com/knoxville-tn-37916/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95824/1000-to-2000',
        'https://www.apartments.com/ridgewood-ny-11385/1000-to-2000',
        'https://www.apartments.com/barstow-ca-92311/1000-to-2000',
        'https://www.apartments.com/troy-mi-48084/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32822/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32805/1000-to-2000',
        'https://www.apartments.com/columbia-sc-29212/1000-to-2000',
        'https://www.apartments.com/colorado-springs-co-80910/1000-to-2000',
        'https://www.apartments.com/colorado-springs-co-80919/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75208/1000-to-2000',
        'https://www.apartments.com/augusta-ga-30907/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48235/1000-to-2000',
        'https://www.apartments.com/greensboro-nc-27403/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21201/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32208/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90063/1000-to-2000',
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
