import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/lubbock-tx-79401/1000-to-2000',
        'https://www.apartments.com/zanesville-oh-43701/1000-to-2000',
        'https://www.apartments.com/joliet-il-60433/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95815/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95814/1000-to-2000',
        'https://www.apartments.com/muskego-wi-53150/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53218/1000-to-2000',
        'https://www.apartments.com/dayton-oh-45410/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19103/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19146/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19115/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19147/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19145/1000-to-2000',
        'https://www.apartments.com/middletown-de-19709/1000-to-2000',
        'https://www.apartments.com/stamford-ct-06902/1000-to-2000',
        'https://www.apartments.com/west-palm-beach-fl-33417/1000-to-2000',
        'https://www.apartments.com/valdosta-ga-31605/1000-to-2000',
        'https://www.apartments.com/mount-vernon-ny-10552/1000-to-2000',
        'https://www.apartments.com/kansas-city-ks-66101/1000-to-2000',
        'https://www.apartments.com/austin-tx-78745/1000-to-2000',
        'https://www.apartments.com/amarillo-tx-79106/1000-to-2000',
        'https://www.apartments.com/tulsa-ok-74105/1000-to-2000',
        'https://www.apartments.com/west-columbia-sc-29172/1000-to-2000',
        'https://www.apartments.com/hollywood-fl-33019/1000-to-2000',
        'https://www.apartments.com/lubbock-tx-79410/1000-to-2000',
        'https://www.apartments.com/lubbock-tx-79413/1000-to-2000',
        'https://www.apartments.com/leominster-ma-01453/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28205/1000-to-2000',
        'https://www.apartments.com/downey-ca-90242/1000-to-2000',
        'https://www.apartments.com/downey-ca-90241/1000-to-2000',
        'https://www.apartments.com/lithonia-ga-30038/1000-to-2000',
        'https://www.apartments.com/jacksonville-nc-28546/1000-to-2000',
        'https://www.apartments.com/jacksonville-nc-28540/1000-to-2000',
        'https://www.apartments.com/midlothian-tx-76065/1000-to-2000',
        'https://www.apartments.com/jamaica-ny-11433/1000-to-2000',
        'https://www.apartments.com/jamaica-ny-11432/1000-to-2000',
        'https://www.apartments.com/jamaica-ny-11434/1000-to-2000',
        'https://www.apartments.com/knoxville-tn-37916/1000-to-2000',
        'https://www.apartments.com/coconut-creek-fl-33066/1000-to-2000',
        'https://www.apartments.com/rancho-cordova-ca-95670/1000-to-2000',
        'https://www.apartments.com/fair-oaks-ca-95628/1000-to-2000',
        'https://www.apartments.com/largo-fl-33773/1000-to-2000',
        'https://www.apartments.com/antelope-ca-95843/1000-to-2000',
        'https://www.apartments.com/west-sacramento-ca-95605/1000-to-2000',
        'https://www.apartments.com/carmichael-ca-95608/1000-to-2000',
        'https://www.apartments.com/citrus-heights-ca-95621/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85015/1000-to-2000',
        'https://www.apartments.com/gainesville-fl-32608/1000-to-2000',
        'https://www.apartments.com/patchogue-ny-11772/1000-to-2000',
        'https://www.apartments.com/conyers-ga-30013/1000-to-2000',
        'https://www.apartments.com/newark-nj-07102/1000-to-2000',
        'https://www.apartments.com/newark-nj-07103/1000-to-2000'

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
