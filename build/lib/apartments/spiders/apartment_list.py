import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/jefferson-city-mo-65101/1000-to-2000',
        'https://www.apartments.com/garden-city-ny-11530/1000-to-2000',
        'https://www.apartments.com/rockville-centre-ny-11570/1000-to-2000',
        'https://www.apartments.com/tulsa-ok-74105/1000-to-2000',
        'https://www.apartments.com/east-orange-nj-07018/1000-to-2000',
        'https://www.apartments.com/fresno-ca-93728/1000-to-2000',
        'https://www.apartments.com/fresno-ca-93710/1000-to-2000',
        'https://www.apartments.com/fresno-ca-93704/1000-to-2000',
        'https://www.apartments.com/jeannette-pa-15644/1000-to-2000',
        'https://www.apartments.com/greensburg-pa-15601/1000-to-2000',
        'https://www.apartments.com/mesa-az-85204/1000-to-2000',
        'https://www.apartments.com/mesa-az-85201/1000-to-2000',
        'https://www.apartments.com/mishawaka-in-46545/1000-to-2000',
        'https://www.apartments.com/berkeley-ca-94709/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30044/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11208/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30043/1000-to-2000',
        'https://www.apartments.com/haverhill-ma-01832/1000-to-2000',
        'https://www.apartments.com/big-rapids-mi-49307/1000-to-2000',
        'https://www.apartments.com/greenville-sc-29609/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90063/1000-to-2000',
        'https://www.apartments.com/durham-nc-27713/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11203/1000-to-2000',
        'https://www.apartments.com/greenville-sc-29611/1000-to-2000',
        'https://www.apartments.com/tulsa-ok-74146/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30083/1000-to-2000',
        'https://www.apartments.com/chester-pa-19013/1000-to-2000'


        
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
