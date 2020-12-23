import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/warren-oh-44485/1000-to-2000',
        'https://www.apartments.com/portland-or-97210/1000-to-2000',
        'https://www.apartments.com/chicago-il-60619/1000-to-2000',
        'https://www.apartments.com/brooklyn-park-mn-55443/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19134/1000-to-2000',
        'https://www.apartments.com/brooklyn-park-mn-55428/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11218/1000-to-2000',
        'https://www.apartments.com/jamaica-ny-11432/1000-to-2000',
        'https://www.apartments.com/calexico-ca-92231/1000-to-2000',
        'https://www.apartments.com/clarkston-ga-30021/1000-to-2000',
        'https://www.apartments.com/lakeland-fl-33805/1000-to-2000',
        'https://www.apartments.com/santa-clarita-ca-91321/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19147/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30316/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46201/1000-to-2000',
        'https://www.apartments.com/union-city-ga-30291/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78207/1000-to-2000',
        'https://www.apartments.com/clinton-township-mi-48038/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19131/1000-to-2000',
        'https://www.apartments.com/columbia-sc-29201/1000-to-2000',
        'https://www.apartments.com/tulsa-ok-74105/1000-to-2000',
        'https://www.apartments.com/tulsa-ok-74133/1000-to-2000',
        'https://www.apartments.com/pomona-ca-91767/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90804/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28205/1000-to-2000',
        'https://www.apartments.com/louisville-ky-40216/1000-to-2000',
        'https://www.apartments.com/west-new-york-nj-07093/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44119/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46226/1000-to-2000',
        'https://www.apartments.com/hiram-ga-30141/1000-to-2000',
        'https://www.apartments.com/mableton-ga-30126/1000-to-2000',
        'https://www.apartments.com/ozone-park-ny-11416/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45208/1000-to-2000',
        'https://www.apartments.com/eden-nc-27288/1000-to-2000',
        'https://www.apartments.com/houston-tx-77477/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33614/1000-to-2000',
        'https://www.apartments.com/fraser-mi-48026/1000-to-2000',
        'https://www.apartments.com/sterling-heights-mi-48312/1000-to-2000'


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
