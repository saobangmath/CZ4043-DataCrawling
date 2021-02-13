import requests 
from bs4 import BeautifulSoup
import csv 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import argparse



pathToReviews = "/TripReviews.csv"
pathToStoreInfo = "/TripStoresInfo.csv"
resturls = ["https://www.tripadvisor.com/Restaurant_Review-g294265-d10453273-Reviews-Beast_Butterflies-Singapore.html", 
"https://www.tripadvisor.com/Restaurant_Review-g294265-d794020-Reviews-Hua_Ting_Restaurant-Singapore.html", 
"https://www.tripadvisor.com/Restaurant_Review-g294265-d5421216-Reviews-Fill_a_Pita-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d17171783-Reviews-Fu_Lin_Men_NSRCC-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d21180746-Reviews-Positano_RP-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d8571637-Reviews-Colony-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d3952172-Reviews-Waterfall_Ristorante_Italiano-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d1018167-Reviews-Paulaner_Brauhaus_Singapore-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d8504143-Reviews-Alma_By_Juan_Amador-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d13200545-Reviews-Publico_Ristorante-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d788966-Reviews-L_Angelus-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d5425405-Reviews-Mitsuba_Japanese_Restaurant-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d6899709-Reviews-The_Assembly_Ground_The_Cathay-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d7367295-Reviews-Prive_Chijmes-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d1756372-Reviews-Brasserie_Les_Saveurs-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d2011973-Reviews-LeVeL33-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d793312-Reviews-Gayatri_Restaurant-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d795586-Reviews-Wah_Lok-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d5980425-Reviews-Anti_dote-Singapore.html",
"https://www.tripadvisor.com/Restaurant_Review-g294265-d967412-Reviews-Garibaldi_Italian_Restaurant_Bar-Singapore.html"
]
maxRev = 100
m=0
arrlen = len(resturls)

def scrapeRestaurantInfo(url):
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    #find all details 
    ct= soup.findAll("div", {"class" : "_2170bBgV"})
    if not ct:
        ct= soup.findAll("div", {"class" : "_1XLfiSsv"})
    print(ct)
    #Store name h1 (div = _1hkogt_o)  
    storeName = soup.find('h1', class_='_3a1XQ88S').text
    #Averagage rating span (div = Ct2OcWS4)
    avgRating = soup.find('span', class_='r2Cf69qf').text.strip()
    #Store address (within div = _2vbD36Hr _36TL14Jn)
    storeAddress = soup.find('div', class_= '_2vbD36Hr _36TL14Jn').find('span', class_='_2saB_OSe').text.strip()
    #No of reviews (within div = Ct2OcWS4)
    noReviews = soup.find('a', class_='_10Iv7dOs').text.strip().split()[0]
    #Cuisines (within div = _1XLfiSsv)
    cuisineType = ct[1].string
    #Price Range (within div = _1XLfiSsv)
    priceRange = ct[0].string
    #Special diet (within div = _1XLfiSsv)
    specialDiet = ct[2].string
    #District (within div = _2vbD36Hr _36TL14Jn)
    district = soup.find('span', class_='_2saB_OSe _1OBMr94N').text.strip()
    #Scrape ratings for other values
    resultstab = soup.find('div', class_='ppr_rup ppr_priv_detail_overview_cards').find('div', class_='ui_columns')
    #print(resultstab)
    raterev = resultstab.find_all('div', class_='jT_QMHn2')
    ratearr = []
    #print(resultstab)
    #print(raterev)

    #print("I am NOT in the for loop")
    for rate in raterev:
        #print("I am in the for loop")
        bars = rate.find('span', class_='_377onWB-').findChildren('span')
        barval = str(bars[0]).split('_')[3]
        print("barval value "+barval[0]+"."+barval[1])
        barnew= barval[0]+"."+barval[1]
        ratearr.append(barnew)
        print(ratearr)
    #Write data to csv and export to file 
    with open(pathToStoreInfo, mode='a', encoding="utf-8") as trip:
        data_writer = csv.writer(trip, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        print(ratearr)
        if len(ratearr) == 3:
            data_writer.writerow([storeName, storeAddress, avgRating, noReviews, cuisineType, priceRange, specialDiet, district, ratearr[0], ratearr[1], ratearr[2], "0"])
        else:
            data_writer.writerow([storeName, storeAddress, avgRating, noReviews, cuisineType, priceRange, specialDiet, district, ratearr[0], ratearr[1], ratearr[2], ratearr[3]])
        print(url , " written to csv")

def scrapereviews():
    nextPage = 1
    while nextPage != maxRev:
        #Requests
        driver.get(resturls[m])
        time.sleep(1)
        #Click More button
        more = driver.find_elements_by_xpath("//span[contains(text(),'More')]")
        for x in range(0,len(more)):
            try:
                driver.execute_script("arguments[0].click();", more[x])
                time.sleep(3)
            except:
                pass
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #Store name
        storeName = soup.find('h1', class_='_3a1XQ88S').text
        #Store location 
        storeLoc = soup.find('div', class_= '_2vbD36Hr _36TL14Jn').find('span', class_='_2saB_OSe').text.strip()
        #Reviews
        results = soup.find('div', class_='listContainer hide-more-mobile')
        try:
            reviews = results.find_all('div', class_='prw_rup prw_reviews_review_resp')
        except Exception:
            continue
        #Export to csv
        try:
            with open(pathToReviews, mode='a', encoding="utf-8") as trip_data:
                data_writer = csv.writer(trip_data, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                for review in reviews:
                    ratingDate = review.find('span', class_='ratingDate').get('title')
                    text_review = review.find('p', class_='partial_entry')
                    if len(text_review.contents) > 2:
                        reviewText = str(text_review.contents[0][:-3]) + ' ' + str(text_review.contents[1].text)
                    else:
                        reviewText = text_review.text
                    reviewerUsername = review.find('div', class_='info_text pointer_cursor')
                    reviewerUsername = reviewerUsername.select('div > div')[0].get_text(strip=True)
                    rating = review.find('div', class_='ui_column is-9').findChildren('span')
                    rating = str(rating[0]).split('_')[3].split('0')[0]
                    data_writer.writerow([storeName, storeLoc, reviewerUsername, ratingDate, reviewText, rating])
                    nextPage += 1
                    print("Comment #" , nextPage , " for " , resturls[m])
                    if nextPage >= maxRev:
                        break
        except:
            pass
        #Go to next page if exists
        try:
            unModifiedUrl = str(soup.find('a', class_ = 'nav next ui_button primary',href=True)['href'])
            url = 'https://www.tripadvisor.com' + unModifiedUrl
        except:
            nextPage >= maxRev

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=chrome_options)

#print(resturls[m])

while m != arrlen:
    scrapeRestaurantInfo(resturls[m])
    m+=1 
m=0
while m != arrlen:
    scrapereviews()
    m+=1