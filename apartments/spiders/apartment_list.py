import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/dallas-tx-75214/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19145/1000-to-2000',
        'https://www.apartments.com/san-francisco-ca-94105/1000-to-2000',
        'https://www.apartments.com/san-francisco-ca-94110/1000-to-2000',
        'https://www.apartments.com/portsmouth-va-23701/1000-to-2000',
        'https://www.apartments.com/portsmouth-va-23707/1000-to-2000',
        'https://www.apartments.com/austin-tx-78736/1000-to-2000',
        'https://www.apartments.com/austin-tx-78748/1000-to-2000',
        'https://www.apartments.com/austin-tx-78745/1000-to-2000',
        'https://www.apartments.com/portsmouth-va-23702/1000-to-2000',
        'https://www.apartments.com/newport-news-va-23602/1000-to-2000',
        'https://www.apartments.com/tucson-az-85705/1000-to-2000',
        'https://www.apartments.com/ocala-fl-34470/1000-to-2000',
        'https://www.apartments.com/tucson-az-85745/1000-to-2000',
        'https://www.apartments.com/tucson-az-85719/1000-to-2000',
        'https://www.apartments.com/tucson-az-85716/1000-to-2000',
        'https://www.apartments.com/harrisburg-pa-17109/1000-to-2000',
        'https://www.apartments.com/killeen-tx-76541/1000-to-2000',
        'https://www.apartments.com/killeen-tx-76549/1000-to-2000',
        'https://www.apartments.com/killeen-tx-76543/1000-to-2000',
        'https://www.apartments.com/roseville-mi-48066/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90803/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90804/1000-to-2000',
        'https://www.apartments.com/miami-fl-33193/1000-to-2000',
        'https://www.apartments.com/miami-fl-33135/1000-to-2000',
        'https://www.apartments.com/miami-fl-33127/1000-to-2000',
        'https://www.apartments.com/miami-fl-33138/1000-to-2000',
        'https://www.apartments.com/miami-fl-33126/1000-to-2000',
        'https://www.apartments.com/miami-fl-33144/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10457/1000-to-2000',
        'https://www.apartments.com/little-rock-ar-72204/1000-to-2000',
        'https://www.apartments.com/chester-pa-19013/1000-to-2000',
        'https://www.apartments.com/upper-darby-pa-19082/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19131/1000-to-2000',
        'https://www.apartments.com/palm-springs-ca-92264/1000-to-2000',
        'https://www.apartments.com/novi-mi-48374/1000-to-2000',
        'https://www.apartments.com/san-francisco-ca-94112/1000-to-2000',
        'https://www.apartments.com/boston-ma-02127/1000-to-2000',
        'https://www.apartments.com/monroe-ga-30655/1000-to-2000',
        'https://www.apartments.com/chapel-hill-nc-27514/1000-to-2000',
        'https://www.apartments.com/chapel-hill-nc-27517/1000-to-2000',
        'https://www.apartments.com/durham-nc-27713/1000-to-2000',
        'https://www.apartments.com/tucker-ga-30084/1000-to-2000',
        'https://www.apartments.com/hollywood-fl-33020/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85015/1000-to-2000'



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
