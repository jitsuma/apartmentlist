import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/atlanta-ga-30316/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23502/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23503/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23518/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23513/1000-to-2000',
        'https://www.apartments.com/new-haven-ct-06511/1000-to-2000',
        'https://www.apartments.com/waterbury-ct-06702/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11208/1000-to-2000',
        'https://www.apartments.com/merced-ca-95348/1000-to-2000',
        'https://www.apartments.com/capitol-heights-md-20743/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76107/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76109/1000-to-2000',
        'https://www.apartments.com/new-britain-ct-06051/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38106/1000-to-2000',
        'https://www.apartments.com/rochester-ny-14607/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90029/1000-to-2000',
        'https://www.apartments.com/torrance-ca-90501/1000-to-2000',
        'https://www.apartments.com/garden-grove-ca-92841/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32218/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32209/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90802/1000-to-2000',
        'https://www.apartments.com/huntington-beach-ca-92649/1000-to-2000',
        'https://www.apartments.com/pomona-ca-91766/1000-to-2000',
        'https://www.apartments.com/louisville-ky-40214/1000-to-2000',
        'https://www.apartments.com/louisville-ky-40206/1000-to-2000',
        'https://www.apartments.com/louisville-ky-40216/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30311/1000-to-2000',
        'https://www.apartments.com/noblesville-in-46060/1000-to-2000',
        'https://www.apartments.com/bradenton-fl-34207/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43205/1000-to-2000',
        'https://www.apartments.com/high-point-nc-27265/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43229/1000-to-2000',
        'https://www.apartments.com/la-crosse-wi-54601/1000-to-2000',
        'https://www.apartments.com/bakersfield-ca-93309/1000-to-2000',
        'https://www.apartments.com/bakersfield-ca-93305/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30309/1000-to-2000',
        'https://www.apartments.com/anderson-in-46016/1000-to-2000',
        'https://www.apartments.com/anderson-in-46012/1000-to-2000',
        'https://www.apartments.com/largo-fl-33773/1000-to-2000',
        'https://www.apartments.com/rahway-nj-07065/1000-to-2000',
        'https://www.apartments.com/charleston-sc-29414/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19147/1000-to-2000',
        'https://www.apartments.com/colton-ca-92324/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92503/1000-to-2000',
        'https://www.apartments.com/highland-ca-92346/1000-to-2000',
        'https://www.apartments.com/ontario-ca-91764/1000-to-2000',
        'https://www.apartments.com/redlands-ca-92373/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92507/1000-to-2000',
        'https://www.apartments.com/san-bernardino-ca-92404/1000-to-2000',
        'https://www.apartments.com/san-bernardino-ca-92410/1000-to-2000',
        'https://www.apartments.com/jamaica-ny-11434/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11203/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85051/1000-to-2000',
        'https://www.apartments.com/lithonia-ga-30058/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11235/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30032/1000-to-2000',
        'https://www.apartments.com/knoxville-tn-37916/1000-to-2000',
        'https://www.apartments.com/ridgewood-ny-11385/1000-to-2000'

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
