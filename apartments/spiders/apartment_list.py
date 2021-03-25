import scrapy


class ApartmentListSpider(scrapy.Spider):
    name = 'apartment_list'
    allowed_domains = ['https://www.apartments.com']
    
    start_urls = [
        'https://www.apartments.com/mount-pleasant-tx-75455/400-to-1000',
        'https://www.apartments.com/tulsa-ok-74115/400-to-1000',
        'https://www.apartments.com/escanaba-mi-0/400-to-1000',
        'https://www.apartments.com/vine-grove-ky-40175/560-to-1198',
        'https://www.apartments.com/chicago-il-60649/320-to-838',
        'https://www.apartments.com/memphis-tn-38109/400-to-1000',
        'https://www.apartments.com/norfolk-va-23503/319-to-478',
        'https://www.apartments.com/lexington-nc-27292/320-to-838',
        'https://www.apartments.com/largo-fl-33774/320-to-838',
        'https://www.apartments.com/memphis-tn-38104/560-to-1198',
        'https://www.apartments.com/myrtle-beach-sc-29575/1000-to-1200',
        'https://www.apartments.com/orlando-fl-32808/400-to-1000',
        'https://www.apartments.com/melbourne-fl-32934/320-to-838',
        'https://www.apartments.com/nashville-tn-37217/560-to-1198',
        'https://www.apartments.com/san-antonio-tx-78249/1000-to-1200',
        'https://www.apartments.com/lafayette-in-47904/319-to-478',
        'https://www.apartments.com/augusta-ga-30904/320-to-838',
        'https://www.apartments.com/detroit-mi-48213/320-to-838',
        'https://www.apartments.com/cartersville-ga-30120/319-to-478',
        'https://www.apartments.com/san-bernardino-ca-92407/400-to-1000',
        'https://www.apartments.com/massillon-oh-44646/320-to-838',
        'https://www.apartments.com/florence-sc-29501/400-to-1000',
        'https://www.apartments.com/evansville-in-47713/320-to-838',
        'https://www.apartments.com/bradenton-fl-34208/560-to-1198',
        'https://www.apartments.com/milwaukee-wi-53210/400-to-1000',
        'https://www.apartments.com/pittsburgh-pa-15206/400-to-1000',
        'https://www.apartments.com/waukesha-wi-53188/400-to-1000',
        'https://www.apartments.com/ogden-ut-84401/560-to-1198',
        'https://www.apartments.com/fort-worth-tx-76115/400-to-1000',
        'https://www.apartments.com/bowling-green-ky-42101/319-to-478',
        'https://www.apartments.com/womelsdorf-pa-19567/320-to-838',
        'https://www.apartments.com/orlando-fl-32804/560-to-1198',
        'https://www.apartments.com/wilmington-nc-28411/320-to-838',
        'https://www.apartments.com/wilson-nc-27893/319-to-478',
        'https://www.apartments.com/coralville-ia-52241/320-to-838',
        'https://www.apartments.com/fishers-in-46037/400-to-1000',
        'https://www.apartments.com/saint-louis-mo-63139/320-to-838',
        'https://www.apartments.com/havelock-nc-28532/560-to-1198',
        'https://www.apartments.com/sulphur-la-70663/320-to-838',
        'https://www.apartments.com/nan-nan-33902/560-to-1198',
        'https://www.apartments.com/chester-sc-29706/320-to-838',
        'https://www.apartments.com/columbia-sc-29203/400-to-1000',
        'https://www.apartments.com/crystal-lake-il-60014/320-to-838',
        'https://www.apartments.com/perry-fl-32348/1000-to-1200',
        'https://www.apartments.com/nan-nan-70727/320-to-838',
        'https://www.apartments.com/bridgeport-ct-6604/319-to-478',
        'https://www.apartments.com/lubbock-tx-79414/320-to-838',
        'https://www.apartments.com/atlanta-ga-30318/319-to-478',
        'https://www.apartments.com/davenport-ia-52803/400-to-1000',
        'https://www.apartments.com/michigan-city-in-46360/400-to-1000',
        'https://www.apartments.com/hesperia-ca-92345/1000-to-1200',
        'https://www.apartments.com/summerville-sc-29485/320-to-838',
        'https://www.apartments.com/rochester-ny-14606/400-to-1000',
        'https://www.apartments.com/chippewa-falls-wi-54729/400-to-1000',
        'https://www.apartments.com/abilene-tx-79605/320-to-838',
        'https://www.apartments.com/greenville-sc-29609/320-to-838',
        'https://www.apartments.com/minneapolis-mn-55403/1000-to-1200',
        'https://www.apartments.com/darby-pa-19023/400-to-1000',
        'https://www.apartments.com/cleveland-oh-44108/320-to-838',
        'https://www.apartments.com/horn-lake-ms-38637/400-to-1000',
        'https://www.apartments.com/chicago-il-60628/319-to-478',
        'https://www.apartments.com/tulsa-ok-74112/400-to-1000',
        'https://www.apartments.com/cypress-tx-77433/1000-to-1200',
        'https://www.apartments.com/clinton-sc-29325/320-to-838',
        'https://www.apartments.com/york-sc-29745/400-to-1000',
        'https://www.apartments.com/saint-louis-mo-63136/320-to-838',
        'https://www.apartments.com/rochester-ny-14611/400-to-1000',
        'https://www.apartments.com/corsicana-tx-75110/320-to-838',
        'https://www.apartments.com/san-marcos-tx-78666/1000-to-1200',
        'https://www.apartments.com/baytown-tx-77520/560-to-1198',
        'https://www.apartments.com/holland-mi-49424/560-to-1198',
        'https://www.apartments.com/cincinnati-oh-45237/400-to-1000',
        'https://www.apartments.com/graniteville-sc-29829/319-to-478',
        'https://www.apartments.com/lenoir-nc-28645/319-to-478',
        'https://www.apartments.com/ansonia-ct-6401/1000-to-1200',
        'https://www.apartments.com/madisonville-ky-42431/319-to-478',
        'https://www.apartments.com/flint-mi-48504/320-to-838',
        'https://www.apartments.com/twin-falls-id-83301/560-to-1198',
        'https://www.apartments.com/dallas-tx-75211/1000-to-1200',
        'https://www.apartments.com/fresno-ca-93722/400-to-1000',
        'https://www.apartments.com/charleston-sc-29407/1000-to-1200',
        'https://www.apartments.com/philadelphia-pa-19143/1000-to-1200',
        'https://www.apartments.com/columbus-oh-43232/320-to-838',
        'https://www.apartments.com/memphis-tn-38122/400-to-1000',
        'https://www.apartments.com/birmingham-al-35208/320-to-838',
        'https://www.apartments.com/jacksonville-fl-32207/560-to-1198',
        'https://www.apartments.com/rixeyville-va-22737/400-to-1000',
        'https://www.apartments.com/indianapolis-in-46218/319-to-478',
        'https://www.apartments.com/owensville-oh-45160/319-to-478',
        'https://www.apartments.com/englewood-tn-37329/400-to-1000',
        'https://www.apartments.com/frankfort-in-46041/400-to-1000',
        'https://www.apartments.com/florence-ms-39073/319-to-478',
        'https://www.apartments.com/bonney-lake-wa-98391/400-to-1000',
        'https://www.apartments.com/east-hartford-ct-6118/319-to-478',
        'https://www.apartments.com/toledo-oh-43608/400-to-1000',
        'https://www.apartments.com/stuart-fl-34994/1000-to-1200',
        'https://www.apartments.com/south-bend-in-46613/320-to-838',
        'https://www.apartments.com/chicago-il-60644/320-to-838',
        'https://www.apartments.com/amelia-court-house-va-23002/320-to-838',
        'https://www.apartments.com/como-ms-38619/320-to-838',
        'https://www.apartments.com/wichita-ks-67216/320-to-838',
        'https://www.apartments.com/monroe-mi-48162/560-to-1198',
        'https://www.apartments.com/san-antonio-tx-78228/1000-to-1200',
        'https://www.apartments.com/pasadena-tx-77504/320-to-838',
        'https://www.apartments.com/savannah-ga-31405/320-to-838',
        'https://www.apartments.com/newburgh-ny-12550/319-to-478',
        'https://www.apartments.com/sapulpa-ok-74066/320-to-838',
        'https://www.apartments.com/nan-nan-20473/1000-to-1200',
        'https://www.apartments.com/dallas-tx-75215/560-to-1198',
        'https://www.apartments.com/new-castle-pa-16105/560-to-1198',
        'https://www.apartments.com/huntsville-al-35810/1000-to-1200',
        'https://www.apartments.com/bronx-ny-10451/560-to-1198',
        'https://www.apartments.com/milwaukee-wi-53233/400-to-1000',
        'https://www.apartments.com/rapid-city-sd-57701/319-to-478',
        'https://www.apartments.com/cleveland-oh-44102/319-to-478',
        'https://www.apartments.com/houston-tx-77031/319-to-478',
        'https://www.apartments.com/supply-nc-28462/560-to-1198',
        'https://www.apartments.com/tampa-fl-33612/560-to-1198',
        'https://www.apartments.com/fort-worth-tx-76133/400-to-1000',
        'https://www.apartments.com/atlanta-ga-30344/560-to-1198',
        'https://www.apartments.com/toledo-oh-43605/320-to-838',
        'https://www.apartments.com/sebastian-fl-32976/1000-to-1200',
        'https://www.apartments.com/memphis-tn-38114/320-to-838',
        'https://www.apartments.com/albany-ny-12208/320-to-838',
        'https://www.apartments.com/manchester-nh-3103/1000-to-1200',
        'https://www.apartments.com/chesapeake-va-23324/400-to-1000',
        'https://www.apartments.com/decatur-il-62522/319-to-478',
        'https://www.apartments.com/las-vegas-nv-89145/400-to-1000',
        'https://www.apartments.com/buckeye-az-85326/1000-to-1200',
        'https://www.apartments.com/mesquite-tx-75149/1000-to-1200',
        'https://www.apartments.com/lexington-park-md-20653/1000-to-1200',
        'https://www.apartments.com/clearwater-fl-33762/320-to-838',
        'https://www.apartments.com/memphis-tn-38108/400-to-1000',
        'https://www.apartments.com/miami-fl-33135/400-to-1000',
        'https://www.apartments.com/winston-salem-nc-27105/320-to-838',
        'https://www.apartments.com/springfield-mo-65803/320-to-838',
        'https://www.apartments.com/gainesville-ga-30501/560-to-1198',
        'https://www.apartments.com/saint-louis-mo-63123/400-to-1000',
        'https://www.apartments.com/indianapolis-in-46250/320-to-838',
        'https://www.apartments.com/arabi-la-70032/320-to-838',
        'https://www.apartments.com/valdosta-ga-31601/320-to-838',
        'https://www.apartments.com/dayton-oh-45417/400-to-1000',
        'https://www.apartments.com/flint-mi-48507/319-to-478',
        'https://www.apartments.com/charlotte-nc-28227/320-to-838',
        'https://www.apartments.com/ladson-sc-29456/320-to-838',
        'https://www.apartments.com/worcester-ma-1605/320-to-838',
        'https://www.apartments.com/san-antonio-tx-78240/1000-to-1200',
        'https://www.apartments.com/pontiac-mi-48341/400-to-1000',
        'https://www.apartments.com/lawrenceburg-tn-38464/319-to-478',
        'https://www.apartments.com/phenix-city-al-36867/320-to-838',
        'https://www.apartments.com/orange-park-fl-32065/560-to-1198',
        'https://www.apartments.com/clinton-ms-39056/319-to-478',
        'https://www.apartments.com/asheboro-nc-27203/320-to-838',
        'https://www.apartments.com/lumberton-nc-28358/400-to-1000',
        'https://www.apartments.com/marcus-hook-pa-19061/320-to-838',
        'https://www.apartments.com/macon-ga-31204/1000-to-1200',
        'https://www.apartments.com/victoria-tx-77901/319-to-478',
        'https://www.apartments.com/wichita-falls-tx-76309/320-to-838',
        'https://www.apartments.com/lubbock-tx-79412/319-to-478',
        'https://www.apartments.com/texas-city-tx-77590/560-to-1198',
        'https://www.apartments.com/galesburg-il-61401/319-to-478',
        'https://www.apartments.com/raleigh-nc-27606/1000-to-1200',
        'https://www.apartments.com/elizabethtown-pa-17022/320-to-838',
        'https://www.apartments.com/newberry-sc-29108/400-to-1000',
        'https://www.apartments.com/casco-mi-48064/320-to-838',
        'https://www.apartments.com/leblanc-la-70651/560-to-1198',
        'https://www.apartments.com/luling-tx-78648/320-to-838',
        'https://www.apartments.com/greenwood-ms-38930/319-to-478',
        'https://www.apartments.com/lake-forest-ca-92630/400-to-1000',
        'https://www.apartments.com/slocomb-al-36375/320-to-838',
        'https://www.apartments.com/covina-ca-91723/320-to-838',
        'https://www.apartments.com/reno-nv-89521/1000-to-1200',
        'https://www.apartments.com/pensacola-fl-32514/560-to-1198',
        'https://www.apartments.com/fayetteville-nc-28311/400-to-1000',
        'https://www.apartments.com/austin-tx-78753/320-to-838',
        'https://www.apartments.com/greenville-sc-29605/319-to-478',
        'https://www.apartments.com/memphis-tn-38115/560-to-1198',
        'https://www.apartments.com/bay-saint-louis-ms-39520/320-to-838',
        'https://www.apartments.com/madison-ms-39110/400-to-1000',
        'https://www.apartments.com/byron-ga-31008/560-to-1198',
        'https://www.apartments.com/nan-nan-32572/1000-to-1200',
        'https://www.apartments.com/calhoun-ga-30701/560-to-1198',
        'https://www.apartments.com/grand-junction-co-81501/1000-to-1200',
        'https://www.apartments.com/milwaukee-wi-53215/400-to-1000',
        'https://www.apartments.com/jacksonville-fl-32211/560-to-1198',
        'https://www.apartments.com/baton-rouge-la-70810/320-to-838',
        'https://www.apartments.com/tampa-fl-33615/400-to-1000',
        'https://www.apartments.com/trenton-nj-8610/1000-to-1200',
        'https://www.apartments.com/marietta-ga-30060/400-to-1000',
        'https://www.apartments.com/cathedral-city-ca-92234/560-to-1198',
        'https://www.apartments.com/fontana-ca-92335/320-to-838',
        'https://www.apartments.com/portland-or-97217/400-to-1000',
        'https://www.apartments.com/phoenix-az-85032/400-to-1000',
        'https://www.apartments.com/nan-nan-29578/319-to-478',
        'https://www.apartments.com/decatur-il-62526/319-to-478',
        'https://www.apartments.com/myrtle-beach-sc-29577/320-to-838',
        'https://www.apartments.com/tulsa-ok-74133/560-to-1198',
        'https://www.apartments.com/mobile-al-36608/560-to-1198',
        'https://www.apartments.com/orting-wa-98360/319-to-478',
        'https://www.apartments.com/fort-worth-tx-76119/320-to-838',
        'https://www.apartments.com/pensacola-fl-32526/400-to-1000',
        'https://www.apartments.com/nan-nan-98455/319-to-478',
        'https://www.apartments.com/baton-rouge-la-70811/320-to-838',
        'https://www.apartments.com/bronx-ny-10458/319-to-478',
        'https://www.apartments.com/opelousas-la-70570/320-to-838',
        'https://www.apartments.com/durham-nc-27703/400-to-1000',
        'https://www.apartments.com/nashville-tn-37208/320-to-838',
        'https://www.apartments.com/forest-grove-or-97116/560-to-1198',
        'https://www.apartments.com/converse-tx-78109/560-to-1198',
        'https://www.apartments.com/nan-nan-10080/400-to-1000',
        'https://www.apartments.com/chandler-az-85249/560-to-1198',
        'https://www.apartments.com/leakesville-ms-39451/319-to-478',
        'https://www.apartments.com/greenville-sc-29611/319-to-478',
        'https://www.apartments.com/mcminnville-or-97128/560-to-1198',
        'https://www.apartments.com/jacksonville-fl-32205/400-to-1000'

        
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
