import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/silver-spring-md-20902/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33614/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76116/1000-to-2000',
        'https://www.apartments.com/mooresville-nc-28125/1000-to-2000',
        'https://www.apartments.com/sarasota-fl-34239/1000-to-2000',
        'https://www.apartments.com/round-rock-tx-78681/1000-to-2000',
        'https://www.apartments.com/prescott-valley-az-86314/1000-to-2000',
        'https://www.apartments.com/sanford-nc-27332/1000-to-2000',
        'https://www.apartments.com/parkville-md-21234/1000-to-2000',
        'https://www.apartments.com/milpitas-ca-95035/1000-to-2000',
        'https://www.apartments.com/hayward-ca-94541/1000-to-2000',
        'https://www.apartments.com/clifton-heights-pa-19018/1000-to-2000',
        'https://www.apartments.com/oxnard-ca-93030/1000-to-2000',
        'https://www.apartments.com/columbia-sc-29201/1000-to-2000',
        'https://www.apartments.com/the-colony-tx-75056/1000-to-2000',
        'https://www.apartments.com/ridgewood-ny-11385/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11208/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43206/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38116/1000-to-2000',
        'https://www.apartments.com/columbia-sc-29205/1000-to-2000',
        'https://www.apartments.com/columbia-sc-29223/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32835/1000-to-2000',
        'https://www.apartments.com/brandon-fl-33510/1000-to-2000',
        'https://www.apartments.com/winter-park-fl-32792/1000-to-2000',
        'https://www.apartments.com/rego-park-ny-11374/1000-to-2000',
        'https://www.apartments.com/jamaica-ny-11435/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11235/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85020/1000-to-2000',
        'https://www.apartments.com/murfreesboro-tn-37127/1000-to-2000',
        'https://www.apartments.com/longmont-co-80501/1000-to-2000',
        'https://www.apartments.com/temecula-ca-92591/1000-to-2000',
        'https://www.apartments.com/king-of-prussia-pa-19406/1000-to-2000',
        'https://www.apartments.com/mesquite-tx-75150/1000-to-2000',
        'https://www.apartments.com/naples-fl-34104/1000-to-2000',
        'https://www.apartments.com/youngstown-oh-44502/1000-to-2000',
        'https://www.apartments.com/port-charlotte-fl-33952/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32811/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33619/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90063/1000-to-2000',
        'https://www.apartments.com/durham-nc-27707/1000-to-2000',
        'https://www.apartments.com/durham-nc-27713/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32209/1000-to-2000',
        'https://www.apartments.com/bloomingdale-il-60108/1000-to-2000',
        'https://www.apartments.com/cedar-falls-ia-50613/1000-to-2000',
        'https://www.apartments.com/new-york-ny-10034/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19134/1000-to-2000',
        'https://www.apartments.com/west-palm-beach-fl-33417/1000-to-2000',
        'https://www.apartments.com/clearwater-fl-33756/1000-to-2000',
        'https://www.apartments.com/clearwater-fl-33760/1000-to-2000',
        'https://www.apartments.com/clearwater-fl-33762/1000-to-2000',
        'https://www.apartments.com/santa-monica-ca-90401/1000-to-2000',
        'https://www.apartments.com/santa-monica-ca-90404/1000-to-2000',
        'https://www.apartments.com/mcdonough-ga-30253/1000-to-2000',
        'https://www.apartments.com/columbus-ga-31904/1000-to-2000'



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
