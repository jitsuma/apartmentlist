import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/tucson-az-85716/1000-to-2000',
        'https://www.apartments.com/victorville-ca-92394/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48223/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48205/1000-to-2000',
        'https://www.apartments.com/harrisburg-pa-17103/1000-to-2000',
        'https://www.apartments.com/irvine-ca-92612/1000-to-2000',
        'https://www.apartments.com/visalia-ca-93277/1000-to-2000',
        'https://www.apartments.com/laughlin-nv-89029/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89156/1000-to-2000',
        'https://www.apartments.com/vancouver-wa-98661/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92507/1000-to-2000',
        'https://www.apartments.com/kissimmee-fl-34741/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95824/1000-to-2000',
        'https://www.apartments.com/maple-shade-nj-08052/1000-to-2000',
        'https://www.apartments.com/prescott-valley-az-86314/1000-to-2000',
        'https://www.apartments.com/tarpon-springs-fl-34689/1000-to-2000',
        'https://www.apartments.com/alton-il-62002/1000-to-2000',
        'https://www.apartments.com/laurel-md-20708/1000-to-2000',
        'https://www.apartments.com/spartanburg-sc-29306/1000-to-2000',
        'https://www.apartments.com/cherry-hill-nj-08034/1000-to-2000',
        'https://www.apartments.com/brighton-il-62012/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38127/1000-to-2000',
        'https://www.apartments.com/frankston-tx-75763/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11216/1000-to-2000',
        'https://www.apartments.com/ridgewood-ny-11385/1000-to-2000',
        'https://www.apartments.com/lithonia-ga-30058/1000-to-2000',
        'https://www.apartments.com/akron-oh-44311/1000-to-2000',
        'https://www.apartments.com/akron-oh-44301/1000-to-2000',
        'https://www.apartments.com/akron-oh-44314/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11203/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46201/1000-to-2000',
        'https://www.apartments.com/houston-tx-77477/1000-to-2000',
        'https://www.apartments.com/gainesville-ga-30504/1000-to-2000',
        'https://www.apartments.com/gainesville-ga-30507/1000-to-2000',
        'https://www.apartments.com/gainesville-ga-30501/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30046/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30044/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30043/1000-to-2000'

        
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
