from daftlistings import Daft, Location, SearchType

daft = Daft()
daft.set_location(Location.DUBLIN_CITY_CENTRE_DUBLIN)
daft.set_search_type(SearchType.STUDENT_ACCOMMODATION)
daft.set_search_type(SearchType.SHARING)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)


