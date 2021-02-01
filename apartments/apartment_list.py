import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/charlotte-nc-28205/1000-to-2000',
        'https://www.apartments.com/colton-ca-92324/1000-to-2000',
        'https://www.apartments.com/woodland-ca-95695/1000-to-2000',
        'https://www.apartments.com/west-sacramento-ca-95605/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48234/1000-to-2000',
        'https://www.apartments.com/madison-heights-mi-48071/1000-to-2000',
        'https://www.apartments.com/hickory-nc-28601/1000-to-2000',
        'https://www.apartments.com/chattanooga-tn-37412/1000-to-2000',
        'https://www.apartments.com/akron-oh-44305/1000-to-2000',
        'https://www.apartments.com/smyrna-ga-30080/1000-to-2000',
        'https://www.apartments.com/oklahoma-city-ok-73127/1000-to-2000',
        'https://www.apartments.com/tucson-az-85705/1000-to-2000',
        'https://www.apartments.com/tucson-az-85719/1000-to-2000',
        'https://www.apartments.com/port-saint-lucie-fl-34986/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33613/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33605/1000-to-2000',
        'https://www.apartments.com/jackson-ms-39216/1000-to-2000',
        'https://www.apartments.com/azusa-ca-91702/1000-to-2000',
        'https://www.apartments.com/fort-pierce-fl-34982/1000-to-2000',
        'https://www.apartments.com/greeley-co-80634/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33308/1000-to-2000',
        'https://www.apartments.com/belmar-nj-07719/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46201/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85020/1000-to-2000',
        'https://www.apartments.com/brooksville-fl-34601/1000-to-2000',
        'https://www.apartments.com/kingsport-tn-37664/1000-to-2000',
        'https://www.apartments.com/newport-news-va-23607/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44109/1000-to-2000',
        'https://www.apartments.com/long-beach-ca-90804/1000-to-2000',
        'https://www.apartments.com/san-francisco-ca-94103/1000-to-2000',
        'https://www.apartments.com/ponchatoula-la-70454/1000-to-2000',
        'https://www.apartments.com/tickfaw-la-70466/1000-to-2000',
        'https://www.apartments.com/taylor-mi-48180/1000-to-2000',
        'https://www.apartments.com/allen-park-mi-48101/1000-to-2000',
        'https://www.apartments.com/highland-mi-48357/1000-to-2000',
        'https://www.apartments.com/san-diego-ca-92106/1000-to-2000',
        'https://www.apartments.com/san-diego-ca-92116/1000-to-2000',
        'https://www.apartments.com/san-diego-ca-92103/1000-to-2000',
        'https://www.apartments.com/san-diego-ca-92102/1000-to-2000',
        'https://www.apartments.com/akron-oh-44313/1000-to-2000',
        'https://www.apartments.com/durham-nc-27713/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30032/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30035/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30030/1000-to-2000',
        'https://www.apartments.com/union-city-ga-30291/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30308/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30339/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30309/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30316/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30311/1000-to-2000'


        
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
