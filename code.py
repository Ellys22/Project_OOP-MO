from daftlistings import Daft, Location, SearchType, PropertyType, Facility, Ber
import operator
import csv


# location Dublin 1 and/or Dublin2
# - price :  500€ - 1000€
# - apartment 1 room
# - studio
# - single or double bed
# - shared room in apartment

locationList = [Location.DUBLIN_1_DUBLIN, Location.DUBLIN_2_DUBLIN]
typeList = [PropertyType.HOUSE, PropertyType.STUDIO_APARTMENT]
facilityList = [Facility.INTERNET, Facility.CENTRAL_HEATING]
searchList = [SearchType.STUDENT_ACCOMMODATION, SearchType.SHARING]


def listToListofDict(myList):

    final_list = list(dict())

    for elem in myList:
        temp = dict()
        price_temp = elem.price.split(" ")

        temp["Title"] = elem.title
        temp["Price per month"] = int(price_temp[0][1:])
        # print(temp["price_val"])
        temp["Category"] = elem.category
        temp["Agent Name"] = elem.agent_name
        temp["Daft Link"] = elem.daft_link
        final_list.append(temp)
    return final_list


def sortListofDict(data):
    data.sort(key=operator.itemgetter('Price per month'))
    return data


def writeToCSV(data):
    keys = data[0].keys()
    with open('Result.csv', 'w', newline='') as file:
        file_writer = csv.DictWriter(file, keys)
        file_writer.writeheader()
        file_writer.writerows(data)


def getData():
    queryResult = list()
    daft = Daft()

    for location in locationList:
        for src in searchList:
            for facility in facilityList:
                for aptType in typeList:
                    print("\nLocation:{}, Search:{}, Facility:{}, PropertyType:{}".format(
                        location, src, facility, aptType))
                    daft.set_location(location)
                    daft.set_search_type(src)
                    daft.set_facility(facility)
                    daft.set_property_type(aptType)
                    daft.set_min_price(500)
                    daft.set_max_price(1000)
                    daft.set_max_beds(2)
                    listings = daft.search(max_pages=1)
                    queryResult += listings

    # print(len(queryResult))
    finalResult = [{}]
    # print(len(queryResult))
    resultList = list(set(queryResult))
    # print(len(resultList))
    finalResult = listToListofDict(resultList)
    # print(finalResult)
    # now the sorting will be implemented.
    # Because if I do sorting in the loop then for each loop I need to perform an nlog(n) complexity or sort algorithm
    # rather it's better to sort using the final list
    finalResult = sortListofDict(finalResult)
    # removing the duplicate results
    finalResult = [dict(t) for t in {tuple(d.items()) for d in finalResult}]
    # print(len(finalResult))
    writeToCSV(finalResult)


getData()
