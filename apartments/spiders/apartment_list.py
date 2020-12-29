import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/austin-tx-78745/1000-to-2000',
        'https://www.apartments.com/san-jose-ca-95125/1000-to-2000',
        'https://www.apartments.com/milpitas-ca-95035/1000-to-2000',
        'https://www.apartments.com/chico-ca-95926/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53204/1000-to-2000',
        'https://www.apartments.com/lake-wales-fl-33898/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37203/1000-to-2000',
        'https://www.apartments.com/wichita-ks-67208/1000-to-2000',
        'https://www.apartments.com/lakewood-wa-98499/1000-to-2000',
        'https://www.apartments.com/marysville-ca-95901/1000-to-2000',
        'https://www.apartments.com/kent-wa-98032/1000-to-2000',
        'https://www.apartments.com/waite-park-mn-56387/1000-to-2000',
        'https://www.apartments.com/seattle-wa-98105/1000-to-2000',
        'https://www.apartments.com/brooksville-fl-34601/1000-to-2000',
        'https://www.apartments.com/spring-hill-fl-34610/1000-to-2000',
        'https://www.apartments.com/austin-tx-78704/1000-to-2000',
        'https://www.apartments.com/austin-tx-78757/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30046/1000-to-2000',
        'https://www.apartments.com/west-sacramento-ca-95605/1000-to-2000',
        'https://www.apartments.com/woodland-ca-95695/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21217/1000-to-2000',
        'https://www.apartments.com/manhattan-ny-10017/1000-to-2000',
        'https://www.apartments.com/tucson-az-85712/1000-to-2000',
        'https://www.apartments.com/kansas-city-mo-64131/1000-to-2000',
        'https://www.apartments.com/portsmouth-va-23702/1000-to-2000',
        'https://www.apartments.com/odenton-md-21113/1000-to-2000',
        'https://www.apartments.com/miami-fl-33175/1000-to-2000',
        'https://www.apartments.com/miami-fl-33138/1000-to-2000',
        'https://www.apartments.com/spring-hill-fl-34608/1000-to-2000',
        'https://www.apartments.com/fremont-ca-94538/1000-to-2000',
        'https://www.apartments.com/manhattan-ny-10036/1000-to-2000',
        'https://www.apartments.com/manhattan-ny-10002/1000-to-2000',
        'https://www.apartments.com/manhattan-ny-10128/1000-to-2000',
        'https://www.apartments.com/manhattan-ny-10021/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78203/1000-to-2000',
        'https://www.apartments.com/burlington-nc-27217/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44113/1000-to-2000',
        'https://www.apartments.com/cedar-grove-nc-27231/1000-to-2000',
        'https://www.apartments.com/buffalo-ny-14216/1000-to-2000',
        'https://www.apartments.com/black-mountain-nc-28711/1000-to-2000',
        'https://www.apartments.com/greensboro-nc-27405/1000-to-2000'


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
