import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/huntsville-al-35803/400-to-1000',
        'https://www.apartments.com/jacksonville-fl-32209/400-to-1000',
        'https://www.apartments.com/green-bay-wi-54302/320-to-838',
        'https://www.apartments.com/lumberton-nc-28360/400-to-1000',
        'https://www.apartments.com/raeford-nc-28376/1000-to-1200',
        'https://www.apartments.com/amite-la-70422/400-to-1000',
        'https://www.apartments.com/hopkinsville-ky-42240/400-to-1000',
        'https://www.apartments.com/hudson-nh-3051/560-to-1198',
        'https://www.apartments.com/asheville-nc-28804/320-to-838',
        'https://www.apartments.com/ambler-pa-19002/560-to-1198',
        'https://www.apartments.com/thomson-ga-0/400-to-1000',
        'https://www.apartments.com/nan-nan-22011/400-to-1000',
        'https://www.apartments.com/indianapolis-in-46221/320-to-838',
        'https://www.apartments.com/gadsden-al-35907/319-to-478',
        'https://www.apartments.com/port-charlotte-fl-33953/320-to-838',
        'https://www.apartments.com/manassas-va-20109/320-to-838',
        'https://www.apartments.com/nan-nan-6102/400-to-1000',
        'https://www.apartments.com/rome-ga-30161/320-to-838',
        'https://www.apartments.com/hanover-pa-17331/320-to-838',
        'https://www.apartments.com/saint-augustine-fl-32084/560-to-1198',
        'https://www.apartments.com/myrtle-beach-sc-29577/320-to-838',
        'https://www.apartments.com/brownsville-tn-38012/400-to-1000',
        'https://www.apartments.com/walkersville-md-21793/1000-to-1200',
        'https://www.apartments.com/hamilton-oh-45013/400-to-1000',
        'https://www.apartments.com/fort-lauderdale-fl-33321/1000-to-1200',
        'https://www.apartments.com/lorain-oh-44055/400-to-1000',
        'https://www.apartments.com/newton-nc-28658/320-to-838',
        'https://www.apartments.com/winder-ga-30680/400-to-1000',
        'https://www.apartments.com/birmingham-al-35209/320-to-838',
        'https://www.apartments.com/charlotte-nc-28206/400-to-1000',
        'https://www.apartments.com/philadelphia-pa-19111/1000-to-1200',
        'https://www.apartments.com/norcross-ga-30093/400-to-1000',
        'https://www.apartments.com/portsmouth-va-23703/560-to-1198',
        'https://www.apartments.com/fort-worth-tx-76179/320-to-838',
        'https://www.apartments.com/goldsboro-nc-27530/320-to-838',
        'https://www.apartments.com/reading-mi-49274/560-to-1198',
        'https://www.apartments.com/hopatcong-nj-7843/400-to-1000',
        'https://www.apartments.com/grand-rapids-mi-49507/400-to-1000',
        'https://www.apartments.com/orlando-fl-32818/400-to-1000',
        'https://www.apartments.com/binghamton-ny-13904/320-to-838',
        'https://www.apartments.com/el-monte-ca-91731/400-to-1000',
        'https://www.apartments.com/warren-mi-48091/400-to-1000',
        'https://www.apartments.com/kinston-nc-28504/320-to-838',
        'https://www.apartments.com/new-castle-in-47362/400-to-1000',
        'https://www.apartments.com/sandy-ut-84094/400-to-1000',
        'https://www.apartments.com/bonifay-fl-32425/560-to-1198',
        'https://www.apartments.com/huntsville-al-35805/400-to-1000',
        'https://www.apartments.com/elberton-ga-30635/320-to-838',
        'https://www.apartments.com/brandon-vt-5733/400-to-1000',
        'https://www.apartments.com/gallipolis-oh-45631/320-to-838',
        'https://www.apartments.com/jacksonville-fl-32205/560-to-1198',
        'https://www.apartments.com/missouri-city-tx-77489/1000-to-1200',
        'https://www.apartments.com/greensboro-nc-27455/320-to-838',
        'https://www.apartments.com/indian-orchard-ma-1151/320-to-838',
        'https://www.apartments.com/yakima-wa-98901/400-to-1000',
        'https://www.apartments.com/detroit-mi-48228/320-to-838',
        'https://www.apartments.com/maryville-tn-37801/560-to-1198',
        'https://www.apartments.com/new-castle-de-19720/400-to-1000',
        'https://www.apartments.com/greensboro-nc-27406/400-to-1000',
        'https://www.apartments.com/killeen-tx-76549/400-to-1000',
        'https://www.apartments.com/forrest-city-ar-72335/320-to-838',
        'https://www.apartments.com/indianapolis-in-46222/400-to-1000',
        'https://www.apartments.com/ashford-al-36312/400-to-1000',
        'https://www.apartments.com/saint-petersburg-fl-33713/1000-to-1200',
        'https://www.apartments.com/budd-lake-nj-7828/400-to-1000',
        'https://www.apartments.com/murrayville-ga-30564/400-to-1000',
        'https://www.apartments.com/miami-fl-33166/1000-to-1200',
        'https://www.apartments.com/galesburg-il-61401/320-to-838',
        'https://www.apartments.com/palm-bay-fl-32905/400-to-1000',
        'https://www.apartments.com/baltimore-md-21213/400-to-1000',
        'https://www.apartments.com/lorain-oh-44052/320-to-838',
        'https://www.apartments.com/monticello-in-47960/320-to-838',
        'https://www.apartments.com/kernersville-nc-27284/319-to-478',
        'https://www.apartments.com/nan-nan-96882/400-to-1000',
        'https://www.apartments.com/spokane-wa-99208/560-to-1198',
        'https://www.apartments.com/reno-nv-89502/560-to-1198',
        'https://www.apartments.com/surprise-az-85379/400-to-1000',
        'https://www.apartments.com/romeo-mi-48065/400-to-1000',
        'https://www.apartments.com/nan-nan-8/400-to-1000',
        'https://www.apartments.com/forsyth-mo-65653/560-to-1198',
        'https://www.apartments.com/louisville-ky-40216/400-to-1000',
        'https://www.apartments.com/phoenix-az-85032/400-to-1000',
        'https://www.apartments.com/modesto-ca-95354/400-to-1000',
        'https://www.apartments.com/canton-oh-44703/320-to-838',
        'https://www.apartments.com/columbus-ga-31907/560-to-1198',
        'https://www.apartments.com/martinsburg-wv-25404/1000-to-1200',
        'https://www.apartments.com/jacksonville-fl-32208/400-to-1000',
        'https://www.apartments.com/schenectady-ny-12308/1000-to-1200',
        'https://www.apartments.com/virginia-beach-va-23454/400-to-1000',
        'https://www.apartments.com/vancouver-wa-98682/560-to-1198',
        'https://www.apartments.com/duncan-ok-73533/320-to-838',
        'https://www.apartments.com/philadelphia-pa-19124/400-to-1000',
        'https://www.apartments.com/kingwood-tx-77339/320-to-838',
        'https://www.apartments.com/lake-city-fl-32024/319-to-478',
        'https://www.apartments.com/hope-mills-nc-28348/400-to-1000',
        'https://www.apartments.com/owensboro-ky-42301/319-to-478',
        'https://www.apartments.com/philadelphia-pa-19148/400-to-1000',
        'https://www.apartments.com/chester-sc-29706/320-to-838',
        'https://www.apartments.com/pottstown-pa-19464/1000-to-1200',
        'https://www.apartments.com/aberdeen-md-21001/320-to-838',
        'https://www.apartments.com/beaumont-tx-77705/1000-to-1200',
        'https://www.apartments.com/pensacola-fl-32526/400-to-1000',
        'https://www.apartments.com/fort-wayne-in-46845/560-to-1198',
        'https://www.apartments.com/dunedin-fl-34698/560-to-1198',
        'https://www.apartments.com/anniston-al-36206/400-to-1000',
        'https://www.apartments.com/sevierville-tn-37862/400-to-1000',
        'https://www.apartments.com/auburn-ny-13021/1000-to-1200',
        'https://www.apartments.com/nan-nan-1352/400-to-1000',
        'https://www.apartments.com/salt-lake-city-ut-84107/400-to-1000',
        'https://www.apartments.com/burlington-nc-27215/319-to-478',
        'https://www.apartments.com/anderson-sc-29621/320-to-838',
        'https://www.apartments.com/york-pa-17403/560-to-1198',
        'https://www.apartments.com/sarasota-fl-34234/400-to-1000',
        'https://www.apartments.com/san-francisco-ca-94102/400-to-1000',
        'https://www.apartments.com/greenville-pa-16125/1000-to-1200',
        'https://www.apartments.com/gainesville-ga-30506/320-to-838',
        'https://www.apartments.com/fayetteville-nc-28301/400-to-1000',
        'https://www.apartments.com/hillsdale-mi-49242/560-to-1198',
        'https://www.apartments.com/sulphur-la-70663/400-to-1000',
        'https://www.apartments.com/fernandina-beach-fl-32034/400-to-1000',
        'https://www.apartments.com/maxton-nc-28364/319-to-478',
        'https://www.apartments.com/anderson-sc-29625/560-to-1198',
        'https://www.apartments.com/fayetteville-nc-28312/400-to-1000',
        'https://www.apartments.com/columbia-sc-29205/400-to-1000',
        'https://www.apartments.com/bridgeport-ct-6605/400-to-1000',
        'https://www.apartments.com/manchester-tn-37355/560-to-1198',
        'https://www.apartments.com/davenport-ia-52806/560-to-1198',
        'https://www.apartments.com/elkhart-in-46514/1000-to-1200',
        'https://www.apartments.com/dubuque-ia-52001/320-to-838',
        'https://www.apartments.com/los-angeles-ca-90026/400-to-1000',
        'https://www.apartments.com/saint-louis-mo-63125/400-to-1000',
        'https://www.apartments.com/elgin-il-60120/1000-to-1200',
        'https://www.apartments.com/temple-tx-76501/400-to-1000',
        'https://www.apartments.com/oklahoma-city-ok-73159/320-to-838',
        'https://www.apartments.com/norfolk-va-23523/400-to-1000',
        'https://www.apartments.com/hickory-nc-28601/1000-to-1200',
        'https://www.apartments.com/newport-news-va-23607/400-to-1000',
        'https://www.apartments.com/cortland-oh-44410/400-to-1000',
        'https://www.apartments.com/avondale-az-85392/400-to-1000',
        'https://www.apartments.com/fountain-co-80817/560-to-1198',
        'https://www.apartments.com/tampa-fl-33615/400-to-1000',
        'https://www.apartments.com/memphis-tn-38141/400-to-1000',
        'https://www.apartments.com/clifton-co-81520/320-to-838',
        'https://www.apartments.com/tulsa-ok-74145/400-to-1000',
        'https://www.apartments.com/kingsport-tn-37660/320-to-838',
        'https://www.apartments.com/petersburg-va-23803/400-to-1000',
        'https://www.apartments.com/killeen-tx-76542/320-to-838',
        'https://www.apartments.com/williamsburg-va-23185/400-to-1000',
        'https://www.apartments.com/hacienda-heights-ca-91745/400-to-1000',
        'https://www.apartments.com/barstow-ca-92311/319-to-478',
        'https://www.apartments.com/boise-id-83704/400-to-1000',
        'https://www.apartments.com/kaneville-il-60144/400-to-1000',
        'https://www.apartments.com/council-bluffs-ia-51501/400-to-1000',
        'https://www.apartments.com/las-vegas-nv-89130/319-to-478',
        'https://www.apartments.com/springfield-oh-45504/400-to-1000',
        'https://www.apartments.com/shawnee-ks-66216/400-to-1000',
        'https://www.apartments.com/marshville-nc-28103/400-to-1000',
        'https://www.apartments.com/memphis-tn-38111/400-to-1000',
        'https://www.apartments.com/lavonia-ga-30553/400-to-1000',
        'https://www.apartments.com/greensboro-nc-27405/320-to-838',
        'https://www.apartments.com/virginia-beach-va-23462/400-to-1000',
        'https://www.apartments.com/brooksville-fl-34601/400-to-1000',
        'https://www.apartments.com/charlotte-nc-28213/400-to-1000',
        'https://www.apartments.com/venice-fl-34293/400-to-1000',
        'https://www.apartments.com/manning-sc-29102/400-to-1000',
        'https://www.apartments.com/belleview-fl-34420/400-to-1000',
        'https://www.apartments.com/lexington-ky-40504/400-to-1000',
        'https://www.apartments.com/chula-vista-ca-91910/400-to-1000',
        'https://www.apartments.com/buffalo-ny-14206/400-to-1000',
        'https://www.apartments.com/somerset-ma-2726/320-to-838',
        'https://www.apartments.com/milwaukee-wi-53204/400-to-1000',
        'https://www.apartments.com/gardena-ca-90247/400-to-1000',
        'https://www.apartments.com/los-angeles-ca-90031/1000-to-1200',
        'https://www.apartments.com/beaumont-tx-77713/560-to-1198',
        'https://www.apartments.com/winston-ga-30187/400-to-1000',
        'https://www.apartments.com/vinton-va-24179/400-to-1000',
        'https://www.apartments.com/dayton-oh-45417/400-to-1000',
        'https://www.apartments.com/austin-tx-78753/400-to-1000',
        'https://www.apartments.com/phoenix-az-85014/400-to-1000',
        'https://www.apartments.com/garner-nc-27529/400-to-1000',
        'https://www.apartments.com/joliet-il-60435/400-to-1000',
        'https://www.apartments.com/new-britain-ct-6051/1000-to-1200',
        'https://www.apartments.com/los-banos-ca-93635/560-to-1198',
        'https://www.apartments.com/alvin-tx-77511/560-to-1198',
        'https://www.apartments.com/arlington-tx-76006/320-to-838',
        'https://www.apartments.com/gwynn-oak-md-21207/400-to-1000',
        'https://www.apartments.com/hanahan-sc-29410/560-to-1198',
        'https://www.apartments.com/newport-news-va-23601/400-to-1000',
        'https://www.apartments.com/kennewick-wa-99337/400-to-1000',
        'https://www.apartments.com/seattle-wa-98168/400-to-1000',
        'https://www.apartments.com/baton-rouge-la-70802/400-to-1000',
        'https://www.apartments.com/alliance-oh-44601/320-to-838',
        'https://www.apartments.com/tucson-az-85710/400-to-1000',
        'https://www.apartments.com/buffalo-ny-14212/1000-to-1200',
        'https://www.apartments.com/easton-pa-18042/400-to-1000',
        'https://www.apartments.com/houston-tx-77066/1000-to-1200',
        'https://www.apartments.com/nan-nan-32085/400-to-1000',
        'https://www.apartments.com/lebanon-mo-65536/400-to-1000',
        'https://www.apartments.com/pleasureville-ky-40057/400-to-1000',
        'https://www.apartments.com/columbia-sc-29209/400-to-1000',
        'https://www.apartments.com/toms-river-nj-8755/560-to-1198',
        'https://www.apartments.com/shelbyville-tn-37160/400-to-1000',
        'https://www.apartments.com/visalia-ca-93291/560-to-1198',
        'https://www.apartments.com/craigsville-wv-26205/400-to-1000',
        'https://www.apartments.com/raleigh-nc-27606/400-to-1000',
        'https://www.apartments.com/idaho-falls-id-83401/400-to-1000',
        'https://www.apartments.com/clearwater-fl-33763/400-to-1000',
        'https://www.apartments.com/bronx-ny-10473/400-to-1000',
        'https://www.apartments.com/perris-ca-92571/400-to-1000',
        'https://www.apartments.com/phoenix-az-85041/400-to-1000',
        'https://www.apartments.com/seminole-fl-33772/400-to-1000',
        'https://www.apartments.com/saint-louis-mo-63136/400-to-1000',
        'https://www.apartments.com/bethlehem-pa-18015/400-to-1000',
        'https://www.apartments.com/milwaukee-wi-53208/1000-to-1200',
        'https://www.apartments.com/fort-walton-beach-fl-32548/400-to-1000',
        'https://www.apartments.com/radcliff-ky-40160/400-to-1000',
        'https://www.apartments.com/sioux-falls-sd-57104/319-to-478',
        'https://www.apartments.com/jackson-ms-39213/400-to-1000',
        'https://www.apartments.com/memphis-tn-38105/400-to-1000',
        'https://www.apartments.com/milwaukee-wi-53214/400-to-1000',
        'https://www.apartments.com/nan-nan-46093/320-to-838',
        'https://www.apartments.com/nan-nan-39207/400-to-1000',
        'https://www.apartments.com/temple-tx-76504/400-to-1000',
        'https://www.apartments.com/memphis-tn-38114/320-to-838',
        'https://www.apartments.com/clarksville-tn-37042/319-to-478',
        'https://www.apartments.com/silver-spring-md-20904/400-to-1000',
        'https://www.apartments.com/central-falls-ri-2863/560-to-1198',
        'https://www.apartments.com/lake-wales-fl-33859/400-to-1000',
        'https://www.apartments.com/brooklyn-md-21225/400-to-1000',
        'https://www.apartments.com/suitland-md-20746/400-to-1000',
        'https://www.apartments.com/augusta-ga-30907/560-to-1198',
        'https://www.apartments.com/portland-or-97206/560-to-1198',
        'https://www.apartments.com/westpoint-tn-38486/560-to-1198',
        'https://www.apartments.com/kalispell-mt-59901/400-to-1000',
        'https://www.apartments.com/colorado-springs-co-80917/400-to-1000',
        'https://www.apartments.com/flint-mi-48507/400-to-1000',
        'https://www.apartments.com/new-orleans-la-70123/400-to-1000',
        'https://www.apartments.com/miami-fl-33138/400-to-1000',
        'https://www.apartments.com/colton-ca-92324/1000-to-1200',
        'https://www.apartments.com/lees-summit-mo-64081/400-to-1000',
        'https://www.apartments.com/little-elm-tx-75068/400-to-1000',
        'https://www.apartments.com/pueblo-co-81004/320-to-838',
        'https://www.apartments.com/akron-oh-44305/400-to-1000',
        'https://www.apartments.com/north-augusta-sc-29841/400-to-1000',
        'https://www.apartments.com/pomona-ca-91766/400-to-1000',
        'https://www.apartments.com/san-diego-ca-92127/400-to-1000',
        'https://www.apartments.com/philadelphia-pa-19135/400-to-1000',
        'https://www.apartments.com/norfolk-va-23508/400-to-1000',
        'https://www.apartments.com/woodbine-ga-31569/400-to-1000',
        'https://www.apartments.com/carrollton-tx-75007/400-to-1000',
        'https://www.apartments.com/charlotte-nc-28214/400-to-1000',
        'https://www.apartments.com/salem-or-97301/400-to-1000',
        'https://www.apartments.com/lancaster-ca-93535/400-to-1000',
        'https://www.apartments.com/titus-al-36080/560-to-1198',
        'https://www.apartments.com/passaic-nj-7055/319-to-478',
        'https://www.apartments.com/homestead-fl-33034/319-to-478',
        'https://www.apartments.com/nan-nan-41105/400-to-1000',
        'https://www.apartments.com/port-arthur-tx-77640/400-to-1000',
        'https://www.apartments.com/oakland-ca-94621/400-to-1000',
        'https://www.apartments.com/sacramento-ca-95823/1000-to-1200',
        'https://www.apartments.com/blaine-wa-98230/400-to-1000',
        'https://www.apartments.com/anchorage-ak-99502/1000-to-1200',
        'https://www.apartments.com/manzanola-co-81058/400-to-1000',
        'https://www.apartments.com/fort-lauderdale-fl-33311/400-to-1000'

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
