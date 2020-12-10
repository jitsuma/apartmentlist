import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/philadelphia-pa-19134/1000-to-2000',
        'https://www.apartments.com/marietta-ga-30008/1000-to-2000',
        'https://www.apartments.com/columbus-ga-31904/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38105/1000-to-2000',
        'https://www.apartments.com/panama-city-fl-32404/1000-to-2000',
        'https://www.apartments.com/cicero-il-60804/1000-to-2000',
        'https://www.apartments.com/goodyear-az-85338/1000-to-2000',
        'https://www.apartments.com/avondale-az-85392/1000-to-2000',
        'https://www.apartments.com/jamestown-ny-14701/1000-to-2000',
        'https://www.apartments.com/buffalo-ny-14211/1000-to-2000',
        'https://www.apartments.com/asheville-nc-28803/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46201/1000-to-2000',
        'https://www.apartments.com/odessa-tx-79761/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21217/1000-to-2000',
        'https://www.apartments.com/lombard-il-60148/1000-to-2000',
        'https://www.apartments.com/batavia-ny-14020/1000-to-2000',
        'https://www.apartments.com/colorado-springs-co-80903/1000-to-2000',
        'https://www.apartments.com/seattle-wa-98105/1000-to-2000',
        'https://www.apartments.com/dunkirk-ny-14048/1000-to-2000',
        'https://www.apartments.com/buffalo-ny-14215/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89119/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48238/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30030/1000-to-2000',
        'https://www.apartments.com/waterbury-ct-06708/1000-to-2000',
        'https://www.apartments.com/addison-il-60101/1000-to-2000',
        'https://www.apartments.com/baton-rouge-la-70802/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90802/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90813/1000-to-2000',
        'https://www.apartments.com/west-chester-oh-45069/1000-to-2000',
        'https://www.apartments.com/mason-oh-45040/1000-to-2000',
        'https://www.apartments.com/arlington-tx-76015/1000-to-2000',
        'https://www.apartments.com/warren-mi-48089/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37211/1000-to-2000',
        'https://www.apartments.com/winter-park-fl-32792/1000-to-2000',
        'https://www.apartments.com/ludlow-ma-01056/1000-to-2000',
        'https://www.apartments.com/chesapeake-va-23324/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19103/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19147/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19145/1000-to-2000'

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
