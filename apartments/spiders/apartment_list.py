import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/riverside-ca-92507/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89135/1000-to-2000',
        'https://www.apartments.com/cedar-grove-nc-27231/1000-to-2000',
        'https://www.apartments.com/greenville-nc-27858/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76107/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76123/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76119/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32803/1000-to-2000',
        'https://www.apartments.com/kalamazoo-mi-49006/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75208/1000-to-2000',
        'https://www.apartments.com/adelanto-ca-92301/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89166/1000-to-2000',
        'https://www.apartments.com/charlottesville-va-22903/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89145/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89117/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89138/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89108/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89148/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89183/1000-to-2000',
        'https://www.apartments.com/sun-city-center-fl-33573/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89128/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89131/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89139/1000-to-2000',
        'https://www.apartments.com/moss-point-ms-39563/1000-to-2000',
        'https://www.apartments.com/saint-louis-mo-63136/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89103/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11208/1000-to-2000',
        'https://www.apartments.com/saint-louis-mo-63139/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76105/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48026/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19141/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19104/1000-to-2000',
        'https://www.apartments.com/kansas-city-mo-64123/1000-to-2000',
        'https://www.apartments.com/flint-mi-48503/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43212/1000-to-2000',
        'https://www.apartments.com/parkville-md-21234/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43205/1000-to-2000',
        'https://www.apartments.com/medford-ny-11763/1000-to-2000',
        'https://www.apartments.com/sayville-ny-11782/1000-to-2000'


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
