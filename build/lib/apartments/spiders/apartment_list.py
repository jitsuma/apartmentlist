import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/hayward-ca-94541/1000-to-2000',
        'https://www.apartments.com/castro-valley-ca-94552/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95814/1000-to-2000',
        'https://www.apartments.com/placerville-ca-95667/1000-to-2000',
        'https://www.apartments.com/brockton-ma-02301/1000-to-2000',
        'https://www.apartments.com/chesapeake-va-23324/1000-to-2000',
        'https://www.apartments.com/bradenton-fl-34203/1000-to-2000',
        'https://www.apartments.com/bradenton-fl-34207/1000-to-2000',
        'https://www.apartments.com/arlington-tx-76010/1000-to-2000',
        'https://www.apartments.com/university-park-il-60484/1000-to-2000',
        'https://www.apartments.com/monee-il-60449/1000-to-2000',
        'https://www.apartments.com/hazel-crest-il-60429/1000-to-2000',
        'https://www.apartments.com/chicago-heights-il-60411/1000-to-2000',
        'https://www.apartments.com/saint-joseph-mo-64506/1000-to-2000',
        'https://www.apartments.com/wyandotte-mi-48192/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46201/1000-to-2000',
        'https://www.apartments.com/el-paso-tx-79902/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/sumter-sc-29150/1000-to-2000',
        'https://www.apartments.com/kerrville-tx-78028/1000-to-2000',
        'https://www.apartments.com/fall-river-ma-02720/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76109/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76107/1000-to-2000',
        'https://www.apartments.com/worcester-ma-01607/1000-to-2000',
        'https://www.apartments.com/dudley-ma-01571/1000-to-2000',
        'https://www.apartments.com/grand-island-fl-32735/1000-to-2000',
        'https://www.apartments.com/elizabeth-nj-07202/1000-to-2000',
        'https://www.apartments.com/wilmington-nc-28403/1000-to-2000',
        'https://www.apartments.com/providence-ri-02908/1000-to-2000',
        'https://www.apartments.com/bentonville-ar-72712/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10469/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33301/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33308/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33306/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33317/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78210/1000-to-2000',
        'https://www.apartments.com/fort-wayne-in-46806/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30087/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30088/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30032/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30083/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75249/1000-to-2000',
        'https://www.apartments.com/des-moines-ia-50317/1000-to-2000'


        
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
