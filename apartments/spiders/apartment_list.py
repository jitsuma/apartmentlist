import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/fort-lauderdale-fl-33308/1000-to-2000',
        'https://www.apartments.com/mooresville-nc-28125/1000-to-2000',
        'https://www.apartments.com/lilburn-ga-30047/1000-to-2000',
        'https://www.apartments.com/dolton-il-60419/1000-to-2000',
        'https://www.apartments.com/lauderhill-fl-33313/1000-to-2000',
        'https://www.apartments.com/sunrise-fl-33351/1000-to-2000',
        'https://www.apartments.com/middleville-mi-49333/1000-to-2000',
        'https://www.apartments.com/helendale-ca-92342/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53218/1000-to-2000',
        'https://www.apartments.com/highland-park-mi-48203/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19131/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19134/1000-to-2000',
        'https://www.apartments.com/salisbury-md-21804/1000-to-2000',
        'https://www.apartments.com/alpharetta-ga-30005/1000-to-2000',
        'https://www.apartments.com/fayetteville-nc-28311/1000-to-2000',
        'https://www.apartments.com/greenville-sc-29607/1000-to-2000',
        'https://www.apartments.com/el-paso-tx-79903/1000-to-2000',
        'https://www.apartments.com/marietta-ga-30008/1000-to-2000',
        'https://www.apartments.com/murrieta-ca-92563/1000-to-2000',
        'https://www.apartments.com/murrieta-ca-92562/1000-to-2000',
        'https://www.apartments.com/baytown-tx-77520/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/chicago-il-60619/1000-to-2000',
        'https://www.apartments.com/richmond-va-23222/1000-to-2000',
        'https://www.apartments.com/richmond-va-23223/1000-to-2000',
        'https://www.apartments.com/richmond-va-23227/1000-to-2000',
        'https://www.apartments.com/richmond-va-23220/1000-to-2000',
        'https://www.apartments.com/richmond-va-23224/1000-to-2000',
        'https://www.apartments.com/lorain-oh-44055/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30311/1000-to-2000',
        'https://www.apartments.com/mcdonough-ga-30252/1000-to-2000'
        

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
