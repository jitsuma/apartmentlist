import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/elkhart-in-46514/1000-to-2000',
        'https://www.apartments.com/broken-arrow-ok-74012/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30043/1000-to-2000',
        'https://www.apartments.com/barberton-oh-44203/1000-to-2000',
        'https://www.apartments.com/warner-robins-ga-31093/1000-to-2000',
        'https://www.apartments.com/greenville-nc-27834/1000-to-2000',
        'https://www.apartments.com/carrollton-ga-30117/1000-to-2000',
        'https://www.apartments.com/north-las-vegas-nv-89032/1000-to-2000',
        'https://www.apartments.com/greensboro-nc-27405/1000-to-2000',
        'https://www.apartments.com/portsmouth-va-23704/1000-to-2000',
        'https://www.apartments.com/noble-ok-73068/1000-to-2000',
        'https://www.apartments.com/pittsburgh-pa-15233/1000-to-2000',
        'https://www.apartments.com/palm-bay-fl-32905/1000-to-2000',
        'https://www.apartments.com/seabrook-nh-03874/1000-to-2000',
        'https://www.apartments.com/augusta-me-04330/1000-to-2000',
        'https://www.apartments.com/fayetteville-nc-28311/1000-to-2000',
        'https://www.apartments.com/savannah-tn-38372/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19111/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75211/1000-to-2000',
        'https://www.apartments.com/decatur-ga-30034/1000-to-2000',
        'https://www.apartments.com/salem-ar-72576/1000-to-2000',
        'https://www.apartments.com/anna-il-62906/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21213/1000-to-2000',
        'https://www.apartments.com/starke-fl-32091/1000-to-2000',
        'https://www.apartments.com/chilhowie-va-24319/1000-to-2000',
        'https://www.apartments.com/clinton-md-20735/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43223/1000-to-2000',
        'https://www.apartments.com/pleasantville-ny-10570/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46268/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76116/1000-to-2000',
        'https://www.apartments.com/goodyear-az-85338/1000-to-2000',
        'https://www.apartments.com/ware-ma-01082/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32809/1000-to-2000',
        'https://www.apartments.com/baldwyn-ms-38824/1000-to-2000',
        'https://www.apartments.com/lake-city-fl-32024/1000-to-2000',
        'https://www.apartments.com/rockmart-ga-30153/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32808/1000-to-2000',
        'https://www.apartments.com/harrisburg-pa-17110/1000-to-2000',
        'https://www.apartments.com/wilmington-de-19805/1000-to-2000',
        'https://www.apartments.com/chester-va-23831/1000-to-2000',
        'https://www.apartments.com/bradenton-fl-34205/1000-to-2000',
        'https://www.apartments.com/allentown-pa-18102/1000-to-2000',
        'https://www.apartments.com/athens-ga-30606/1000-to-2000',
        'https://www.apartments.com/merced-ca-95341/1000-to-2000',
        'https://www.apartments.com/oxford-nc-27565/1000-to-2000',
        'https://www.apartments.com/stockbridge-ga-30281/1000-to-2000',
        'https://www.apartments.com/phenix-city-al-36870/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32209/1000-to-2000',
        'https://www.apartments.com/norfolk-va-23507/1000-to-2000',
        'https://www.apartments.com/syracuse-ny-13204/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30314/1000-to-2000',
        'https://www.apartments.com/sun-city-az-85351/1000-to-2000',
        'https://www.apartments.com/coventry-ri-02816/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46208/1000-to-2000',
        'https://www.apartments.com/southgate-mi-48195/1000-to-2000',
        'https://www.apartments.com/loves-park-il-61111/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53202/1000-to-2000',
        'https://www.apartments.com/lewisville-tx-75067/1000-to-2000',
        'https://www.apartments.com/theodore-al-36582/1000-to-2000',
        'https://www.apartments.com/york-pa-17404/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85029/1000-to-2000',
        'https://www.apartments.com/memphis-tn-38104/1000-to-2000',
        'https://www.apartments.com/cary-nc-27518/1000-to-2000',
        'https://www.apartments.com/kansas-city-mo-64105/1000-to-2000',
        'https://www.apartments.com/fresno-ca-93702/1000-to-2000',
        'https://www.apartments.com/onalaska-wa-98570/1000-to-2000',
        'https://www.apartments.com/macon-ga-31206/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30310/1000-to-2000',
        'https://www.apartments.com/linwood-mi-48634/1000-to-2000',
        'https://www.apartments.com/caneyville-ky-42721/1000-to-2000',
        'https://www.apartments.com/glendale-az-85301/1000-to-2000',
        'https://www.apartments.com/winchester-va-22601/1000-to-2000',
        'https://www.apartments.com/merrill-wi-54452/1000-to-2000',
        'https://www.apartments.com/anderson-sc-29624/1000-to-2000',
        'https://www.apartments.com/west-monroe-la-71292/1000-to-2000',
        'https://www.apartments.com/grand-rapids-mi-49548/1000-to-2000',
        'https://www.apartments.com/montgomery-al-36111/1000-to-2000',
        'https://www.apartments.com/greensburg-in-47240/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75240/1000-to-2000',
        'https://www.apartments.com/east-saint-louis-il-62201/1000-to-2000',
        'https://www.apartments.com/detroit-mi-48238/1000-to-2000',
        'https://www.apartments.com/henderson-nv-89044/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85053/1000-to-2000',
        'https://www.apartments.com/homestead-fl-33030/1000-to-2000',
        'https://www.apartments.com/springfield-gardens-ny-11413/1000-to-2000',
        'https://www.apartments.com/palermo-ca-95968/1000-to-2000',
        'https://www.apartments.com/yuma-az-85364/1000-to-2000',
        'https://www.apartments.com/goshen-oh-45122/1000-to-2000',
        'https://www.apartments.com/garland-tx-75043/1000-to-2000',
        'https://www.apartments.com/chicago-il-60653/1000-to-2000',
        'https://www.apartments.com/hamtramck-mi-48212/1000-to-2000',
        'https://www.apartments.com/hamilton-oh-45011/1000-to-2000',
        'https://www.apartments.com/hyattsville-md-20783/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33616/1000-to-2000',
        'https://www.apartments.com/greensboro-nc-27407/1000-to-2000',
        'https://www.apartments.com/altus-ok-73521/1000-to-2000',
        'https://www.apartments.com/erie-pa-16509/1000-to-2000',
        'https://www.apartments.com/riverside-nj-08075/1000-to-2000',
        'https://www.apartments.com/beaumont-tx-77703/1000-to-2000',
        'https://www.apartments.com/fontana-ca-92337/1000-to-2000',
        'https://www.apartments.com/umatilla-fl-32784/1000-to-2000',
        'https://www.apartments.com/hallandale-fl-33009/1000-to-2000',
        'https://www.apartments.com/peoria-il-61605/1000-to-2000',
        'https://www.apartments.com/fort-wayne-in-46802/1000-to-2000',
        'https://www.apartments.com/oklahoma-city-ok-73106/1000-to-2000',
        'https://www.apartments.com/sanford-fl-32771/1000-to-2000',
        'https://www.apartments.com/san-dimas-ca-91773/1000-to-2000',
        'https://www.apartments.com/birmingham-al-35228/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33612/1000-to-2000',
        'https://www.apartments.com/cayce-sc-29033/1000-to-2000',
        'https://www.apartments.com/los-lunas-nm-87031/1000-to-2000',
        'https://www.apartments.com/houston-tx-77088/1000-to-2000',
        'https://www.apartments.com/atlanta-ga-30318/1000-to-2000',
        'https://www.apartments.com/indianola-il-61850/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10455/1000-to-2000',
        'https://www.apartments.com/lincoln-ne-68510/1000-to-2000',
        'https://www.apartments.com/locust-grove-ga-30248/1000-to-2000',
        'https://www.apartments.com/norwalk-ca-90650/1000-to-2000',
        'https://www.apartments.com/aurora-or-97002/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92503/1000-to-2000',
        'https://www.apartments.com/dayton-oh-45420/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85022/1000-to-2000',
        'https://www.apartments.com/warsaw-in-46580/1000-to-2000',
        'https://www.apartments.com/austin-tx-78728/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92504/1000-to-2000',
        'https://www.apartments.com/farmer-city-il-61842/1000-to-2000',
        'https://www.apartments.com/fort-myers-fl-33908/1000-to-2000',
        'https://www.apartments.com/harrison-mi-48625/1000-to-2000',
        'https://www.apartments.com/pinellas-park-fl-33781/1000-to-2000',
        'https://www.apartments.com/ecorse-mi-48229/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33605/1000-to-2000',
        'https://www.apartments.com/dayton-oh-45405/1000-to-2000',
        'https://www.apartments.com/griffin-ga-30223/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44109/1000-to-2000',
        'https://www.apartments.com/lawrenceville-ga-30046/1000-to-2000',
        'https://www.apartments.com/brockton-ma-02301/1000-to-2000',
        'https://www.apartments.com/clearwater-fl-33759/1000-to-2000',
        'https://www.apartments.com/clinton-township-mi-48038/1000-to-2000',
        'https://www.apartments.com/greenville-sc-29605/1000-to-2000',
        'https://www.apartments.com/dallas-tx-75243/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33313/1000-to-2000',
        'https://www.apartments.com/nan-nan-74102/1000-to-2000',
        'https://www.apartments.com/cookeville-tn-38501/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89121/1000-to-2000',
        'https://www.apartments.com/oswego-il-60543/1000-to-2000',
        'https://www.apartments.com/howard-beach-ny-11414/1000-to-2000',
        'https://www.apartments.com/grand-saline-tx-75140/1000-to-2000',
        'https://www.apartments.com/newport-news-va-23601/1000-to-2000',
        'https://www.apartments.com/tulsa-ok-74115/1000-to-2000',
        'https://www.apartments.com/alton-il-62002/1000-to-2000',
        'https://www.apartments.com/new-port-richey-fl-34653/1000-to-2000',
        'https://www.apartments.com/san-diego-ca-92105/1000-to-2000',
        'https://www.apartments.com/nashville-tn-37207/1000-to-2000',
        'https://www.apartments.com/jackson-ms-39212/1000-to-2000',
        'https://www.apartments.com/boaz-al-35956/1000-to-2000',
        'https://www.apartments.com/sand-springs-ok-74063/1000-to-2000',
        'https://www.apartments.com/springdale-pa-15144/1000-to-2000',
        'https://www.apartments.com/tucson-az-85745/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43211/1000-to-2000',
        'https://www.apartments.com/springfield-or-97477/1000-to-2000',
        'https://www.apartments.com/connellsville-pa-15425/1000-to-2000',
        'https://www.apartments.com/stuart-fl-34996/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95823/1000-to-2000',
        'https://www.apartments.com/harper-woods-mi-48225/1000-to-2000',
        'https://www.apartments.com/dublin-ga-31021/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32277/1000-to-2000',
        'https://www.apartments.com/clinton-mo-64735/1000-to-2000',
        'https://www.apartments.com/chandler-az-85249/1000-to-2000',
        'https://www.apartments.com/terre-haute-in-47802/1000-to-2000',
        'https://www.apartments.com/amarillo-tx-79109/1000-to-2000',
        'https://www.apartments.com/hot-springs-national-park-ar-71913/1000-to-2000',
        'https://www.apartments.com/tacoma-wa-98422/1000-to-2000',
        'https://www.apartments.com/franklin-tn-37064/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90011/1000-to-2000',
        'https://www.apartments.com/richardson-tx-75080/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46222/1000-to-2000',
        'https://www.apartments.com/pomona-ca-91766/1000-to-2000',
        'https://www.apartments.com/lancaster-ca-93534/1000-to-2000',
        'https://www.apartments.com/winston-salem-nc-27127/1000-to-2000',
        'https://www.apartments.com/deerfield-beach-fl-33441/1000-to-2000',
        'https://www.apartments.com/hartselle-al-35640/1000-to-2000',
        'https://www.apartments.com/clearwater-fl-33765/1000-to-2000',
        'https://www.apartments.com/campbell-ca-95008/1000-to-2000',
        'https://www.apartments.com/chandler-in-47610/1000-to-2000',
        'https://www.apartments.com/oklahoma-city-ok-73149/1000-to-2000',
        'https://www.apartments.com/farmington-nm-87401/1000-to-2000',
        'https://www.apartments.com/tyler-tx-75707/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45214/1000-to-2000',
        'https://www.apartments.com/charleston-wv-25306/1000-to-2000',
        'https://www.apartments.com/savannah-ga-31415/1000-to-2000',
        'https://www.apartments.com/joelton-tn-37080/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89147/1000-to-2000',
        'https://www.apartments.com/garland-tx-75040/1000-to-2000',
        'https://www.apartments.com/omaha-ne-68102/1000-to-2000',
        'https://www.apartments.com/meriden-ct-06450/1000-to-2000',
        'https://www.apartments.com/vero-beach-fl-32960/1000-to-2000',
        'https://www.apartments.com/wilson-nc-27893/1000-to-2000',
        'https://www.apartments.com/bakersfield-ca-93305/1000-to-2000',
        'https://www.apartments.com/inman-sc-29349/1000-to-2000',
        'https://www.apartments.com/desoto-tx-75115/1000-to-2000',
        'https://www.apartments.com/ingleside-tx-78362/1000-to-2000',
        'https://www.apartments.com/tuscaloosa-al-35405/1000-to-2000',
        'https://www.apartments.com/huffman-tx-77336/1000-to-2000',
        'https://www.apartments.com/frederick-md-21702/1000-to-2000',
        'https://www.apartments.com/san-bernardino-ca-92410/1000-to-2000',
        'https://www.apartments.com/shawnee-ok-74804/1000-to-2000',
        'https://www.apartments.com/jamaica-ny-11434/1000-to-2000',
        'https://www.apartments.com/kingston-tn-37763/1000-to-2000',
        'https://www.apartments.com/jacksonville-beach-fl-32250/1000-to-2000',
        'https://www.apartments.com/riverview-fl-33578/1000-to-2000',
        'https://www.apartments.com/paramount-ca-90723/1000-to-2000',
        'https://www.apartments.com/warner-robins-ga-31088/1000-to-2000',
        'https://www.apartments.com/washington-pa-15301/1000-to-2000',
        'https://www.apartments.com/red-bluff-ca-96080/1000-to-2000',
        'https://www.apartments.com/north-royalton-oh-44133/1000-to-2000',
        'https://www.apartments.com/middletown-va-22645/1000-to-2000',
        'https://www.apartments.com/elizabethtown-ky-42701/1000-to-2000',
        'https://www.apartments.com/desert-hot-springs-ca-92240/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85028/1000-to-2000',
        'https://www.apartments.com/pasadena-ca-91104/1000-to-2000',
        'https://www.apartments.com/catasauqua-pa-18032/1000-to-2000',
        'https://www.apartments.com/bronx-ny-10469/1000-to-2000',
        'https://www.apartments.com/statesboro-ga-30458/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43213/1000-to-2000',
        'https://www.apartments.com/saint-petersburg-fl-33714/1000-to-2000',
        'https://www.apartments.com/dayton-oh-45417/1000-to-2000',
        'https://www.apartments.com/plant-city-fl-33563/1000-to-2000',
        'https://www.apartments.com/riverside-ca-92507/1000-to-2000',
        'https://www.apartments.com/dothan-al-36303/1000-to-2000',
        'https://www.apartments.com/red-oak-ia-51566/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46237/1000-to-2000',
        'https://www.apartments.com/nan-nan-891**/1000-to-2000',
        'https://www.apartments.com/reno-nv-89512/1000-to-2000',
        'https://www.apartments.com/columbia-sc-29229/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19132/1000-to-2000',
        'https://www.apartments.com/chicago-il-60628/1000-to-2000',
        'https://www.apartments.com/gastonia-nc-28056/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78230/1000-to-2000',
        'https://www.apartments.com/lutz-fl-33549/1000-to-2000',
        'https://www.apartments.com/milwaukee-wi-53215/1000-to-2000',
        'https://www.apartments.com/mountville-pa-17554/1000-to-2000',
        'https://www.apartments.com/pekin-il-61554/1000-to-2000',
        'https://www.apartments.com/apex-nc-27523/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44118/1000-to-2000',
        'https://www.apartments.com/albuquerque-nm-87114/1000-to-2000',
        'https://www.apartments.com/magee-ms-39111/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78209/1000-to-2000',
        'https://www.apartments.com/ocoee-fl-34761/1000-to-2000',
        'https://www.apartments.com/columbus-oh-43205/1000-to-2000',
        'https://www.apartments.com/youngstown-oh-44505/1000-to-2000',
        'https://www.apartments.com/miami-fl-33147/1000-to-2000',
        'https://www.apartments.com/fort-myers-fl-33912/1000-to-2000',
        'https://www.apartments.com/sandusky-oh-44870/1000-to-2000',
        'https://www.apartments.com/lagrange-ga-30240/1000-to-2000',
        'https://www.apartments.com/belton-mo-64012/1000-to-2000',
        'https://www.apartments.com/weirton-wv-26062/1000-to-2000',
        'https://www.apartments.com/ephrata-pa-17522/1000-to-2000',
        'https://www.apartments.com/palm-harbor-fl-34684/1000-to-2000',
        'https://www.apartments.com/norfolk-ne-68701/1000-to-2000',
        'https://www.apartments.com/manteca-ca-95337/1000-to-2000',
        'https://www.apartments.com/birmingham-al-35214/1000-to-2000',
        'https://www.apartments.com/estero-fl-33928/1000-to-2000',
        'https://www.apartments.com/nan-nan-74388/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44134/1000-to-2000',
        'https://www.apartments.com/los-angeles-ca-90002/1000-to-2000',
        'https://www.apartments.com/pompano-beach-fl-33068/1000-to-2000'

        
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
