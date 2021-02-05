import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/el-mirage-az-85335/1000-to-2000',
        'https://www.apartments.com/omaha-ne-68131/1000-to-2000',
        'https://www.apartments.com/providence-ri-02906/1000-to-2000',
        'https://www.apartments.com/decatur-al-35601/1000-to-2000',
        'https://www.apartments.com/monroeville-pa-15146/1000-to-2000',
        'https://www.apartments.com/port-saint-lucie-fl-34953/1000-to-2000',
        'https://www.apartments.com/alton-il-62002/1000-to-2000',
        'https://www.apartments.com/burlington-ia-52601/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46208/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46218/1000-to-2000',
        'https://www.apartments.com/new-port-richey-fl-34653/1000-to-2000',
        'https://www.apartments.com/columbia-md-21046/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38108/1000-to-2000',
        'https://www.apartments.com/grand-rapids-mi-49503/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48235/1000-to-2000',
        'https://www.apartments.com/port-saint-lucie-fl-34986/1000-to-2000',
        'https://www.apartments.com/franklin-park-il-60131/1000-to-2000',
        'https://www.apartments.com/vero-beach-fl-32960/1000-to-2000',
        'https://www.apartments.com/berkeley-il-60163/1000-to-2000',
        'https://www.apartments.com/bellwood-il-60104/1000-to-2000',
        'https://www.apartments.com/river-forest-il-60305/1000-to-2000',
        'https://www.apartments.com/melrose-park-il-60160/1000-to-2000',
        'https://www.apartments.com/vero-beach-fl-32962/1000-to-2000',
        'https://www.apartments.com/goodyear-az-85338/1000-to-2000',
        'https://www.apartments.com/chesapeake-va-23324/1000-to-2000',
        'https://www.apartments.com/manhattan-ny-10033/1000-to-2000',
        'https://www.apartments.com/tucson-az-85705/1000-to-2000',
        'https://www.apartments.com/dayton-oh-45431/1000-to-2000',
        'https://www.apartments.com/dayton-oh-45405/1000-to-2000'

        
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
