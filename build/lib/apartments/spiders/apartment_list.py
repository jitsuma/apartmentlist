import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/los-angeles-ca-90063/1000-to-2000',
        'https://www.apartments.com/cherry-hill-nj-08034/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19145/1000-to-2000',
        'https://www.apartments.com/twin-falls-id-83301/1000-to-2000',
        'https://www.apartments.com/greensboro-nc-27405/1000-to-2000',
        'https://www.apartments.com/victorville-ca-92392/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37212/1000-to-2000',
        'https://www.apartments.com/victorville-ca-92394/1000-to-2000',
        'https://www.apartments.com/lexington-park-md-20653/1000-to-2000',
        'https://www.apartments.com/newark-nj-07104/1000-to-2000',
        'https://www.apartments.com/newark-nj-07103/1000-to-2000',
        'https://www.apartments.com/san-jacinto-ca-92582/1000-to-2000',
        'https://www.apartments.com/waretown-nj-08758/1000-to-2000',
        'https://www.apartments.com/manahawkin-nj-08050/1000-to-2000',
        'https://www.apartments.com/elmhurst-ny-11373/1000-to-2000',
        'https://www.apartments.com/buffalo-ny-14216/1000-to-2000',
        'https://www.apartments.com/glendale-az-85302/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/buffalo-ny-14211/1000-to-2000',
        'https://www.apartments.com/tucson-az-85745/1000-to-2000',
        'https://www.apartments.com/tucson-az-85705/1000-to-2000',
        'https://www.apartments.com/hollywood-fl-33020/1000-to-2000',
        'https://www.apartments.com/cuyahoga-falls-oh-44223/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33624/1000-to-2000',
        'https://www.apartments.com/auburn-wa-98002/1000-to-2000',
        'https://www.apartments.com/gastonia-nc-28054/1000-to-2000',
        'https://www.apartments.com/covington-ga-30014/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33617/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33619/1000-to-2000',
        'https://www.apartments.com/haverhill-ma-01830/1000-to-2000',
        'https://www.apartments.com/haverhill-ma-01832/1000-to-2000',
        'https://www.apartments.com/kansas-city-mo-64123/1000-to-2000',
        'https://www.apartments.com/morrow-ga-30260/1000-to-2000',
        'https://www.apartments.com/boynton-beach-fl-33435/1000-to-2000',
        'https://www.apartments.com/yeadon-pa-19050/1000-to-2000',
        'https://www.apartments.com/akron-oh-44305/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30046/1000-to-2000',
        'https://www.apartments.com/florissant-mo-63033/1000-to-2000',
        'https://www.apartments.com/birmingham-al-35212/1000-to-2000',
        'https://www.apartments.com/duluth-ga-30096/1000-to-2000',
        'https://www.apartments.com/hazelwood-mo-63042/1000-to-2000',
        'https://www.apartments.com/florissant-mo-63031/1000-to-2000',
        'https://www.apartments.com/morris-il-60450/1000-to-2000',
        'https://www.apartments.com/capitol-heights-md-20743/1000-to-2000',
        'https://www.apartments.com/district-heights-md-20747/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33611/1000-to-2000',
        'https://www.apartments.com/silver-spring-md-20902/1000-to-2000',
        'https://www.apartments.com/laurel-md-20707/1000-to-2000',
        'https://www.apartments.com/hyattsville-md-20782/1000-to-2000',
        'https://www.apartments.com/columbia-mo-65201/1000-to-2000',
        'https://www.apartments.com/columbia-mo-65202/1000-to-2000'


        
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
