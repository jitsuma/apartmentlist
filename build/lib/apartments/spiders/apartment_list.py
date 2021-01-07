import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/greenville-sc-29607/1000-to-2000',
        'https://www.apartments.com/manhattan-ny-10021/1000-to-2000',
        'https://www.apartments.com/houston-tx-77033/1000-to-2000',
        'https://www.apartments.com/waynesboro-va-22980/1000-to-2000',
        'https://www.apartments.com/chicago-il-60651/1000-to-2000',
        'https://www.apartments.com/chicago-il-60630/1000-to-2000',
        'https://www.apartments.com/salt-lake-city-ut-84115/1000-to-2000',
        'https://www.apartments.com/west-jordan-ut-84081/1000-to-2000',
        'https://www.apartments.com/oklahoma-city-ok-73106/1000-to-2000',
        'https://www.apartments.com/kissimmee-fl-34743/1000-to-2000',
        'https://www.apartments.com/kissimmee-fl-34746/1000-to-2000',
        'https://www.apartments.com/lithia-springs-ga-30122/1000-to-2000',
        'https://www.apartments.com/sunrise-fl-33351/1000-to-2000',
        'https://www.apartments.com/lauderhill-fl-33313/1000-to-2000',
        'https://www.apartments.com/virginia-beach-va-23451/1000-to-2000',
        'https://www.apartments.com/virginia-beach-va-23464/1000-to-2000',
        'https://www.apartments.com/portsmouth-va-23702/1000-to-2000',
        'https://www.apartments.com/virginia-beach-va-23462/1000-to-2000',
        'https://www.apartments.com/apple-valley-ca-92308/1000-to-2000',
        'https://www.apartments.com/madison-al-35758/1000-to-2000',
        'https://www.apartments.com/mattoon-il-61938/1000-to-2000',
        'https://www.apartments.com/chicago-il-60624/1000-to-2000',
        'https://www.apartments.com/fayetteville-nc-28314/1000-to-2000',
        'https://www.apartments.com/fayetteville-nc-28311/1000-to-2000',
        'https://www.apartments.com/virginia-beach-va-23455/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46218/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76119/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76123/1000-to-2000',
        'https://www.apartments.com/poinciana-fl-34759/1000-to-2000',
        'https://www.apartments.com/albuquerque-nm-87107/1000-to-2000',
        'https://www.apartments.com/murrieta-ca-92562/1000-to-2000',
        'https://www.apartments.com/mount-vernon-ny-10550/1000-to-2000',
        'https://www.apartments.com/capitol-heights-md-20743/1000-to-2000',
        'https://www.apartments.com/murrieta-ca-92563/1000-to-2000',
        'https://www.apartments.com/district-heights-md-20747/1000-to-2000',
        'https://www.apartments.com/springfield-il-62704/1000-to-2000',
        'https://www.apartments.com/columbia-md-21046/1000-to-2000',
        'https://www.apartments.com/richmond-va-23219/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53216/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21201/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53215/1000-to-2000',
        'https://www.apartments.com/oak-creek-wi-53154/1000-to-2000',
        'https://www.apartments.com/racine-wi-53402/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53233/1000-to-2000',
        'https://www.apartments.com/mount-vernon-ny-10552/1000-to-2000',
        'https://www.apartments.com/new-smyrna-beach-fl-32169/1000-to-2000'
        

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
