import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/maryland-heights-mo-63043/1000-to-2000',
        'https://www.apartments.com/bridgeton-mo-63044/1000-to-2000',
        'https://www.apartments.com/bayonne-nj-07002/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53204/1000-to-2000',
        'https://www.apartments.com/perry-ga-31069/1000-to-2000',
        'https://www.apartments.com/lake-worth-fl-33463/1000-to-2000',
        'https://www.apartments.com/lake-worth-fl-33467/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32246/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90063/1000-to-2000',
        'https://www.apartments.com/salisbury-nc-28144/1000-to-2000',
        'https://www.apartments.com/columbia-sc-29205/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85022/1000-to-2000',
        'https://www.apartments.com/longview-tx-75605/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92507/1000-to-2000',
        'https://www.apartments.com/bolingbrook-il-60440/1000-to-2000',
        'https://www.apartments.com/lake-dallas-tx-75065/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90804/1000-to-2000',
        'https://www.apartments.com/far-rockaway-ny-11691/1000-to-2000',
        'https://www.apartments.com/hollywood-fl-33020/1000-to-2000',
        'https://www.apartments.com/clearwater-fl-33761/1000-to-2000',
        'https://www.apartments.com/kennesaw-ga-30144/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30311/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75208/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30339/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30350/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85020/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37212/1000-to-2000',
        'https://www.apartments.com/petersburg-va-23805/1000-to-2000',
        'https://www.apartments.com/spring-tx-77379/1000-to-2000',
        'https://www.apartments.com/ridgewood-ny-11385/1000-to-2000',
        'https://www.apartments.com/new-haven-ct-06511/1000-to-2000',
        'https://www.apartments.com/newark-nj-07106/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37207/1000-to-2000',
        'https://www.apartments.com/mishawaka-in-46545/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48221/1000-to-2000'

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
