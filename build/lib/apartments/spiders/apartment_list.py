import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/fontana-ca-92336/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92507/1000-to-2000',
        'https://www.apartments.com/hemet-ca-92543/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92501/1000-to-2000',
        'https://www.apartments.com/hemet-ca-92545/1000-to-2000',
        'https://www.apartments.com/chesapeake-va-23321/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38116/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38122/1000-to-2000',
        'https://www.apartments.com/albuquerque-nm-87110/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38111/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38108/1000-to-2000',
        'https://www.apartments.com/washington-dc-20012/1000-to-2000',
        'https://www.apartments.com/washington-dc-20015/1000-to-2000',
        'https://www.apartments.com/fort-pierce-fl-34951/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32209/1000-to-2000',
        'https://www.apartments.com/north-hollywood-ca-91605/1000-to-2000',
        'https://www.apartments.com/desoto-tx-75115/1000-to-2000',
        'https://www.apartments.com/sauk-rapids-mn-56379/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10463/1000-to-2000',
        'https://www.apartments.com/lancaster-ca-93536/1000-to-2000',
        'https://www.apartments.com/charleston-sc-29407/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90028/1000-to-2000',
        'https://www.apartments.com/campbell-ca-95008/1000-to-2000',
        'https://www.apartments.com/sunnyvale-ca-94086/1000-to-2000',
        'https://www.apartments.com/jonesboro-ga-30236/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46229/1000-to-2000',
        'https://www.apartments.com/palm-coast-fl-32137/1000-to-2000',
        'https://www.apartments.com/fruitland-park-fl-34731/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33610/1000-to-2000',
        'https://www.apartments.com/saint-louis-mo-63109/1000-to-2000',
        'https://www.apartments.com/tallahassee-fl-32304/1000-to-2000',
        'https://www.apartments.com/saint-louis-mo-63116/1000-to-2000',
        'https://www.apartments.com/south-bend-in-46619/1000-to-2000',
        'https://www.apartments.com/south-bend-in-46615/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28212/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33604/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33617/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48238/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33614/1000-to-2000',
        'https://www.apartments.com/greenville-sc-29615/1000-to-2000',
        'https://www.apartments.com/greenville-sc-29605/1000-to-2000',
        'https://www.apartments.com/grand-rapids-mi-49503/1000-to-2000',
        'https://www.apartments.com/greenville-sc-29611/1000-to-2000',
        'https://www.apartments.com/haverhill-ma-01832/1000-to-2000',
        'https://www.apartments.com/haverhill-ma-01830/1000-to-2000'
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
