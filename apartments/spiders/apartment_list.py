import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/reseda-ca-91335/1000-to-2000',
        'https://www.apartments.com/ventura-ca-93001/1000-to-2000',
        'https://www.apartments.com/midland-tx-79706/1000-to-2000',
        'https://www.apartments.com/canoga-park-ca-91304/1000-to-2000',
        'https://www.apartments.com/santa-clarita-ca-91321/1000-to-2000',
        'https://www.apartments.com/newbury-park-ca-91320/1000-to-2000',
        'https://www.apartments.com/thousand-oaks-ca-91360/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44110/1000-to-2000',
        'https://www.apartments.com/oxnard-ca-93030/1000-to-2000',
        'https://www.apartments.com/ontario-ca-91764/1000-to-2000',
        'https://www.apartments.com/pomona-ca-91766/1000-to-2000',
        'https://www.apartments.com/hawthorne-ca-90250/1000-to-2000',
        'https://www.apartments.com/pensacola-fl-32506/1000-to-2000',
        'https://www.apartments.com/richmond-va-23223/1000-to-2000',
        'https://www.apartments.com/fort-wayne-in-46806/1000-to-2000',
        'https://www.apartments.com/elk-grove-ca-95624/1000-to-2000',
        'https://www.apartments.com/oakland-ca-94619/1000-to-2000',
        'https://www.apartments.com/raleigh-nc-27603/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90063/1000-to-2000',
        'https://www.apartments.com/lakeport-ca-95451/1000-to-2000',
        'https://www.apartments.com/providence-ri-02908/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10471/1000-to-2000',
        'https://www.apartments.com/houston-tx-77082/1000-to-2000',
        'https://www.apartments.com/houston-tx-77057/1000-to-2000',
        'https://www.apartments.com/houston-tx-77021/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75241/1000-to-2000',
        'https://www.apartments.com/houston-tx-77091/1000-to-2000',
        'https://www.apartments.com/houston-tx-77036/1000-to-2000',
        'https://www.apartments.com/johnson-city-tn-37604/1000-to-2000',
        'https://www.apartments.com/kingsport-tn-37664/1000-to-2000',
        'https://www.apartments.com/douglasville-ga-30135/1000-to-2000',
        'https://www.apartments.com/watsonville-ca-95076/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45229/1000-to-2000',
        'https://www.apartments.com/huntington-wv-25703/1000-to-2000',
        'https://www.apartments.com/cherry-hill-nj-08034/1000-to-2000',
        'https://www.apartments.com/huntington-wv-25701/1000-to-2000',
        'https://www.apartments.com/huntington-wv-25702/1000-to-2000',
        'https://www.apartments.com/miami-fl-33144/1000-to-2000',
        'https://www.apartments.com/lombard-il-60148/1000-to-2000',
        'https://www.apartments.com/austin-tx-78745/1000-to-2000',
        'https://www.apartments.com/long-branch-nj-07740/1000-to-2000',
        'https://www.apartments.com/decatur-al-35603/1000-to-2000',
        'https://www.apartments.com/florissant-mo-63031/1000-to-2000',
        'https://www.apartments.com/daytona-beach-fl-32118/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32805/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23503/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23513/1000-to-2000',
        'https://www.apartments.com/chesapeake-va-23325/1000-to-2000',
        'https://www.apartments.com/chesapeake-va-23324/1000-to-2000',
        'https://www.apartments.com/burleson-tx-76028/1000-to-2000',
        'https://www.apartments.com/chicago-il-60619/1000-to-2000',
        'https://www.apartments.com/winston-salem-nc-27106/1000-to-2000',
        'https://www.apartments.com/winston-salem-nc-27101/1000-to-2000',
        'https://www.apartments.com/jacksonville-nc-28546/1000-to-2000',
        'https://www.apartments.com/pineville-nc-28134/1000-to-2000'



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
