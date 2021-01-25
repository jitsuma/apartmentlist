import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/athens-ga-30607/1000-to-2000',
        'https://www.apartments.com/monroe-ga-30655/1000-to-2000',
        'https://www.apartments.com/commerce-ga-30529/1000-to-2000',
        'https://www.apartments.com/monroe-ga-30656/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46219/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21206/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21223/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21214/1000-to-2000',
        'https://www.apartments.com/chicago-il-60619/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21216/1000-to-2000',
        'https://www.apartments.com/bedford-oh-44146/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53215/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19134/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19131/1000-to-2000',
        'https://www.apartments.com/lakeland-fl-33801/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45213/1000-to-2000',
        'https://www.apartments.com/lakewood-wa-98498/1000-to-2000',
        'https://www.apartments.com/beaumont-ca-92223/1000-to-2000',
        'https://www.apartments.com/salem-or-97304/1000-to-2000',
        'https://www.apartments.com/corvallis-or-97330/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38127/1000-to-2000',
        'https://www.apartments.com/joliet-il-60431/1000-to-2000',
        'https://www.apartments.com/greenville-nc-27858/1000-to-2000',
        'https://www.apartments.com/brookhaven-pa-19015/1000-to-2000',
        'https://www.apartments.com/warrensburg-mo-64093/1000-to-2000',
        'https://www.apartments.com/lakewood-oh-44107/1000-to-2000',
        'https://www.apartments.com/knob-noster-mo-65336/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28215/1000-to-2000',
        'https://www.apartments.com/hackensack-nj-07601/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90029/1000-to-2000',
        'https://www.apartments.com/cherry-hill-nj-08034/1000-to-2000',
        'https://www.apartments.com/university-park-il-60484/1000-to-2000',
        'https://www.apartments.com/homestead-fl-33035/1000-to-2000',
        'https://www.apartments.com/richmond-va-23219/1000-to-2000',
        'https://www.apartments.com/jersey-city-nj-07302/1000-to-2000',
        'https://www.apartments.com/san-diego-ca-92104/1000-to-2000',
        'https://www.apartments.com/hampton-va-23666/1000-to-2000',
        'https://www.apartments.com/lakeland-fl-33810/1000-to-2000',
        'https://www.apartments.com/kansas-city-mo-64123/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85017/1000-to-2000',
        'https://www.apartments.com/mesa-az-85201/1000-to-2000',
        'https://www.apartments.com/tempe-az-85281/1000-to-2000',
        'https://www.apartments.com/scottsdale-az-85250/1000-to-2000',
        'https://www.apartments.com/mesa-az-85204/1000-to-2000',
        'https://www.apartments.com/glendale-az-85302/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75215/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75216/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75227/1000-to-2000',
        'https://www.apartments.com/garland-tx-75040/1000-to-2000',
        'https://www.apartments.com/plano-tx-75074/1000-to-2000'

        
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
