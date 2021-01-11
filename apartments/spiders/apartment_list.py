import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/lehigh-acres-fl-33936/1000-to-2000',
        'https://www.apartments.com/lehigh-acres-fl-33972/1000-to-2000',
        'https://www.apartments.com/chillicothe-oh-45601/1000-to-2000',
        'https://www.apartments.com/mableton-ga-30126/1000-to-2000',
        'https://www.apartments.com/chesapeake-va-23325/1000-to-2000',
        'https://www.apartments.com/brandon-fl-33511/1000-to-2000',
        'https://www.apartments.com/tucson-az-85713/1000-to-2000',
        'https://www.apartments.com/garland-tx-75043/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30032/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30083/1000-to-2000',
        'https://www.apartments.com/spokane-wa-99201/1000-to-2000',
        'https://www.apartments.com/tyler-tx-75703/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46218/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33612/1000-to-2000',
        'https://www.apartments.com/westfield-ma-01085/1000-to-2000',
        'https://www.apartments.com/natick-ma-01760/1000-to-2000',
        'https://www.apartments.com/arlington-tx-76012/1000-to-2000',
        'https://www.apartments.com/horn-lake-ms-38637/1000-to-2000',
        'https://www.apartments.com/west-springfield-ma-01089/1000-to-2000',
        'https://www.apartments.com/jonesboro-ga-30236/1000-to-2000',
        'https://www.apartments.com/canton-mi-48188/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30035/1000-to-2000',
        'https://www.apartments.com/upper-marlboro-md-20774/1000-to-2000',
        'https://www.apartments.com/bayonne-nj-07002/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44110/1000-to-2000',
        'https://www.apartments.com/suffolk-va-23434/1000-to-2000',
        'https://www.apartments.com/clarkston-ga-30021/1000-to-2000',
        'https://www.apartments.com/tucker-ga-30084/1000-to-2000',
        'https://www.apartments.com/norcross-ga-30092/1000-to-2000',
        'https://www.apartments.com/manhattan-ny-10002/1000-to-2000',
        'https://www.apartments.com/saint-louis-mo-63111/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85008/1000-to-2000',
        'https://www.apartments.com/cocoa-fl-32927/1000-to-2000',
        'https://www.apartments.com/mansfield-ma-02048/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11203/1000-to-2000',
        'https://www.apartments.com/pensacola-fl-32504/1000-to-2000',
        'https://www.apartments.com/lawton-ok-73505/1000-to-2000',
        'https://www.apartments.com/buckeye-az-85396/1000-to-2000',
        'https://www.apartments.com/avondale-estates-ga-30002/1000-to-2000'

        

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
