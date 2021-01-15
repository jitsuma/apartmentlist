import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/phoenix-az-85020/1000-to-2000',
        'https://www.apartments.com/lubbock-tx-79414/1000-to-2000',
        'https://www.apartments.com/lubbock-tx-79410/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/washington-mi-48094/1000-to-2000',
        'https://www.apartments.com/montgomery-al-36111/1000-to-2000',
        'https://www.apartments.com/cleveland-tx-77328/1000-to-2000',
        'https://www.apartments.com/tulsa-ok-74135/1000-to-2000',
        'https://www.apartments.com/trenton-nj-08629/1000-to-2000',
        'https://www.apartments.com/pembroke-pines-fl-33024/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33312/1000-to-2000',
        'https://www.apartments.com/braham-mn-55006/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19131/1000-to-2000',
        'https://www.apartments.com/new-providence-pa-17560/1000-to-2000',
        'https://www.apartments.com/florissant-mo-63033/1000-to-2000',
        'https://www.apartments.com/florissant-mo-63031/1000-to-2000',
        'https://www.apartments.com/southfield-mi-48033/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33316/1000-to-2000',
        'https://www.apartments.com/athens-ga-30605/1000-to-2000',
        'https://www.apartments.com/zanesville-oh-43701/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33311/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33315/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33301/1000-to-2000',
        'https://www.apartments.com/spartanburg-sc-29303/1000-to-2000'


        
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
