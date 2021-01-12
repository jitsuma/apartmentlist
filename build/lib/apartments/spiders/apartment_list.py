import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/milwaukee-wi-53225/1000-to-2000',
        'https://www.apartments.com/louisville-ky-40291/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90017/1000-to-2000',
        'https://www.apartments.com/normal-il-61761/1000-to-2000',
        'https://www.apartments.com/rochester-ny-14613/1000-to-2000',
        'https://www.apartments.com/decatur-al-35603/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30311/1000-to-2000',
        'https://www.apartments.com/college-park-ga-30349/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76105/1000-to-2000',
        'https://www.apartments.com/mobile-al-36608/1000-to-2000',
        'https://www.apartments.com/east-point-ga-30344/1000-to-2000',
        'https://www.apartments.com/buford-ga-30519/1000-to-2000',
        'https://www.apartments.com/clarksville-tn-37043/1000-to-2000',
        'https://www.apartments.com/clarksville-tn-37042/1000-to-2000',
        'https://www.apartments.com/clarksville-tn-37040/1000-to-2000',
        'https://www.apartments.com/upper-darby-pa-19082/1000-to-2000',
        'https://www.apartments.com/mishawaka-in-46545/1000-to-2000',
        'https://www.apartments.com/louisville-ky-40203/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45205/1000-to-2000',
        'https://www.apartments.com/chicago-il-60609/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19131/1000-to-2000',
        'https://www.apartments.com/chicago-il-60617/1000-to-2000',
        'https://www.apartments.com/zion-il-60099/1000-to-2000',
        'https://www.apartments.com/madera-ca-93638/1000-to-2000',
        'https://www.apartments.com/valdosta-ga-31602/1000-to-2000',
        'https://www.apartments.com/valdosta-ga-31601/1000-to-2000',
        'https://www.apartments.com/bloomington-il-61704/1000-to-2000',
        'https://www.apartments.com/leesburg-fl-34748/1000-to-2000',
        'https://www.apartments.com/palm-desert-ca-92260/1000-to-2000',
        'https://www.apartments.com/euclid-oh-44132/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75229/1000-to-2000',
        'https://www.apartments.com/fayetteville-nc-28311/1000-to-2000',
        'https://www.apartments.com/statesville-nc-28677/1000-to-2000',
        'https://www.apartments.com/conway-ar-72032/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90804/1000-to-2000',
        'https://www.apartments.com/highland-park-mi-48203/1000-to-2000',
        'https://www.apartments.com/sarasota-fl-34239/1000-to-2000',
        'https://www.apartments.com/lake-mary-fl-32746/1000-to-2000',
        'https://www.apartments.com/waterford-mi-48328/1000-to-2000',
        'https://www.apartments.com/harrisburg-pa-17103/1000-to-2000',
        'https://www.apartments.com/fairfield-ct-06824/1000-to-2000',
        'https://www.apartments.com/florence-ky-41042/1000-to-2000'


        
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
