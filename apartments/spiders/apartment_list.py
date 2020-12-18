import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/long-beach-ca-90804/1000-to-2000',
        'https://www.apartments.com/saint-clair-shores-mi-48080/1000-to-2000',
        'https://www.apartments.com/bellmawr-nj-08031/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53216/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53215/1000-to-2000',
        'https://www.apartments.com/albuquerque-nm-87107/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78239/1000-to-2000',
        'https://www.apartments.com/mesa-az-85203/1000-to-2000',
        'https://www.apartments.com/parma-oh-44130/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78223/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78212/1000-to-2000',
        'https://www.apartments.com/parma-oh-44134/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78210/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19134/1000-to-2000',
        'https://www.apartments.com/rochester-ny-14607/1000-to-2000',
        'https://www.apartments.com/parma-oh-44129/1000-to-2000',
        'https://www.apartments.com/rochester-ny-14608/1000-to-2000',
        'https://www.apartments.com/decatur-al-35603/1000-to-2000',
        'https://www.apartments.com/rochester-ny-14613/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53204/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28277/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90813/1000-to-2000',
        'https://www.apartments.com/miami-fl-33179/1000-to-2000',
        'https://www.apartments.com/riverview-fl-33569/1000-to-2000',
        'https://www.apartments.com/valrico-fl-33594/1000-to-2000',
        'https://www.apartments.com/birmingham-al-35226/1000-to-2000',
        'https://www.apartments.com/birmingham-al-35212/1000-to-2000',
        'https://www.apartments.com/gainesville-ga-30504/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11220/1000-to-2000',
        'https://www.apartments.com/riverdale-ga-30296/1000-to-2000',
        'https://www.apartments.com/riverdale-ga-30274/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11211/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11235/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11203/1000-to-2000',
        'https://www.apartments.com/athens-oh-45701/1000-to-2000',
        'https://www.apartments.com/bradenton-fl-34207/1000-to-2000',
        'https://www.apartments.com/newport-news-va-23602/1000-to-2000',
        'https://www.apartments.com/newport-news-va-23608/1000-to-2000',
        'https://www.apartments.com/newport-news-va-23607/1000-to-2000',
        'https://www.apartments.com/erie-pa-16502/1000-to-2000',
        'https://www.apartments.com/harrisburg-pa-17103/1000-to-2000',
        'https://www.apartments.com/concord-nc-28027/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38127/1000-to-2000',
        'https://www.apartments.com/irvington-nj-07111/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30316/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30308/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30339/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30311/1000-to-2000',
        'https://www.apartments.com/ocala-fl-34470/1000-to-2000',
        'https://www.apartments.com/myrtle-beach-sc-29572/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28208/1000-to-2000',
        'https://www.apartments.com/concord-nc-28025/1000-to-2000'


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
