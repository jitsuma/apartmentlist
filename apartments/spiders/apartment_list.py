import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/vancouver-wa-98661/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75220/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75216/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75208/1000-to-2000',
        'https://www.apartments.com/canton-ga-30115/1000-to-2000',
        'https://www.apartments.com/cicero-il-60804/1000-to-2000',
        'https://www.apartments.com/chicago-il-60619/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21217/1000-to-2000',
        'https://www.apartments.com/colorado-springs-co-80910/1000-to-2000',
        'https://www.apartments.com/portland-or-97233/1000-to-2000',
        'https://www.apartments.com/anaheim-ca-92801/1000-to-2000',
        'https://www.apartments.com/anaheim-ca-92805/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30088/1000-to-2000',
        'https://www.apartments.com/litchfield-park-az-85340/1000-to-2000',
        'https://www.apartments.com/goodyear-az-85338/1000-to-2000',
        'https://www.apartments.com/dolton-il-60419/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48228/1000-to-2000',
        'https://www.apartments.com/mishawaka-in-46545/1000-to-2000',
        'https://www.apartments.com/richmond-va-23223/1000-to-2000',
        'https://www.apartments.com/colonial-heights-va-23834/1000-to-2000',
        'https://www.apartments.com/little-rock-ar-72206/1000-to-2000',
        'https://www.apartments.com/avondale-az-85392/1000-to-2000',
        'https://www.apartments.com/mansfield-ma-02048/1000-to-2000',
        'https://www.apartments.com/youngstown-oh-44509/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32208/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32202/1000-to-2000',
        'https://www.apartments.com/altamonte-springs-fl-32714/1000-to-2000',
        'https://www.apartments.com/washington-dc-20012/1000-to-2000',
        'https://www.apartments.com/altamonte-springs-fl-32701/1000-to-2000',
        'https://www.apartments.com/longwood-fl-32779/1000-to-2000',
        'https://www.apartments.com/avondale-az-85323/1000-to-2000',
        'https://www.apartments.com/albany-ga-31707/1000-to-2000',
        'https://www.apartments.com/north-attleboro-ma-02760/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85020/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85015/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85022/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37211/1000-to-2000'

        
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
