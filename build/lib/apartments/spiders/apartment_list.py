import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/newark-nj-7108/400-to-1000',
        'https://www.apartments.com/athens-tn-37303/319-to-478',
        'https://www.apartments.com/naples-tx-75568/400-to-1000',
        'https://www.apartments.com/milwaukee-wi-53209/400-to-1000',
        'https://www.apartments.com/gastonia-nc-28052/400-to-1000',
        'https://www.apartments.com/paterson-nj-0/400-to-1000',
        'https://www.apartments.com/latrobe-pa-15650/320-to-838',
        'https://www.apartments.com/aztec-nm-87410/560-to-1198',
        'https://www.apartments.com/fort-lauderdale-fl-33311/400-to-1000',
        'https://www.apartments.com/bronx-ny-10468/400-to-1000',
        'https://www.apartments.com/cedar-hill-tx-75104/400-to-1000',
        'https://www.apartments.com/milton-pa-17847/320-to-838',
        'https://www.apartments.com/belmont-nc-28012/1000-to-1200',
        'https://www.apartments.com/payette-id-83661/400-to-1000',
        'https://www.apartments.com/lansing-mi-48910/320-to-838',
        'https://www.apartments.com/springfield-oh-45506/400-to-1000',
        'https://www.apartments.com/montgomery-al-36108/320-to-838',
        'https://www.apartments.com/vicksburg-ms-39183/320-to-838',
        'https://www.apartments.com/dayton-oh-45429/1000-to-1200',
        'https://www.apartments.com/decatur-al-35603/320-to-838',
        'https://www.apartments.com/racine-wi-53406/320-to-838',
        'https://www.apartments.com/toledo-oh-43612/400-to-1000',
        'https://www.apartments.com/elgin-sc-29045/320-to-838',
        'https://www.apartments.com/melbourne-fl-32940/400-to-1000',
        'https://www.apartments.com/san-luis-obispo-ca-93401/320-to-838',
        'https://www.apartments.com/charlotte-nc-28206/400-to-1000',
        'https://www.apartments.com/saint-petersburg-fl-33711/400-to-1000',
        'https://www.apartments.com/houston-tx-77034/319-to-478',
        'https://www.apartments.com/davison-mi-48423/400-to-1000',
        'https://www.apartments.com/san-antonio-tx-78249/400-to-1000',
        'https://www.apartments.com/san-jose-ca-95131/320-to-838',
        'https://www.apartments.com/kenner-la-70062/400-to-1000',
        'https://www.apartments.com/baltimore-md-21215/400-to-1000',
        'https://www.apartments.com/cocoa-fl-32922/400-to-1000',
        'https://www.apartments.com/indianapolis-in-46241/400-to-1000',
        'https://www.apartments.com/canton-oh-44707/400-to-1000',
        'https://www.apartments.com/manchester-ky-40962/400-to-1000',
        'https://www.apartments.com/newnan-ga-30263/400-to-1000',
        'https://www.apartments.com/bentonville-ar-72712/400-to-1000',
        'https://www.apartments.com/huntington-wv-25701/400-to-1000',
        'https://www.apartments.com/columbia-sc-29210/400-to-1000',
        'https://www.apartments.com/merrill-wi-54452/560-to-1198',
        'https://www.apartments.com/cleveland-oh-44109/560-to-1198',
        'https://www.apartments.com/jacksonville-fl-32210/400-to-1000',
        'https://www.apartments.com/memphis-tn-38116/400-to-1000',
        'https://www.apartments.com/chicago-il-60620/400-to-1000',
        'https://www.apartments.com/dalton-ga-30720/400-to-1000',
        'https://www.apartments.com/monticello-ar-71655/319-to-478',
        'https://www.apartments.com/ecorse-mi-48229/320-to-838',
        'https://www.apartments.com/lakewood-wa-98499/400-to-1000',
        'https://www.apartments.com/baltimore-md-21218/400-to-1000',
        'https://www.apartments.com/bridgeport-ct-6610/400-to-1000',
        'https://www.apartments.com/hattiesburg-ms-39401/400-to-1000',
        'https://www.apartments.com/nan-nan-76320/320-to-838',
        'https://www.apartments.com/brandon-fl-33510/400-to-1000',
        'https://www.apartments.com/lenoir-city-tn-37771/320-to-838',
        'https://www.apartments.com/mesa-az-85207/400-to-1000',
        'https://www.apartments.com/brandon-fl-33511/400-to-1000',
        'https://www.apartments.com/lake-charles-la-70607/400-to-1000',
        'https://www.apartments.com/columbus-oh-43213/320-to-838',
        'https://www.apartments.com/chalmette-la-70043/1000-to-1200',
        'https://www.apartments.com/cincinnati-oh-45227/400-to-1000',
        'https://www.apartments.com/saint-louis-mo-63125/400-to-1000',
        'https://www.apartments.com/lansing-mi-48911/400-to-1000',
        'https://www.apartments.com/ogden-ut-84404/560-to-1198',
        'https://www.apartments.com/huntington-beach-ca-92648/400-to-1000',
        'https://www.apartments.com/lansing-mi-48917/560-to-1198',
        'https://www.apartments.com/redding-ca-96001/400-to-1000',
        'https://www.apartments.com/chesterton-in-46304/400-to-1000',
        'https://www.apartments.com/syracuse-ny-13203/400-to-1000',
        'https://www.apartments.com/lawrence-ks-66046/320-to-838',
        'https://www.apartments.com/jacksonville-fl-32244/400-to-1000',
        'https://www.apartments.com/albuquerque-nm-87108/400-to-1000',
        'https://www.apartments.com/wilkes-barre-pa-18706/400-to-1000',
        'https://www.apartments.com/winton-ca-95388/400-to-1000',
        'https://www.apartments.com/orlando-fl-32825/320-to-838',
        'https://www.apartments.com/delaware-oh-43015/319-to-478',
        'https://www.apartments.com/fultondale-al-35068/400-to-1000',
        'https://www.apartments.com/sebring-fl-33870/1000-to-1200',
        'https://www.apartments.com/hermitage-tn-37076/400-to-1000',
        'https://www.apartments.com/fort-myers-fl-33913/319-to-478',
        'https://www.apartments.com/rich-hill-mo-64779/320-to-838',
        'https://www.apartments.com/cleveland-oh-44105/400-to-1000',
        'https://www.apartments.com/greenville-sc-29611/400-to-1000',
        'https://www.apartments.com/baltimore-md-21217/400-to-1000',
        'https://www.apartments.com/chesapeake-va-23320/400-to-1000',
        'https://www.apartments.com/newton-nj-7860/319-to-478',
        'https://www.apartments.com/punta-gorda-fl-33980/400-to-1000',
        'https://www.apartments.com/lithonia-ga-30038/320-to-838',
        'https://www.apartments.com/fountain-co-80817/400-to-1000',
        'https://www.apartments.com/baltimore-md-21224/400-to-1000',
        'https://www.apartments.com/wallingford-ct-6492/400-to-1000',
        'https://www.apartments.com/dallas-tx-75228/560-to-1198',
        'https://www.apartments.com/kinston-nc-28501/400-to-1000',
        'https://www.apartments.com/edinburg-tx-78542/560-to-1198',
        'https://www.apartments.com/canton-oh-44714/400-to-1000',
        'https://www.apartments.com/kalispell-mt-59901/319-to-478',
        'https://www.apartments.com/pico-rivera-ca-90660/1000-to-1200',
        'https://www.apartments.com/saint-louis-mo-63136/320-to-838',
        'https://www.apartments.com/little-elm-tx-75068/400-to-1000',
        'https://www.apartments.com/pocola-ok-74902/400-to-1000',
        'https://www.apartments.com/bellport-ny-11713/400-to-1000',
        'https://www.apartments.com/cape-may-court-house-nj-8210/320-to-838',
        'https://www.apartments.com/peoria-az-85382/400-to-1000',
        'https://www.apartments.com/richmond-va-23223/400-to-1000',
        'https://www.apartments.com/oroville-ca-95966/1000-to-1200',
        'https://www.apartments.com/lansing-mi-48906/400-to-1000',
        'https://www.apartments.com/washington-pa-15301/560-to-1198',
        'https://www.apartments.com/orlando-fl-32810/400-to-1000',
        'https://www.apartments.com/newark-de-19702/400-to-1000',
        'https://www.apartments.com/norcross-ga-30092/1000-to-1200',
        'https://www.apartments.com/mansfield-ma-2048/560-to-1198'


        
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
