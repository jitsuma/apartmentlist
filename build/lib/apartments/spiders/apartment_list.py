import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/mooresville-nc-28117/1000-to-2000',
        'https://www.apartments.com/montgomery-al-36116/1000-to-2000',
        'https://www.apartments.com/fall-river-ma-02721/1000-to-2000',
        'https://www.apartments.com/lenoir-nc-28645/1000-to-2000',
        'https://www.apartments.com/bryan-tx-77807/1000-to-2000',
        'https://www.apartments.com/bryan-tx-77801/1000-to-2000',
        'https://www.apartments.com/west-palm-beach-fl-33417/1000-to-2000',
        'https://www.apartments.com/mooresville-nc-28115/1000-to-2000',
        'https://www.apartments.com/mooresville-nc-28125/1000-to-2000',
        'https://www.apartments.com/woodbridge-va-22191/1000-to-2000',
        'https://www.apartments.com/cedartown-ga-30125/1000-to-2000',
        'https://www.apartments.com/sebring-fl-33872/1000-to-2000',
        'https://www.apartments.com/sebring-fl-33870/1000-to-2000',
        'https://www.apartments.com/houston-tx-77091/1000-to-2000',
        'https://www.apartments.com/sterling-heights-mi-48313/1000-to-2000',
        'https://www.apartments.com/chicago-il-60657/1000-to-2000',
        'https://www.apartments.com/fall-river-ma-02720/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32811/1000-to-2000',
        'https://www.apartments.com/ann-arbor-mi-48104/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44121/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44105/1000-to-2000',
        'https://www.apartments.com/trenton-tn-38382/1000-to-2000',
        'https://www.apartments.com/jackson-tn-38301/1000-to-2000'

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
