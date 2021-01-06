import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/nashville-tn-37216/1000-to-2000',
        'https://www.apartments.com/westfield-in-46074/1000-to-2000',
        'https://www.apartments.com/noblesville-in-46062/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37203/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37212/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37211/1000-to-2000',
        'https://www.apartments.com/chicago-il-60619/1000-to-2000',
        'https://www.apartments.com/brooklyn-ny-11203/1000-to-2000',
        'https://www.apartments.com/washington-nc-27889/1000-to-2000',
        'https://www.apartments.com/stone-mountain-ga-30083/1000-to-2000',
        'https://www.apartments.com/rancho-cucamonga-ca-91730/1000-to-2000',
        'https://www.apartments.com/queens-village-ny-11428/1000-to-2000',
        'https://www.apartments.com/ocala-fl-34470/1000-to-2000',
        'https://www.apartments.com/saint-petersburg-fl-33705/1000-to-2000',
        'https://www.apartments.com/pomona-ca-91766/1000-to-2000',
        'https://www.apartments.com/calumet-city-il-60409/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23518/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23504/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23509/1000-to-2000',
        'https://www.apartments.com/upper-marlboro-md-20774/1000-to-2000',
        'https://www.apartments.com/virginia-beach-va-23453/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10467/1000-to-2000',
        'https://www.apartments.com/newport-news-va-23608/1000-to-2000',
        'https://www.apartments.com/albuquerque-nm-87106/1000-to-2000',
        'https://www.apartments.com/scranton-pa-18504/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30349/1000-to-2000',
        'https://www.apartments.com/albany-ny-12210/1000-to-2000',
        'https://www.apartments.com/wilmington-de-19806/1000-to-2000',
        'https://www.apartments.com/wilmington-de-19805/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33614/1000-to-2000',
        'https://www.apartments.com/bradenton-fl-34207/1000-to-2000',
        'https://www.apartments.com/bartow-fl-33830/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32209/1000-to-2000',
        'https://www.apartments.com/metairie-la-70001/1000-to-2000',
        'https://www.apartments.com/wrentham-ma-02093/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45229/1000-to-2000',
        'https://www.apartments.com/springfield-oh-45503/1000-to-2000',
        'https://www.apartments.com/staten-island-ny-10312/1000-to-2000'
        

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
