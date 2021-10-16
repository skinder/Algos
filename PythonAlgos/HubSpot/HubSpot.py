import requests
from datetime import datetime

api_data = requests.get('https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=2ccd73e4e0b35ea611dd0a98f1da')
json_data = api_data.json()
partners = json_data['partners']


def get_start_dates(dates):
    """
    :param dates: sorted list of dates
    :return: list of starting dates of the two day period
    """
    start_dates = []
    for i in range(len(dates)-1):
        curr_date = datetime.strptime(dates[i], "%Y-%m-%d")
        next_date = datetime.strptime(dates[i+1], "%Y-%m-%d")
        if abs((next_date - curr_date).days) == 1:
            start_dates.append(dates[i])
    return start_dates


# Collect: Country->startDate->list of emails
agg_data = dict()
for partner in partners:
    dates = partner['availableDates']
    country = partner['country']
    agg_data[country] = agg_data.get(country, {})
    for date in get_start_dates(sorted(dates)):
        agg_data[country][date] = agg_data[country].get(date, [0, []])
        agg_data[country][date][0] += 1
        agg_data[country][date][1].append(partner['email'])


# get max number of attendees for each country
for country in agg_data:
    max_cnt = 0
    cnt_emails = [None, []]
    start_date = None
    for date in agg_data[country]:
        if agg_data[country][date][0] > max_cnt:
            max_cnt = agg_data[country][date][0]
            start_date = date
            cnt_emails = agg_data[country][date]
    agg_data[country] = (start_date, cnt_emails)


# prepare output data
output_json_data = {}
output_json_list = []
for country in agg_data:
    output_data = {'attendeeCount': agg_data[country][1][0], 'attendees': agg_data[country][1][1], 'name': country,
                   'startDate': agg_data[country][0]}
    output_json_list.append(output_data)

output_json_data['countries'] = output_json_list

send_post_request = requests.post('https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey'
                                  '=2ccd73e4e0b35ea611dd0a98f1da', json=output_json_data)

print(send_post_request.json())



