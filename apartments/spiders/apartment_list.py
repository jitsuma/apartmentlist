import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/san-jose-ca-95112/1000-to-2000',
        'https://www.apartments.com/west-palm-beach-fl-33407/1000-to-2000',
        'https://www.apartments.com/corvallis-or-97330/1000-to-2000',
        'https://www.apartments.com/murrieta-ca-92562/1000-to-2000',
        'https://www.apartments.com/murrieta-ca-92563/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90813/1000-to-2000',
        'https://www.apartments.com/killeen-tx-76549/1000-to-2000',
        'https://www.apartments.com/saint-louis-mo-63107/1000-to-2000',
        'https://www.apartments.com/killeen-tx-76541/1000-to-2000',
        'https://www.apartments.com/el-paso-tx-79901/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85020/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85015/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10469/1000-to-2000',
        'https://www.apartments.com/lansing-mi-48911/1000-to-2000',
        'https://www.apartments.com/vancouver-wa-98661/1000-to-2000',
        'https://www.apartments.com/vancouver-wa-98683/1000-to-2000',
        'https://www.apartments.com/vancouver-wa-98686/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33613/1000-to-2000',
        'https://www.apartments.com/chelsea-ma-02150/1000-to-2000',
        'https://www.apartments.com/mobile-al-36606/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92503/1000-to-2000',
        'https://www.apartments.com/moreno-valley-ca-92557/1000-to-2000',
        'https://www.apartments.com/jamaica-ny-11434/1000-to-2000',
        'https://www.apartments.com/calumet-city-il-60409/1000-to-2000',
        'https://www.apartments.com/san-diego-ca-92104/1000-to-2000',
        'https://www.apartments.com/griffin-ga-30223/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85009/1000-to-2000',
        'https://www.apartments.com/glens-falls-ny-12801/1000-to-2000',
        'https://www.apartments.com/cohoes-ny-12047/1000-to-2000',
        'https://www.apartments.com/wynantskill-ny-12198/1000-to-2000',
        'https://www.apartments.com/north-canton-oh-44720/1000-to-2000',
        'https://www.apartments.com/sonora-ca-95370/1000-to-2000',
        'https://www.apartments.com/columbia-sc-29223/1000-to-2000',
        'https://www.apartments.com/akron-oh-44314/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19134/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30032/1000-to-2000'


        
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
