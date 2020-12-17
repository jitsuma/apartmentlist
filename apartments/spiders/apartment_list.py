import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/richmond-va-23219/1000-to-2000',
        'https://www.apartments.com/mesa-az-85201/1000-to-2000',
        'https://www.apartments.com/apache-junction-az-85119/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11208/1000-to-2000',
        'https://www.apartments.com/gresham-or-97030/1000-to-2000',
        'https://www.apartments.com/apple-valley-ca-92307/1000-to-2000',
        'https://www.apartments.com/tallahassee-fl-32304/1000-to-2000',
        'https://www.apartments.com/zanesville-oh-43701/1000-to-2000',
        'https://www.apartments.com/vero-beach-fl-32967/1000-to-2000',
        'https://www.apartments.com/vero-beach-fl-32960/1000-to-2000',
        'https://www.apartments.com/middleton-id-83644/1000-to-2000',
        'https://www.apartments.com/twin-falls-id-83301/1000-to-2000',
        'https://www.apartments.com/tahlequah-ok-74464/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85032/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33614/1000-to-2000',
        'https://www.apartments.com/hollywood-fl-33020/1000-to-2000',
        'https://www.apartments.com/hollywood-fl-33019/1000-to-2000',
        'https://www.apartments.com/wilson-nc-27896/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75229/1000-to-2000',
        'https://www.apartments.com/north-las-vegas-nv-89084/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30309/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89122/1000-to-2000',
        'https://www.apartments.com/valdosta-ga-31601/1000-to-2000',
        'https://www.apartments.com/pasadena-ca-91106/1000-to-2000',
        'https://www.apartments.com/schenectady-ny-12308/1000-to-2000',
        'https://www.apartments.com/martinez-ca-94553/1000-to-2000',
        'https://www.apartments.com/schenectady-ny-12303/1000-to-2000',
        'https://www.apartments.com/el-mirage-az-85335/1000-to-2000',
        'https://www.apartments.com/portsmouth-va-23702/1000-to-2000',
        'https://www.apartments.com/portsmouth-va-23704/1000-to-2000'

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
