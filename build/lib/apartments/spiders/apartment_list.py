import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']

    start_urls = [
        'https://www.apartments.com/chula-vista-ca-91910/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95814/1000-to-2000',
        'https://www.apartments.com/pompano-beach-fl-33069/1000-to-2000',
        'https://www.apartments.com/brea-ca-92821/1000-to-2000',
        'https://www.apartments.com/rowland-heights-ca-91748/1000-to-2000',
        'https://www.apartments.com/redding-ca-96001/1000-to-2000',
        'https://www.apartments.com/lake-worth-fl-33467/1000-to-2000',
        'https://www.apartments.com/lake-worth-fl-33462/1000-to-2000',
        'https://www.apartments.com/redlands-ca-92374/1000-to-2000',
        'https://www.apartments.com/colton-ca-92324/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90063/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89156/1000-to-2000',
        'https://www.apartments.com/mesa-az-85210/1000-to-2000',
        'https://www.apartments.com/desoto-tx-75115/1000-to-2000',
        'https://www.apartments.com/cherry-hill-nj-08034/1000-to-2000',
        'https://www.apartments.com/flushing-ny-11358/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11203/1000-to-2000',
        'https://www.apartments.com/mcdonough-ga-30253/1000-to-2000',
        'https://www.apartments.com/burnsville-mn-55337/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75208/1000-to-2000',
        'https://www.apartments.com/miami-fl-33144/1000-to-2000',
        'https://www.apartments.com/new-port-richey-fl-34653/1000-to-2000',
        'https://www.apartments.com/chicago-il-60613/1000-to-2000',
        'https://www.apartments.com/chicago-il-60640/1000-to-2000',
        'https://www.apartments.com/upland-ca-91786/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30316/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30311/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32224/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32209/1000-to-2000',
        'https://www.apartments.com/chicago-il-60619/1000-to-2000',
        'https://www.apartments.com/tallahassee-fl-32304/1000-to-2000',
        'https://www.apartments.com/fort-wayne-in-46804/1000-to-2000',
        'https://www.apartments.com/new-port-richey-fl-34654/1000-to-2000',
        'https://www.apartments.com/calumet-city-il-60409/1000-to-2000',
        'https://www.apartments.com/hollywood-fl-33020/1000-to-2000'


    ]

    def parse(self, response):
        print("procesing:"+response.url)
        #Extract data using css selectors
        address=response.xpath("//div[@class='location']/text()").extract()
        phone_number=response.xpath("//div[@class='phone']/span/text()").extract()
        link_url=response.xpath("//div[@class='placardContainer']//li//article//@data-url").extract()

        row_data=zip(address,phone_number,link_url)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'address' : item[0], #item[0] means product in the list and so on, index tells what value to assign
                'phone_number' : item[1],
                'link_url' : item[2]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
