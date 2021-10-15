import sys
import datetime
import requests
import json
import time
import os
from collections import namedtuple

URI = "http://wukong-api2.las.prod.hulu.com/v2/history/"
URI_PARAMETERS = "?offset=0&size=100&desc=true"
URI_FAIL_PARAMETERS = "?offset=0&size=20&desc=true&status=FAILURE"
current_time = datetime.datetime.utcnow()
Jobs_in_param = namedtuple("jobs_in_param", "job_name parent_job_name job_id parent_job_id "
                                            "max_absolute_delay max_relative_delay max_failures "
                                            "failure_check_time")
Jobs_calc_param = namedtuple("jobs_calc_param", "absolute_delay_hrs relative_delay_hrs "
                                                "absolute_delay_status relative_delay_status "
                                                "failure_count failure_status")

def calculate_harmony_delay_for_job(job_id):
    query = URI + job_id + URI_PARAMETERS
    response = requests.get(query)
    response.raise_for_status()
    last_not_completed_hour = sys.maxsize
    last_success_hour = 0
    check_list = []
    for (target) in json.loads(response.text).get("taskStatus"):
        status = target.get("status")
        task_time = target.get("taskTimeUtc")

        # print "task_time:{}, status:{}".format(task_time, status)
        if status == "REVISION":
            continue

        if task_time not in check_list:
            check_list.append(task_time)
        else:
            continue

        if status != "SUCCESS":
            last_not_completed_hour = min(last_not_completed_hour, task_time)
        else:
            last_success_hour = max(last_success_hour, task_time)

        # print "last_not_completed_hour:{}, last_success_hour:{}".format(last_not_completed_hour, last_success_hour)

    # every job success, no last_not_completed_hour found

    if last_not_completed_hour == sys.maxsize:
        last_not_completed_hour = current_time.strftime("%Y%m%d%H%M")

    return last_not_completed_hour


# print(calculate_harmony_delay_for_job('13203'))

