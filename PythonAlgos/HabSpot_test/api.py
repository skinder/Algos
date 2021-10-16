import requests
from datetime import datetime

partner_data = requests.get('https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=68d9d7827b0710e4da5f61c1a18a')

partner_json = partner_data.json()
partners = partner_json['partners']

# first we need to find if dates are consecutive by isConsecutive(date1,date2) =&gt; abs(date2-date1)==1
def isConsecutive(date1,date2):
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((date2 - date1).days) == 1


# gives us a dictionary of consecutive dates {'21_22':2} date1_date2:times-observed
def isConsecutiveDates(dates):
    consecutiveData = {}
    for i in range(len(dates)-1):
        date1,date2 = dates[i],dates[i+1]
        if isConsecutive(date1,date2):
            date_key = '_'.join([date1,date2])
            consecutiveData[date_key] = consecutiveData.get(date_key,0) + 1
    return consecutiveData

#make list of attendees from countryDict
def getAttendees(countryDict):
    countryAttendees = countryDict[1][1]
    attendeeEmails = []
    for attendee in countryAttendees:
        attEmail = attendee.get('email')
        attendeeEmails.append(attEmail)
    return attendeeEmails

#get start date from countryDict
def getStartDate(countryDict):
    if countryDict[0] is None:
        return None
    dateConcat = countryDict[0]
    newDate = dateConcat.split('_')[0]
    return newDate

#for each partner we get a dictionary of date and count so we must add it to a country-wide dictionary where
# {country:{date_1: [n,[partner_dict1...partner_dictn]]}
countryDict = dict()
for dct in partners:
    dates = dct['availableDates']
    dates = sorted(dates, key=lambda d: tuple(map(int, d.split('-'))))
    consecutiveDates = isConsecutiveDates(dates)
    country = dct['country']
    #build our countryWide dictionary
    countryDict[country] = countryDict.get(country,{})
    for date in consecutiveDates:
        countryDict[country][date] = countryDict[country].get(date,[0,[]])
        countryDict[country][date][0] += 1
        countryDict[country][date][1].append(dct)

#get max element for each country from countryDict and change countryDict to contain data from
# only that date for each country
for country in countryDict:
    maxEl = 0
    maxData = [None,[]]
    max_date = None
    for date in countryDict[country]:
        if countryDict[country][date][0] > maxEl:
            maxEl = countryDict[country][date][0]
            maxData = countryDict[country][date]
            max_date = date
    countryDict[country] = (max_date,maxData)

#build json dictionary for posting to api endpoint
jsonData = {}
jsonList = []
for country in countryDict:
    newDict = {}
    newDict['attendeeCount'] = countryDict[country][1][0]
    newDict['attendees'] = getAttendees(countryDict[country])
    newDict['name'] = country
    newDict['startDate'] = getStartDate(countryDict[country])
    jsonList.append(newDict)

jsonData['countries'] = jsonList
r = requests.post('https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=68d9d7827b0710e4da5f61c1a18a',
              json = jsonData
              )
#print the status of our post request
print(r.json())