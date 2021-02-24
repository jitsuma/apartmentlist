import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/gaithersburg-md-20878/500-to-1500',
        'https://www.apartments.com/chicago-il-60621/500-to-1500',
        'https://www.apartments.com/rochester-ny-14611/500-to-1500',
        'https://www.apartments.com/fayetteville-nc-28304/500-to-1500',
        'https://www.apartments.com/berwick-pa-18603/500-to-1500',
        'https://www.apartments.com/springfield-il-62702/500-to-1500',
        'https://www.apartments.com/bullhead-city-az-86442/500-to-1500',
        'https://www.apartments.com/milwaukee-wi-53218/500-to-1500',
        'https://www.apartments.com/murfreesboro-tn-37127/500-to-1500',
        'https://www.apartments.com/albuquerque-nm-87123/500-to-1500',
        'https://www.apartments.com/gastonia-nc-28052/500-to-1500',
        'https://www.apartments.com/salisbury-nc-28146/500-to-1500',
        'https://www.apartments.com/portland-or-97229/500-to-1500',
        'https://www.apartments.com/goshen-in-46528/500-to-1500',
        'https://www.apartments.com/alliance-oh-44601/500-to-1500',
        'https://www.apartments.com/fort-lauderdale-fl-33334/500-to-1500',
        'https://www.apartments.com/killbuck-oh-44637/500-to-1500',
        'https://www.apartments.com/racine-wi-53404/500-to-1500',
        'https://www.apartments.com/elmont-ny-11003/500-to-1500',
        'https://www.apartments.com/nan-nan-0/500-to-1500',
        'https://www.apartments.com/kingston-ny-12401/500-to-1500',
        'https://www.apartments.com/pontiac-mi-48342/500-to-1500',
        'https://www.apartments.com/raleigh-nc-27601/500-to-1500',
        'https://www.apartments.com/highland-park-mi-48203/500-to-1500',
        'https://www.apartments.com/clearwater-fl-33762/500-to-1500',
        'https://www.apartments.com/charlotte-nc-28206/500-to-1500',
        'https://www.apartments.com/cleveland-tn-37312/500-to-1500',
        'https://www.apartments.com/indianapolis-in-46235/500-to-1500',
        'https://www.apartments.com/ridgewood-ny-11385/500-to-1500',
        'https://www.apartments.com/carlisle-pa-17013/500-to-1500',
        'https://www.apartments.com/detroit-mi-48235/500-to-1500',
        'https://www.apartments.com/springfield-mo-65802/500-to-1500',
        'https://www.apartments.com/florence-sc-29506/500-to-1500',
        'https://www.apartments.com/phenix-city-al-36867/500-to-1500',
        'https://www.apartments.com/jacksonville-fl-32209/500-to-1500',
        'https://www.apartments.com/joliet-il-60433/500-to-1500',
        'https://www.apartments.com/charlotte-nc-28205/500-to-1500',
        'https://www.apartments.com/san-antonio-tx-78223/500-to-1500',
        'https://www.apartments.com/bethlehem-pa-18017/500-to-1500',
        'https://www.apartments.com/inverness-fl-34453/500-to-1500',
        'https://www.apartments.com/lewisburg-pa-17837/500-to-1500',
        'https://www.apartments.com/saint-marys-ga-31558/500-to-1500',
        'https://www.apartments.com/birmingham-al-35211/500-to-1500',
        'https://www.apartments.com/memphis-tn-38117/500-to-1500',
        'https://www.apartments.com/burlington-ia-52601/500-to-1500',
        'https://www.apartments.com/orlando-fl-32812/500-to-1500',
        'https://www.apartments.com/port-huron-mi-48060/500-to-1500',
        'https://www.apartments.com/saint-louis-mo-63118/500-to-1500',
        'https://www.apartments.com/kingman-az-86401/500-to-1500',
        'https://www.apartments.com/kannapolis-nc-28083/500-to-1500',
        'https://www.apartments.com/san-angelo-tx-76903/500-to-1500',
        'https://www.apartments.com/wilmington-nc-28403/500-to-1500',
        'https://www.apartments.com/independence-la-70443/500-to-1500',
        'https://www.apartments.com/neptune-nj-7753/500-to-1500',
        'https://www.apartments.com/rome-ga-30165/500-to-1500',
        'https://www.apartments.com/stevens-point-wi-54481/500-to-1500',
        'https://www.apartments.com/san-pablo-ca-94806/500-to-1500',
        'https://www.apartments.com/riverview-fl-33578/500-to-1500',
        'https://www.apartments.com/clarksville-in-47129/500-to-1500',
        'https://www.apartments.com/brooklyn-ct-6234/500-to-1500',
        'https://www.apartments.com/taylorville-il-62568/500-to-1500',
        'https://www.apartments.com/marrero-la-70072/500-to-1500',
        'https://www.apartments.com/seffner-fl-33584/500-to-1500',
        'https://www.apartments.com/vancouver-wa-98660/500-to-1500',
        'https://www.apartments.com/alexander-nc-28701/500-to-1500',
        'https://www.apartments.com/roseville-mi-48066/500-to-1500',
        'https://www.apartments.com/hickory-nc-28601/500-to-1500',
        'https://www.apartments.com/bakersfield-ca-93305/500-to-1500',
        'https://www.apartments.com/benton-city-wa-99320/500-to-1500',
        'https://www.apartments.com/sunbury-pa-17801/500-to-1500',
        'https://www.apartments.com/richmond-va-23222/500-to-1500',
        'https://www.apartments.com/carrollton-ga-30116/500-to-1500',
        'https://www.apartments.com/colorado-springs-co-80922/500-to-1500',
        'https://www.apartments.com/dover-de-19904/500-to-1500',
        'https://www.apartments.com/churubusco-in-46723/500-to-1500',
        'https://www.apartments.com/melbourne-fl-32901/500-to-1500',
        'https://www.apartments.com/north-las-vegas-nv-89032/500-to-1500',
        'https://www.apartments.com/avondale-estates-ga-30002/500-to-1500',
        'https://www.apartments.com/tyler-tx-75701/500-to-1500',
        'https://www.apartments.com/marietta-ga-30060/500-to-1500',
        'https://www.apartments.com/new-bern-nc-28560/500-to-1500',
        'https://www.apartments.com/dallas-tx-75217/500-to-1500',
        'https://www.apartments.com/penns-grove-nj-8069/500-to-1500',
        'https://www.apartments.com/salisbury-md-21801/500-to-1500',
        'https://www.apartments.com/el-paso-tx-79934/500-to-1500',
        'https://www.apartments.com/san-antonio-tx-78251/500-to-1500',
        'https://www.apartments.com/chehalis-wa-98532/500-to-1500',
        'https://www.apartments.com/saint-louis-mo-63121/500-to-1500',
        'https://www.apartments.com/manchester-ct-6040/500-to-1500',
        'https://www.apartments.com/easton-pa-18042/500-to-1500',
        'https://www.apartments.com/melrose-park-il-60164/500-to-1500',
        'https://www.apartments.com/fort-worth-tx-76133/500-to-1500',
        'https://www.apartments.com/lufkin-tx-75901/500-to-1500',
        'https://www.apartments.com/anderson-sc-29624/500-to-1500',
        'https://www.apartments.com/pittsburg-ks-66762/500-to-1500',
        'https://www.apartments.com/orangevale-ca-95662/500-to-1500',
        'https://www.apartments.com/birmingham-al-35234/500-to-1500',
        'https://www.apartments.com/payson-az-85541/500-to-1500',
        'https://www.apartments.com/mobile-al-36612/500-to-1500',
        'https://www.apartments.com/albuquerque-nm-87102/500-to-1500',
        'https://www.apartments.com/federal-way-wa-98023/500-to-1500',
        'https://www.apartments.com/covington-ga-30014/500-to-1500',
        'https://www.apartments.com/coshocton-oh-43812/500-to-1500',
        'https://www.apartments.com/hollywood-fl-33024/500-to-1500',
        'https://www.apartments.com/mancelona-mi-49659/500-to-1500',
        'https://www.apartments.com/panama-city-fl-32401/500-to-1500',
        'https://www.apartments.com/yakima-wa-98903/500-to-1500',
        'https://www.apartments.com/albuquerque-nm-87108/500-to-1500',
        'https://www.apartments.com/lakeland-fl-33801/500-to-1500',
        'https://www.apartments.com/hinesville-ga-31313/500-to-1500',
        'https://www.apartments.com/detroit-mi-48227/500-to-1500',
        'https://www.apartments.com/jersey-city-nj-7305/500-to-1500',
        'https://www.apartments.com/delano-tn-37325/500-to-1500',
        'https://www.apartments.com/tucson-az-85719/500-to-1500',
        'https://www.apartments.com/decatur-il-62521/500-to-1500',
        'https://www.apartments.com/pelham-ga-31779/500-to-1500',
        'https://www.apartments.com/las-vegas-nv-89107/500-to-1500',
        'https://www.apartments.com/pueblo-co-81006/500-to-1500',
        'https://www.apartments.com/colorado-springs-co-80916/500-to-1500',
        'https://www.apartments.com/framingham-ma-1702/500-to-1500',
        'https://www.apartments.com/beaumont-tx-77708/500-to-1500',
        'https://www.apartments.com/siloam-springs-ar-72761/500-to-1500',
        'https://www.apartments.com/riverside-ca-92507/500-to-1500',
        'https://www.apartments.com/waterloo-il-62298/500-to-1500',
        'https://www.apartments.com/martin-tn-38237/500-to-1500',
        'https://www.apartments.com/tacoma-wa-98409/500-to-1500',
        'https://www.apartments.com/peoria-az-85345/500-to-1500',
        'https://www.apartments.com/nederland-tx-77627/500-to-1500',
        'https://www.apartments.com/valdosta-ga-31601/500-to-1500',
        'https://www.apartments.com/brunswick-ga-31520/500-to-1500',
        'https://www.apartments.com/lexington-nc-27292/500-to-1500',
        'https://www.apartments.com/temple-tx-76502/500-to-1500',
        'https://www.apartments.com/nan-nan-29503/500-to-1500',
        'https://www.apartments.com/mountain-home-ar-72653/500-to-1500',
        'https://www.apartments.com/gulfport-ms-39501/500-to-1500',
        'https://www.apartments.com/philadelphia-pa-19121/500-to-1500',
        'https://www.apartments.com/augusta-ga-30906/500-to-1500',
        'https://www.apartments.com/bullhead-city-az-86429/500-to-1500',
        'https://www.apartments.com/loveland-co-80537/500-to-1500',
        'https://www.apartments.com/lewistown-pa-17044/500-to-1500',
        'https://www.apartments.com/glendale-az-85301/500-to-1500',
        'https://www.apartments.com/torrance-ca-90503/500-to-1500',
        'https://www.apartments.com/klamath-falls-or-97601/500-to-1500',
        'https://www.apartments.com/farmington-nm-87401/500-to-1500',
        'https://www.apartments.com/morton-wa-98356/500-to-1500',
        'https://www.apartments.com/oswego-ny-13126/500-to-1500',
        'https://www.apartments.com/sanford-nc-27332/500-to-1500',
        'https://www.apartments.com/tampa-fl-33619/500-to-1500',
        'https://www.apartments.com/wilmington-ca-90744/500-to-1500',
        'https://www.apartments.com/poplar-bluff-mo-63901/500-to-1500',
        'https://www.apartments.com/hudson-ky-40145/500-to-1500',
        'https://www.apartments.com/burlington-wi-53105/500-to-1500',
        'https://www.apartments.com/denver-co-80232/500-to-1500',
        'https://www.apartments.com/dayton-oh-45424/500-to-1500',
        'https://www.apartments.com/boone-nc-28607/500-to-1500',
        'https://www.apartments.com/akron-oh-44320/500-to-1500',
        'https://www.apartments.com/rossville-ga-30741/500-to-1500',
        'https://www.apartments.com/hemet-ca-92544/500-to-1500',
        'https://www.apartments.com/el-paso-tx-79903/500-to-1500',
        'https://www.apartments.com/miami-fl-33142/500-to-1500',
        'https://www.apartments.com/paterson-nj-7522/500-to-1500',
        'https://www.apartments.com/lebanon-pa-17042/500-to-1500',
        'https://www.apartments.com/ripley-tn-38063/500-to-1500',
        'https://www.apartments.com/springfield-il-62703/500-to-1500',
        'https://www.apartments.com/kenosha-wi-53140/500-to-1500',
        'https://www.apartments.com/inwood-wv-25428/500-to-1500',
        'https://www.apartments.com/lumberton-nc-28358/500-to-1500',
        'https://www.apartments.com/riverdale-il-60827/500-to-1500',
        'https://www.apartments.com/phoenix-az-85022/500-to-1500',
        'https://www.apartments.com/gallup-nm-87301/500-to-1500',
        'https://www.apartments.com/pevely-mo-63070/500-to-1500',
        'https://www.apartments.com/chicago-il-60653/500-to-1500',
        'https://www.apartments.com/jackson-ms-39209/500-to-1500',
        'https://www.apartments.com/canton-ga-30115/500-to-1500',
        'https://www.apartments.com/sulphur-la-70663/500-to-1500',
        'https://www.apartments.com/pasadena-tx-77506/500-to-1500',
        'https://www.apartments.com/houston-tx-77016/500-to-1500',
        'https://www.apartments.com/syracuse-ny-13205/500-to-1500',
        'https://www.apartments.com/mobile-al-36603/500-to-1500',
        'https://www.apartments.com/nan-nan-34579/500-to-1500',
        'https://www.apartments.com/cartersville-ga-30121/500-to-1500',
        'https://www.apartments.com/inglewood-ca-90304/500-to-1500',
        'https://www.apartments.com/saginaw-mi-48601/500-to-1500',
        'https://www.apartments.com/skokie-il-60077/500-to-1500',
        'https://www.apartments.com/brandon-fl-33511/500-to-1500',
        'https://www.apartments.com/pearl-city-hi-96782/500-to-1500',
        'https://www.apartments.com/great-bend-ks-67530/500-to-1500',
        'https://www.apartments.com/baltimore-md-21218/500-to-1500',
        'https://www.apartments.com/maitland-fl-32751/500-to-1500',
        'https://www.apartments.com/pompano-beach-fl-33069/500-to-1500',
        'https://www.apartments.com/columbia-tn-38401/500-to-1500',
        'https://www.apartments.com/bay-minette-al-36507/500-to-1500',
        'https://www.apartments.com/jefferson-ga-30549/500-to-1500',
        'https://www.apartments.com/marshall-mi-49068/500-to-1500',
        'https://www.apartments.com/mc-kees-rocks-pa-15136/500-to-1500',
        'https://www.apartments.com/memphis-tn-38127/500-to-1500',
        'https://www.apartments.com/haines-city-fl-33844/500-to-1500',
        'https://www.apartments.com/berwyn-il-60402/500-to-1500',
        'https://www.apartments.com/culpeper-va-22701/500-to-1500',
        'https://www.apartments.com/darlington-sc-29532/500-to-1500',
        'https://www.apartments.com/hernando-ms-38632/500-to-1500',
        'https://www.apartments.com/columbus-oh-43228/500-to-1500',
        'https://www.apartments.com/richmond-va-23224/500-to-1500',
        'https://www.apartments.com/indianapolis-in-46229/500-to-1500',
        'https://www.apartments.com/taylor-mi-48180/500-to-1500',
        'https://www.apartments.com/cincinnati-oh-45206/500-to-1500',
        'https://www.apartments.com/bryant-ar-72022/500-to-1500',
        'https://www.apartments.com/lynn-ma-1905/500-to-1500',
        'https://www.apartments.com/conyers-ga-30012/500-to-1500',
        'https://www.apartments.com/columbia-sc-29203/500-to-1500',
        'https://www.apartments.com/chatsworth-ca-91311/500-to-1500',
        'https://www.apartments.com/tampa-fl-33602/500-to-1500',
        'https://www.apartments.com/kingman-az-86409/500-to-1500',
        'https://www.apartments.com/dundalk-md-21222/500-to-1500',
        'https://www.apartments.com/fredericksburg-pa-17026/500-to-1500',
        'https://www.apartments.com/citrus-heights-ca-95610/500-to-1500',
        'https://www.apartments.com/evansville-in-47710/500-to-1500',
        'https://www.apartments.com/charlotte-nc-28208/500-to-1500',
        'https://www.apartments.com/fort-lauderdale-fl-33311/500-to-1500',
        'https://www.apartments.com/porterville-ca-93257/500-to-1500',
        'https://www.apartments.com/kansas-city-mo-64124/500-to-1500',
        'https://www.apartments.com/clinton-ia-52732/500-to-1500',
        'https://www.apartments.com/stockton-ca-95204/500-to-1500',
        'https://www.apartments.com/wilmington-de-19809/500-to-1500',
        'https://www.apartments.com/tarpon-springs-fl-34689/500-to-1500',
        'https://www.apartments.com/lancaster-ca-93535/500-to-1500',
        'https://www.apartments.com/tucson-az-85711/500-to-1500',
        'https://www.apartments.com/keene-nh-3431/500-to-1500',
        'https://www.apartments.com/redford-mi-48239/500-to-1500',
        'https://www.apartments.com/houston-tx-77049/500-to-1500',
        'https://www.apartments.com/bastrop-la-71220/500-to-1500',
        'https://www.apartments.com/huntsville-al-35805/500-to-1500',
        'https://www.apartments.com/bell-gardens-ca-90201/500-to-1500',
        'https://www.apartments.com/cleveland-oh-44135/500-to-1500',
        'https://www.apartments.com/griffin-ga-30223/500-to-1500',
        'https://www.apartments.com/waterloo-ia-50702/500-to-1500',
        'https://www.apartments.com/cerritos-ca-90703/500-to-1500',
        'https://www.apartments.com/newport-news-va-23608/500-to-1500'



        
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
