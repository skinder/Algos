
#
#  Storage cleanup.
#
#     We have a list of server information logs in a directory, these information logs are collected in different days
#     for different servers, and the file format will be:
#
#          server_id@YYYY-MM-DD.csv
#
#     We want to remove some of the old files to save the space, requirements:
#
#       1. Keep at least one most recent report for each server
#       2. For the rest, delete them if they are older than 90 days
#
import collections defaultdict
# sample input
files = [
        'sk-0108dcc8-095e-4f89-9192-8516698966cd@2020-12-25.csv',
        'sk-111b7e39-b3f9-49aa-89f8-2309bab8c215@2021-1-24.csv',
        'sk-1bb6b675-14ed-43ac-8a88-08b644d8610a@2020-12-23.csv'
        'sk-111b7e39-b3f9-49aa-89f8-2309bab8c215@2021-1-12.csv',
        'sk-1bb6b675-14ed-43ac-8a88-08b644d8610a@2020-12-21.csv'
]

# return a list of files to remove
def calculate_delete_candidates(files):
        save_list = []
        output = []
        dict = defaultdict()
        for file in files:
                server_id = file.split("@")[0]
                date = file.split("@")[1].split(".")[0]
                if date > (today - 90days):
                    save_list.append(file)
                elif: server_id in dict and dict[server_id] < date:
                        dict[server_id] = date
                elif server_id not in dict:
                        dict[server_id] = date

        for fl in files:
          if fl not in save_list:
                if dict[fl.split("@")[0]] != fl.split("@")[1].split(".")[0]:
                        output.append(fl)