import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/buffalo-ny-14211/1000-to-2000',
        'https://www.apartments.com/carteret-nj-07008/1000-to-2000',
        'https://www.apartments.com/somerset-nj-08873/1000-to-2000',
        'https://www.apartments.com/rahway-nj-07065/1000-to-2000',
        'https://www.apartments.com/new-port-richey-fl-34653/1000-to-2000',
        'https://www.apartments.com/shreveport-la-71106/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33610/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33612/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33604/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33614/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19147/1000-to-2000',
        'https://www.apartments.com/palm-desert-ca-92211/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75220/1000-to-2000',
        'https://www.apartments.com/ridgewood-ny-11385/1000-to-2000',
        'https://www.apartments.com/clarksville-tn-37040/1000-to-2000',
        'https://www.apartments.com/gadsden-al-35901/1000-to-2000',
        'https://www.apartments.com/laughlin-nv-89029/1000-to-2000',
        'https://www.apartments.com/chestnut-hill-ma-02467/1000-to-2000',
        'https://www.apartments.com/fresno-ca-93710/1000-to-2000',
        'https://www.apartments.com/fresno-ca-93730/1000-to-2000',
        'https://www.apartments.com/barstow-ca-92311/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32209/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32204/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92507/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32206/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11203/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95824/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95814/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48219/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48205/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48214/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78203/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48238/1000-to-2000',
        'https://www.apartments.com/boston-ma-02127/1000-to-2000',
        'https://www.apartments.com/pinellas-park-fl-33781/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30311/1000-to-2000',
        'https://www.apartments.com/palm-coast-fl-32137/1000-to-2000'


        
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
