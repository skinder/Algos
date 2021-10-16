'''
Write a method that does find a file in given directory
search for file in all subdirectories
search for a file with variable number of constraints(like size, creation-date, ends-with etc..)
'''

import os


def file_ops(path, target_file, size):
         # find a file in cur dir
         for filename in os.listdir(path):
             if filename == target_file:
                 return path + filename

         # find file in directory and subdirectory
         for path, _, file_list in os.walk(path):
             for filename in file_list:
                 if filename == target_file:
                     return path + directory

         # search for file with size greater than given size
         results = []
         for path, _, file_list in os.walk(path):
             for filename in file_list:
                 stat = os.stat(path + filename)
                 if stat.st_size > size:
                     results.append(path + filename)

         # search for a file with variable number of constraints
         # similarly use stat = os.stat, state.st_ctime etc