import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/metairie-la-70001/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76116/1000-to-2000',
        'https://www.apartments.com/san-bernardino-ca-92411/1000-to-2000',
        'https://www.apartments.com/hickory-nc-28601/1000-to-2000',
        'https://www.apartments.com/jamaica-ny-11435/1000-to-2000',
        'https://www.apartments.com/charleston-mo-63834/1000-to-2000',
        'https://www.apartments.com/mebane-nc-27302/1000-to-2000',
        'https://www.apartments.com/mastic-ny-11950/1000-to-2000',
        'https://www.apartments.com/corpus-christi-tx-78405/1000-to-2000',
        'https://www.apartments.com/sparrows-point-md-21219/1000-to-2000',
        'https://www.apartments.com/irvington-nj-0/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28205/1000-to-2000',
        'https://www.apartments.com/essex-md-21221/1000-to-2000',
        'https://www.apartments.com/west-warwick-ri-2893/1000-to-2000',
        'https://www.apartments.com/palmdale-ca-93550/1000-to-2000',
        'https://www.apartments.com/norcross-ga-30093/1000-to-2000',
        'https://www.apartments.com/oklahoma-city-ok-73119/1000-to-2000',
        'https://www.apartments.com/rocky-mount-nc-27804/1000-to-2000',
        'https://www.apartments.com/malta-bend-mo-65339/1000-to-2000',
        'https://www.apartments.com/ocala-fl-34472/1000-to-2000',
        'https://www.apartments.com/lima-oh-45801/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45239/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46256/1000-to-2000',
        'https://www.apartments.com/springfield-gardens-ny-11413/1000-to-2000',
        'https://www.apartments.com/brownsville-tx-78521/1000-to-2000',
        'https://www.apartments.com/fayetteville-ar-72701/1000-to-2000',
        'https://www.apartments.com/tempe-az-85281/1000-to-2000',
        'https://www.apartments.com/harrisburg-pa-17110/1000-to-2000',
        'https://www.apartments.com/eaton-in-47338/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44108/1000-to-2000',
        'https://www.apartments.com/monroe-ga-30655/1000-to-2000',
        'https://www.apartments.com/maryville-tn-37801/1000-to-2000',
        'https://www.apartments.com/pittsburgh-pa-15212/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46222/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19132/1000-to-2000',
        'https://www.apartments.com/wichita-falls-tx-76306/1000-to-2000',
        'https://www.apartments.com/augusta-me-4330/1000-to-2000',
        'https://www.apartments.com/rochester-ny-14617/1000-to-2000',
        'https://www.apartments.com/ellenton-fl-34222/1000-to-2000',
        'https://www.apartments.com/sikeston-mo-63801/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19139/1000-to-2000',
        'https://www.apartments.com/mooresburg-tn-37811/1000-to-2000',
        'https://www.apartments.com/ellenwood-ga-30294/1000-to-2000',
        'https://www.apartments.com/nan-nan-75015/1000-to-2000',
        'https://www.apartments.com/muskogee-ok-74401/1000-to-2000',
        'https://www.apartments.com/baltimore-md-21215/1000-to-2000',
        'https://www.apartments.com/portsmouth-oh-45662/1000-to-2000',
        'https://www.apartments.com/statesboro-ga-30458/1000-to-2000',
        'https://www.apartments.com/rocky-mount-va-24151/1000-to-2000',
        'https://www.apartments.com/rock-hill-sc-29732/1000-to-2000',
        'https://www.apartments.com/loudon-tn-37774/1000-to-2000',
        'https://www.apartments.com/hanford-ca-93230/1000-to-2000',
        'https://www.apartments.com/sterling-il-61081/1000-to-2000',
        'https://www.apartments.com/mobile-al-36608/1000-to-2000',
        'https://www.apartments.com/providence-ri-2904/1000-to-2000',
        'https://www.apartments.com/orlando-fl-32805/1000-to-2000',
        'https://www.apartments.com/joliet-il-60436/1000-to-2000',
        'https://www.apartments.com/royal-oak-mi-48067/1000-to-2000',
        'https://www.apartments.com/san-antonio-tx-78223/1000-to-2000',
        'https://www.apartments.com/ormond-beach-fl-32174/1000-to-2000',
        'https://www.apartments.com/saint-augustine-fl-32080/1000-to-2000',
        'https://www.apartments.com/melbourne-fl-32901/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32209/1000-to-2000',
        'https://www.apartments.com/alpharetta-ga-30022/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32222/1000-to-2000',
        'https://www.apartments.com/harrisburg-pa-17103/1000-to-2000',
        'https://www.apartments.com/fayetteville-ga-30215/1000-to-2000',
        'https://www.apartments.com/live-oak-fl-32064/1000-to-2000',
        'https://www.apartments.com/douglasville-ga-30134/1000-to-2000',
        'https://www.apartments.com/fayetteville-nc-28301/1000-to-2000',
        'https://www.apartments.com/lincolnton-nc-28092/1000-to-2000',
        'https://www.apartments.com/capac-mi-48014/1000-to-2000',
        'https://www.apartments.com/okeechobee-fl-34974/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85031/1000-to-2000',
        'https://www.apartments.com/pawtucket-ri-2860/1000-to-2000',
        'https://www.apartments.com/columbia-mo-65202/1000-to-2000',
        'https://www.apartments.com/philadelphia-pa-19138/1000-to-2000',
        'https://www.apartments.com/hugo-ok-74743/1000-to-2000',
        'https://www.apartments.com/fresno-ca-93722/1000-to-2000',
        'https://www.apartments.com/siloam-springs-ar-72761/1000-to-2000',
        'https://www.apartments.com/lafayette-la-70503/1000-to-2000',
        'https://www.apartments.com/lansing-mi-48917/1000-to-2000',
        'https://www.apartments.com/live-oak-fl-32060/1000-to-2000',
        'https://www.apartments.com/redding-ca-96002/1000-to-2000',
        'https://www.apartments.com/hudson-nc-28638/1000-to-2000',
        'https://www.apartments.com/fayetteville-nc-28314/1000-to-2000',
        'https://www.apartments.com/rochester-ny-14606/1000-to-2000',
        'https://www.apartments.com/durham-nc-27703/1000-to-2000',
        'https://www.apartments.com/lake-worth-fl-33460/1000-to-2000',
        'https://www.apartments.com/charlotte-nc-28202/1000-to-2000',
        'https://www.apartments.com/nan-nan-39033/1000-to-2000',
        'https://www.apartments.com/sacramento-ca-95820/1000-to-2000',
        'https://www.apartments.com/louisville-ky-40205/1000-to-2000',
        'https://www.apartments.com/sanford-nc-27332/1000-to-2000',
        'https://www.apartments.com/columbus-ga-31904/1000-to-2000',
        'https://www.apartments.com/scottsdale-az-85251/1000-to-2000',
        'https://www.apartments.com/shelby-nc-28152/1000-to-2000',
        'https://www.apartments.com/eugene-or-97402/1000-to-2000',
        'https://www.apartments.com/garland-tx-75043/1000-to-2000',
        'https://www.apartments.com/waldorf-md-20601/1000-to-2000',
        'https://www.apartments.com/franklin-in-46131/1000-to-2000',
        'https://www.apartments.com/toledo-oh-43612/1000-to-2000',
        'https://www.apartments.com/san-juan-capistrano-ca-92675/1000-to-2000',
        'https://www.apartments.com/phoenix-az-85021/1000-to-2000',
        'https://www.apartments.com/hamtramck-mi-48212/1000-to-2000',
        'https://www.apartments.com/dawson-ga-39842/1000-to-2000',
        'https://www.apartments.com/yuma-az-85364/1000-to-2000',
        'https://www.apartments.com/hephzibah-ga-30815/1000-to-2000',
        'https://www.apartments.com/clarksville-tn-37042/1000-to-2000',
        'https://www.apartments.com/salem-or-97301/1000-to-2000',
        'https://www.apartments.com/southampton-pa-18966/1000-to-2000',
        'https://www.apartments.com/fort-lauderdale-fl-33311/1000-to-2000',
        'https://www.apartments.com/tifton-ga-31794/1000-to-2000',
        'https://www.apartments.com/woodside-ny-11377/1000-to-2000',
        'https://www.apartments.com/millen-ga-30442/1000-to-2000',
        'https://www.apartments.com/las-vegas-nv-89101/1000-to-2000',
        'https://www.apartments.com/new-orleans-la-70119/1000-to-2000',
        'https://www.apartments.com/cathedral-city-ca-92234/1000-to-2000',
        'https://www.apartments.com/vinton-la-70668/1000-to-2000',
        'https://www.apartments.com/hyattsville-md-20782/1000-to-2000',
        'https://www.apartments.com/chicago-il-60636/1000-to-2000',
        'https://www.apartments.com/harrison-oh-45030/1000-to-2000',
        'https://www.apartments.com/oklahoma-city-ok-73106/1000-to-2000',
        'https://www.apartments.com/oakland-ca-94603/1000-to-2000',
        'https://www.apartments.com/horn-lake-ms-38637/1000-to-2000',
        'https://www.apartments.com/high-point-nc-27260/1000-to-2000',
        'https://www.apartments.com/dayton-oh-45410/1000-to-2000',
        'https://www.apartments.com/kansas-city-mo-64124/1000-to-2000',
        'https://www.apartments.com/gastonia-nc-28052/1000-to-2000',
        'https://www.apartments.com/tifton-ga-31793/1000-to-2000',
        'https://www.apartments.com/fresno-ca-93710/1000-to-2000',
        'https://www.apartments.com/woodbury-ga-30293/1000-to-2000',
        'https://www.apartments.com/nan-nan-60666/1000-to-2000',
        'https://www.apartments.com/virginia-beach-va-23462/1000-to-2000',
        'https://www.apartments.com/pittsburg-ca-94565/1000-to-2000',
        'https://www.apartments.com/gainesville-ga-30501/1000-to-2000',
        'https://www.apartments.com/greensboro-nc-27455/1000-to-2000',
        'https://www.apartments.com/sanford-fl-32771/1000-to-2000',
        'https://www.apartments.com/riverdale-ga-30274/1000-to-2000',
        'https://www.apartments.com/commerce-city-co-80022/1000-to-2000',
        'https://www.apartments.com/salisbury-md-21804/1000-to-2000',
        'https://www.apartments.com/winter-haven-fl-33880/1000-to-2000',
        'https://www.apartments.com/saint-petersburg-fl-33706/1000-to-2000',
        'https://www.apartments.com/miami-fl-33157/1000-to-2000',
        'https://www.apartments.com/cleveland-oh-44106/1000-to-2000',
        'https://www.apartments.com/fort-smith-ar-72901/1000-to-2000',
        'https://www.apartments.com/lakewood-wa-98499/1000-to-2000',
        'https://www.apartments.com/hendersonville-nc-28792/1000-to-2000',
        'https://www.apartments.com/kenton-de-19955/1000-to-2000',
        'https://www.apartments.com/connellys-springs-nc-28612/1000-to-2000',
        'https://www.apartments.com/winnetka-ca-91306/1000-to-2000',
        'https://www.apartments.com/brownsville-tx-78526/1000-to-2000',
        'https://www.apartments.com/southfield-mi-48076/1000-to-2000',
        'https://www.apartments.com/dodge-city-ks-67801/1000-to-2000',
        'https://www.apartments.com/athol-ma-1331/1000-to-2000',
        'https://www.apartments.com/marion-va-24354/1000-to-2000',
        'https://www.apartments.com/visalia-ca-93291/1000-to-2000',
        'https://www.apartments.com/conway-ar-72034/1000-to-2000',
        'https://www.apartments.com/newark-de-19702/1000-to-2000',
        'https://www.apartments.com/ypsilanti-mi-48197/1000-to-2000',
        'https://www.apartments.com/cincinnati-oh-45204/1000-to-2000',
        'https://www.apartments.com/berwyn-il-60402/1000-to-2000',
        'https://www.apartments.com/raleigh-nc-27610/1000-to-2000',
        'https://www.apartments.com/indianapolis-in-46237/1000-to-2000',
        'https://www.apartments.com/tucson-az-85710/1000-to-2000',
        'https://www.apartments.com/nan-nan-98449/1000-to-2000',
        'https://www.apartments.com/york-pa-17404/1000-to-2000',
        'https://www.apartments.com/tampa-fl-33619/1000-to-2000',
        'https://www.apartments.com/maywood-ca-90270/1000-to-2000',
        'https://www.apartments.com/olympia-wa-98501/1000-to-2000',
        'https://www.apartments.com/wilmington-nc-28405/1000-to-2000',
        'https://www.apartments.com/joliet-il-60432/1000-to-2000',
        'https://www.apartments.com/oak-grove-ky-42262/1000-to-2000',
        'https://www.apartments.com/holland-mi-49423/1000-to-2000',
        'https://www.apartments.com/glendale-az-85302/1000-to-2000',
        'https://www.apartments.com/plano-tx-75074/1000-to-2000',
        'https://www.apartments.com/jersey-city-nj-7305/1000-to-2000',
        'https://www.apartments.com/fort-worth-tx-76108/1000-to-2000',
        'https://www.apartments.com/shreveport-la-71109/1000-to-2000',
        'https://www.apartments.com/strongsville-oh-44136/1000-to-2000',
        'https://www.apartments.com/ayer-ma-1432/1000-to-2000',
        'https://www.apartments.com/tulsa-ok-74127/1000-to-2000',
        'https://www.apartments.com/gadsden-al-35903/1000-to-2000',
        'https://www.apartments.com/crossville-tn-38571/1000-to-2000',
        'https://www.apartments.com/san-martin-ca-95046/1000-to-2000',
        'https://www.apartments.com/barbourville-ky-40906/1000-to-2000',
        'https://www.apartments.com/nan-nan-54215/1000-to-2000',
        'https://www.apartments.com/fairview-heights-il-62208/1000-to-2000',
        'https://www.apartments.com/jacksonville-fl-32208/1000-to-2000',
        'https://www.apartments.com/port-orchard-wa-98367/1000-to-2000',
        'https://www.apartments.com/eagle-creek-or-97022/1000-to-2000',
        'https://www.apartments.com/winder-ga-30680/1000-to-2000',
        'https://www.apartments.com/missoula-mt-59801/1000-to-2000',
        'https://www.apartments.com/fairfield-oh-45014/1000-to-2000',
        'https://www.apartments.com/idaho-falls-id-83402/1000-to-2000',
        'https://www.apartments.com/hutchinson-ks-67501/1000-to-2000',
        'https://www.apartments.com/queens-village-ny-11429/1000-to-2000'

        
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
