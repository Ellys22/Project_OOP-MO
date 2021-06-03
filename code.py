from daftlistings import Daft, Location, SearchType, PropertyType, Facility, Ber



# location Dublin 1 and/or Dublin2
# - price : if is need it a range can be between 500€ - 1000€
# - apartment 1 room
# - studio
# - single or double bed
# - shared room in apartment

locationList = [Location.DUBLIN_1_DUBLIN, Location.DUBLIN_2_DUBLIN]
typeList = [PropertyType.HOUSE, PropertyType.STUDIO_APARTMENT]
facilityList = [Facility.INTERNET, Facility.CENTRAL_HEATING]
searchList = [SearchType.STUDENT_ACCOMMODATION, SearchType.SHARING]

def getData():
    daft = Daft()
    daft.set_min_price(500)
    daft.set_max_price(1000)
    daft.set_max_beds(2)
    daft.set_facility(Facility.INTERNET)
    
    listings = daft.search()
    print(len(listings))


    for listing in listings:
        print(listing.title)
        print(listing.price)
        print(listing.daft_link)
        print(listing.bedrooms)
        print(listing.brochure)
        print()


# git push https://Ellys22:ETscorpion22@20@github.com/B_user_name/project.git

# git config user.name Ellys22
# git config user.email sba21167@student.cct.ie