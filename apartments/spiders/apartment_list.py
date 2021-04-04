import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/manassas-va-20109/1000-to-1200',
        'https://www.apartments.com/reidsville-nc-0/400-to-1000',
        'https://www.apartments.com/fraser-mi-48026/320-to-838',
        'https://www.apartments.com/la-verne-ca-91750/320-to-838',
        'https://www.apartments.com/memphis-tn-38116/320-to-838',
        'https://www.apartments.com/fairfield-oh-45014/320-to-838',
        'https://www.apartments.com/dallas-tx-75231/320-to-838',
        'https://www.apartments.com/dallas-tx-75241/1000-to-1200',
        'https://www.apartments.com/mission-ks-66202/560-to-1198',
        'https://www.apartments.com/virginia-beach-va-23456/320-to-838',
        'https://www.apartments.com/jacksonville-nc-28546/560-to-1198',
        'https://www.apartments.com/kingsport-tn-37660/319-to-478',
        'https://www.apartments.com/fleming-island-fl-32003/560-to-1198',
        'https://www.apartments.com/harriman-tn-37748/320-to-838',
        'https://www.apartments.com/kansas-city-mo-64153/560-to-1198',
        'https://www.apartments.com/auburn-wa-98001/1000-to-1200',
        'https://www.apartments.com/moreno-valley-ca-92553/320-to-838',
        'https://www.apartments.com/jamaica-ny-11432/320-to-838',
        'https://www.apartments.com/columbus-ga-31907/320-to-838',
        'https://www.apartments.com/lagrange-ga-30240/320-to-838',
        'https://www.apartments.com/san-fernando-ca-91340/560-to-1198',
        'https://www.apartments.com/lexington-ky-40508/320-to-838',
        'https://www.apartments.com/newport-news-va-23607/1000-to-1200',
        'https://www.apartments.com/santa-fe-nm-87506/560-to-1198',
        'https://www.apartments.com/marion-oh-43302/320-to-838',
        'https://www.apartments.com/jeffersonville-in-47130/560-to-1198',
        'https://www.apartments.com/winchester-va-22602/320-to-838',
        'https://www.apartments.com/chicago-il-60625/320-to-838',
        'https://www.apartments.com/mesa-az-85201/1000-to-1200',
        'https://www.apartments.com/oshkosh-wi-54902/320-to-838',
        'https://www.apartments.com/spokane-wa-99208/560-to-1198',
        'https://www.apartments.com/comer-ga-30629/560-to-1198',
        'https://www.apartments.com/nan-nan-99240/560-to-1198',
        'https://www.apartments.com/conway-ar-72034/560-to-1198',
        'https://www.apartments.com/oakwood-va-24631/319-to-478',
        'https://www.apartments.com/las-vegas-nv-89141/560-to-1198',
        'https://www.apartments.com/mesa-az-85208/560-to-1198',
        'https://www.apartments.com/nan-nan-36331/560-to-1198',
        'https://www.apartments.com/mableton-ga-30126/320-to-838',
        'https://www.apartments.com/hartselle-al-35640/319-to-478',
        'https://www.apartments.com/newark-nj-7104/560-to-1198',
        'https://www.apartments.com/kissimmee-fl-34743/319-to-478',
        'https://www.apartments.com/south-hill-va-23970/560-to-1198',
        'https://www.apartments.com/schertz-tx-78154/560-to-1198',
        'https://www.apartments.com/grand-prairie-tx-75052/560-to-1198',
        'https://www.apartments.com/augusta-ga-30907/560-to-1198',
        'https://www.apartments.com/clarksville-tn-37042/320-to-838',
        'https://www.apartments.com/ferndale-ca-95536/320-to-838',
        'https://www.apartments.com/venice-fl-34293/1000-to-1200',
        'https://www.apartments.com/milford-ct-6460/319-to-478',
        'https://www.apartments.com/west-palm-beach-fl-33406/320-to-838',
        'https://www.apartments.com/bethune-sc-29009/320-to-838',
        'https://www.apartments.com/ozark-ar-72949/320-to-838',
        'https://www.apartments.com/abilene-tx-79603/320-to-838',
        'https://www.apartments.com/philadelphia-pa-19121/319-to-478',
        'https://www.apartments.com/houston-tx-77029/560-to-1198',
        'https://www.apartments.com/albuquerque-nm-87114/319-to-478',
        'https://www.apartments.com/atlanta-ga-30315/319-to-478',
        'https://www.apartments.com/springfield-oh-45504/320-to-838',
        'https://www.apartments.com/chesapeake-va-23320/560-to-1198',
        'https://www.apartments.com/yucca-valley-ca-92284/560-to-1198',
        'https://www.apartments.com/columbia-md-21046/560-to-1198',
        'https://www.apartments.com/buckeye-az-85326/1000-to-1200',
        'https://www.apartments.com/cleveland-oh-44126/560-to-1198',
        'https://www.apartments.com/gainesville-fl-32641/319-to-478',
        'https://www.apartments.com/lumberton-nc-28358/319-to-478',
        'https://www.apartments.com/austell-ga-30106/319-to-478',
        'https://www.apartments.com/powder-springs-ga-30127/320-to-838',
        'https://www.apartments.com/visalia-ca-93291/560-to-1198',
        'https://www.apartments.com/houston-oh-45333/319-to-478',
        'https://www.apartments.com/logan-oh-43138/320-to-838',
        'https://www.apartments.com/high-point-nc-27262/560-to-1198',
        'https://www.apartments.com/killeen-tx-76542/320-to-838',
        'https://www.apartments.com/henderson-nc-27537/1000-to-1200',
        'https://www.apartments.com/columbus-in-47201/320-to-838',
        'https://www.apartments.com/curtice-oh-43412/560-to-1198',
        'https://www.apartments.com/miami-fl-33133/560-to-1198',
        'https://www.apartments.com/toledo-oh-43611/319-to-478',
        'https://www.apartments.com/mays-landing-nj-8330/320-to-838',
        'https://www.apartments.com/milwaukee-wi-53208/320-to-838',
        'https://www.apartments.com/fort-wayne-in-46845/320-to-838',
        'https://www.apartments.com/atlanta-ga-30318/320-to-838',
        'https://www.apartments.com/sacramento-ca-95826/560-to-1198',
        'https://www.apartments.com/mesa-az-85207/320-to-838',
        'https://www.apartments.com/wister-ok-74966/319-to-478',
        'https://www.apartments.com/wahiawa-hi-96786/320-to-838',
        'https://www.apartments.com/winston-salem-nc-27107/320-to-838',
        'https://www.apartments.com/daytona-beach-fl-32118/320-to-838',
        'https://www.apartments.com/salt-lake-city-ut-84115/320-to-838',
        'https://www.apartments.com/gibsonton-fl-33534/319-to-478',
        'https://www.apartments.com/pompano-beach-fl-33062/1000-to-1200',
        'https://www.apartments.com/galax-va-24333/1000-to-1200',
        'https://www.apartments.com/ellenwood-ga-30294/560-to-1198',
        'https://www.apartments.com/muncie-in-47303/560-to-1198',
        'https://www.apartments.com/wagoner-ok-74467/320-to-838',
        'https://www.apartments.com/austin-tx-78758/1000-to-1200',
        'https://www.apartments.com/port-orange-fl-32127/560-to-1198',
        'https://www.apartments.com/philadelphia-pa-19138/320-to-838',
        'https://www.apartments.com/redlands-ca-92374/560-to-1198',
        'https://www.apartments.com/des-moines-ia-50317/320-to-838',
        'https://www.apartments.com/roanoke-va-24016/1000-to-1200',
        'https://www.apartments.com/franklin-in-46131/320-to-838',
        'https://www.apartments.com/herndon-va-20170/560-to-1198',
        'https://www.apartments.com/carrollton-ga-30117/320-to-838',
        'https://www.apartments.com/ada-ok-74820/320-to-838',
        'https://www.apartments.com/fort-smith-ar-72916/319-to-478',
        'https://www.apartments.com/shelby-nc-28150/320-to-838',
        'https://www.apartments.com/wildwood-fl-34785/319-to-478',
        'https://www.apartments.com/daytona-beach-fl-32114/320-to-838',
        'https://www.apartments.com/indianapolis-in-46204/560-to-1198',
        'https://www.apartments.com/milaca-mn-56353/320-to-838',
        'https://www.apartments.com/saint-james-mo-65559/320-to-838',
        'https://www.apartments.com/cartersville-ga-30120/320-to-838',
        'https://www.apartments.com/centralia-il-62801/320-to-838',
        'https://www.apartments.com/estacada-or-97023/560-to-1198',
        'https://www.apartments.com/rockford-il-61101/320-to-838',
        'https://www.apartments.com/lithonia-ga-30058/319-to-478',
        'https://www.apartments.com/shallotte-nc-28470/320-to-838',
        'https://www.apartments.com/kenosha-wi-53144/320-to-838',
        'https://www.apartments.com/athens-ga-30606/320-to-838',
        'https://www.apartments.com/covington-ga-30014/560-to-1198',
        'https://www.apartments.com/austin-tx-78753/320-to-838',
        'https://www.apartments.com/baltimore-md-21215/560-to-1198',
        'https://www.apartments.com/columbus-oh-43227/320-to-838',
        'https://www.apartments.com/reading-pa-19604/320-to-838',
        'https://www.apartments.com/cleveland-oh-44109/1000-to-1200',
        'https://www.apartments.com/miami-fl-33147/1000-to-1200',
        'https://www.apartments.com/cary-nc-27518/320-to-838',
        'https://www.apartments.com/philadelphia-pa-19120/320-to-838',
        'https://www.apartments.com/chicago-il-60619/320-to-838',
        'https://www.apartments.com/jacksonville-fl-32210/1000-to-1200',
        'https://www.apartments.com/hickory-nc-28601/320-to-838',
        'https://www.apartments.com/sanford-nc-27330/320-to-838',
        'https://www.apartments.com/nacogdoches-tx-75964/320-to-838',
        'https://www.apartments.com/swanton-oh-43558/320-to-838',
        'https://www.apartments.com/ocala-fl-34476/320-to-838',
        'https://www.apartments.com/auburn-in-46706/319-to-478',
        'https://www.apartments.com/cincinnati-oh-45215/560-to-1198',
        'https://www.apartments.com/norfolk-va-23504/320-to-838',
        'https://www.apartments.com/keysville-va-23947/320-to-838',
        'https://www.apartments.com/stockton-ca-95206/1000-to-1200',
        'https://www.apartments.com/red-oak-tx-75154/320-to-838',
        'https://www.apartments.com/tremonton-ut-84337/320-to-838',
        'https://www.apartments.com/georgetown-tx-78633/560-to-1198',
        'https://www.apartments.com/martinsville-in-46151/560-to-1198',
        'https://www.apartments.com/jonesboro-ar-72404/319-to-478',
        'https://www.apartments.com/ladson-sc-29456/320-to-838',
        'https://www.apartments.com/philadelphia-pa-19136/319-to-478',
        'https://www.apartments.com/victorville-ca-92392/320-to-838',
        'https://www.apartments.com/tucson-az-85701/320-to-838',
        'https://www.apartments.com/spartanburg-sc-29302/320-to-838',
        'https://www.apartments.com/calera-al-35040/560-to-1198',
        'https://www.apartments.com/stockton-ca-95205/320-to-838',
        'https://www.apartments.com/springfield-or-97477/320-to-838',
        'https://www.apartments.com/fontana-ca-92336/320-to-838',
        'https://www.apartments.com/minneapolis-mn-55426/560-to-1198',
        'https://www.apartments.com/buffalo-ny-14207/560-to-1198',
        'https://www.apartments.com/finksburg-md-21048/320-to-838',
        'https://www.apartments.com/ozark-al-36360/320-to-838',
        'https://www.apartments.com/augusta-ga-30901/320-to-838',
        'https://www.apartments.com/hickory-hills-il-60457/320-to-838',
        'https://www.apartments.com/cape-may-court-house-nj-8210/320-to-838',
        'https://www.apartments.com/erlanger-ky-41018/320-to-838',
        'https://www.apartments.com/cartersville-ga-30121/560-to-1198',
        'https://www.apartments.com/suffolk-va-23438/1000-to-1200',
        'https://www.apartments.com/brooklyn-ny-11237/1000-to-1200',
        'https://www.apartments.com/san-pablo-ca-94806/560-to-1198',
        'https://www.apartments.com/west-palm-beach-fl-33401/560-to-1198',
        'https://www.apartments.com/wynne-ar-72396/319-to-478',
        'https://www.apartments.com/frostproof-fl-33843/319-to-478',
        'https://www.apartments.com/santa-paula-ca-93060/1000-to-1200',
        'https://www.apartments.com/joplin-mo-64804/320-to-838',
        'https://www.apartments.com/bronx-ny-10457/320-to-838',
        'https://www.apartments.com/capitol-heights-md-20743/560-to-1198',
        'https://www.apartments.com/tallahassee-fl-32317/320-to-838',
        'https://www.apartments.com/tracy-ca-95377/320-to-838',
        'https://www.apartments.com/maple-heights-oh-44137/1000-to-1200',
        'https://www.apartments.com/gastonia-nc-28052/319-to-478',
        'https://www.apartments.com/milwaukee-wi-53207/560-to-1198',
        'https://www.apartments.com/springdale-ar-72764/320-to-838',
        'https://www.apartments.com/kissimmee-fl-34741/560-to-1198',
        'https://www.apartments.com/wendell-nc-27591/320-to-838',
        'https://www.apartments.com/reading-pa-19602/560-to-1198',
        'https://www.apartments.com/clearwater-fl-33755/1000-to-1200',
        'https://www.apartments.com/burley-id-83318/319-to-478',
        'https://www.apartments.com/texarkana-tx-75501/319-to-478',
        'https://www.apartments.com/newark-nj-7103/560-to-1198',
        'https://www.apartments.com/lyles-tn-37098/320-to-838',
        'https://www.apartments.com/portsmouth-nh-3801/560-to-1198',
        'https://www.apartments.com/warsaw-in-46580/560-to-1198',
        'https://www.apartments.com/hollywood-fl-33020/560-to-1198',
        'https://www.apartments.com/warren-oh-44485/320-to-838',
        'https://www.apartments.com/greeneville-tn-37743/320-to-838',
        'https://www.apartments.com/gilbert-az-85234/560-to-1198',
        'https://www.apartments.com/bedford-tx-76021/320-to-838',
        'https://www.apartments.com/longmont-co-80501/1000-to-1200',
        'https://www.apartments.com/starkville-ms-39759/320-to-838',
        'https://www.apartments.com/detroit-mi-48219/320-to-838',
        'https://www.apartments.com/hydesville-ca-95547/319-to-478',
        'https://www.apartments.com/toledo-oh-43612/319-to-478',
        'https://www.apartments.com/waterbury-ct-6710/560-to-1198',
        'https://www.apartments.com/cornelia-ga-30531/320-to-838',
        'https://www.apartments.com/canton-tx-75103/1000-to-1200',
        'https://www.apartments.com/auburn-wa-98002/320-to-838',
        'https://www.apartments.com/middletown-oh-45044/560-to-1198',
        'https://www.apartments.com/elizabeth-city-nc-27909/560-to-1198',
        'https://www.apartments.com/austin-tx-78744/320-to-838',
        'https://www.apartments.com/gainesville-fl-32601/320-to-838',
        'https://www.apartments.com/columbia-tn-38401/560-to-1198',
        'https://www.apartments.com/davenport-ia-52803/319-to-478',
        'https://www.apartments.com/bakersfield-ca-93301/560-to-1198',
        'https://www.apartments.com/douglas-ga-31533/320-to-838',
        'https://www.apartments.com/louisville-ky-40217/560-to-1198',
        'https://www.apartments.com/miami-fl-33166/560-to-1198',
        'https://www.apartments.com/sterling-il-61081/320-to-838',
        'https://www.apartments.com/sulphur-springs-tx-75482/560-to-1198',
        'https://www.apartments.com/new-haven-ky-40051/560-to-1198',
        'https://www.apartments.com/cambridge-md-21613/1000-to-1200',
        'https://www.apartments.com/asheville-nc-28804/319-to-478',
        'https://www.apartments.com/portsmouth-va-23703/560-to-1198',
        'https://www.apartments.com/euclid-oh-44132/320-to-838',
        'https://www.apartments.com/rossville-ga-30741/320-to-838',
        'https://www.apartments.com/arvada-co-80005/560-to-1198',
        'https://www.apartments.com/petersburg-va-23803/320-to-838'

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
