import csv
import requests
from bs4 import BeautifulSoup

#PROGRAM DESCRIPTION
#The following program is a web scrapper used to collect business information via YellowPages
#You enter what it is that you are looking for, along with the city and state
#It queries YellowPages and print out results that meet the requirements
#TO-DO LIST
#Add save function that will save data in CSV format for spreadsheet usage
#Allow user to gather results on more than just the first page returned by YellowPages

def scrapePage(thing, city, state):
    print("Generating list, please wait. . .")

    url = "http://www.yellowpages.com/search?search_terms={}&geo_location_terms={}%2C+{}".format(thing, city, state)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    print("\n" * 100)

    business_info = soup.find_all("div", {"class": "info"})
    for item in business_info:
        try:
           businessName = item.contents[0].find_all("a", {"class": "business-name"})[0].text
           streetAddress = item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
           city = item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replace(',','')
           state = item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text
           zipcode = item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
           phone = item.contents[1].find_all("div", {"itemprop": "telephone"})[0].text
           print(businessName,streetAddress,city,state,zipcode,phone,'------------------------------------------',sep="\n")
        except:
            pass

def saveData(thing, city, state):
    url = "http://www.yellowpages.com/search?search_terms={}&geo_location_terms={}%2C+{}".format(thing, city, state)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    business_info = soup.find_all("div", {"class": "info"})
    fileName = thing+'_'+city+'_'+state+'.csv'

    with open(fileName, 'w', newline='') as csvfile:
        fieldnames = ['Business', 'Address', 'City', 'State', 'Zipcode', 'Phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in business_info:
            try:
               businessName = item.contents[0].find_all("a", {"class": "business-name"})[0].text
               streetAddress = item.contents[1].find_all("span", {"itemprop": "streetAddress"})[0].text
               city = item.contents[1].find_all("span", {"itemprop": "addressLocality"})[0].text.replace(',','')
               state = item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text
               zipcode = item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
               phone = item.contents[1].find_all("div", {"itemprop": "telephone"})[0].text
               writer.writerow({'Business': businessName, 'Address': streetAddress, 'City': city, 'State': state, 'Zipcode': zipcode, 'Phone': phone})
            except:
                pass

thing = input("What are you looking for?")
city = input("What city would you like to check?")
state = input("What state is {} in?".format(city))
scrapePage(thing,city,state)
save = input("Would you like to save this data to CSV file? (Y/N)")
if save == "Y":
  saveData(thing,city,state)
else:
  pass