# -*- coding: utf-8 -*-
"""(Year) GenderPronoun - Time Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hTrXh3PmfZcVwcPsQdKjvt3lfzgH1yuM
"""

import json
import time
import glob
import gzip
from datetime import datetime 
import re
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import collections


SAMPLE_FILE = "ENTER THE PATH OF YOUR SAMPLE FILE"



#This part shows how many unique ids there are in the sample file.

id_year_dict = dict()
with open(SAMPLE_FILE_15, "r") as sample:
  for line in sample:
    dpoint = json.loads(line)
    dt_object = datetime.fromtimestamp(dpoint["current_tweet_timestamp"])
    year = str(dt_object)[0:4]
    id_year_dict[str(dpoint["id_str"])] = year

print("The number of unique ids in the sample file", len(id_year_dict))

#YEAR
id_year = []
with open(SAMPLE_FILE, "r") as sample:
  for line in sample:
    dpoint = json.loads(line)
    dt_object = datetime.fromtimestamp(dpoint["current_tweet_timestamp"])
    year = str(dt_object)[0:4]
    a = (str(dpoint["id_str"]), year, str(dpoint["description"]) )
    id_year.append(a)
#id_year is a list with id:year tuple pairs. - because dictionary requires unique keys
sorted_id_year = sorted(id_year, key=lambda x: x[1])

#sorts id_year dict ascending - result is list of tuples.

#Categorizes ids according to their creation year.
ids_2011 = list()
ids_2012 = list()
ids_2013 = list()
ids_2014 = list()
ids_2015 = list()
ids_2016 = list()
ids_2017 = list()
ids_2018 = list()
ids_2019 = list()
ids_2020 = list()

for item in sorted_id_year:
  if item[1] == "2011":
    ids_2011.append(item)
  elif item[1] == "2012":
    ids_2012.append(item)
  elif item[1] == "2013":
    ids_2013.append(item)
  elif item[1] == "2014":
    ids_2014.append(item) 
  elif item[1] == "2015":
    ids_2015.append(item)
  elif item[1] == "2016":
    ids_2016.append(item)
  elif item[1] == "2017":
    ids_2017.append(item)
  elif item[1] == "2018":
    ids_2018.append(item)
  elif item[1] == "2019":
    ids_2019.append(item)
  else:
    ids_2020.append(item)
  
ids_list = [ids_2011, ids_2012, ids_2013, ids_2014, ids_2015, ids_2016, ids_2017, ids_2018, ids_2019, ids_2020]

#dictionaries to keep year:count pairs.

data_she = []
data_he = []
data_they = []
data_ze = []
data_xe = []
data_sie = []

#Regex codes to detect pronouns in the text and descriptions.
she_regex = r"(\sshe\sher\shers\s)|(\sshe\sher\s)"
he_regex = r"(\she\shim\shis\s)|(\she\shim\s)"
they_regex = r"(\sthey\sthem\s)|(\sthey\sthem\stheirs\s)"
ze_regex = r"(\sze\szir\szirs\s)|(\sze\szir\szis\s)|(\sze\szir\s)"
xe_regex = r"(\sxe\sxem\sxir\s)|(\sxe\sxem\sxirs\s)|(\sxe\sxem\s)"
sie_regex = r"(\ssie\shir\shirs\s)|(\ssie\shir\s)"

regex_list = [she_regex, he_regex, they_regex, ze_regex, xe_regex, sie_regex]

def check_regex(regex_type, line):
  match = re.search(regex_type, line, re.MULTILINE | re.IGNORECASE)
  if match == None:
    return False
  else:
    return True

#The lists that keep the unique ids' that include corresponding pronound in their description field.
unique_she = []
unique_he = []
unique_they = []
unique_ze = []
unique_xe = []
unique_sie = []


#she
for year_list in ids_list:
  count = 0
  if len(year_list) == 0:
    continue
  else:
    for line in year_list:
      if line[0] not in unique_she:
        check = check_regex(she_regex, line[2])
        if check == True:
          unique_she.append(line[0])
          count +=1
        else:
          continue
      else:
        continue
    data_she.append((str(year_list[0][1]), count))

#he
for year_list in ids_list:
  count = 0
  if len(year_list) == 0:
    continue
  else:
    for line in year_list:
      if line[0] not in unique_he:
        check = check_regex(he_regex, line[2])
        if check == True:
          unique_he.append(line[0])
          count +=1
        else:
          continue
      else:
        continue
    data_he.append((str(year_list[0][1]), count))

#they
for year_list in ids_list:
  count = 0
  if len(year_list) == 0:
    continue
  else:
    for line in year_list:
      if line[0] not in unique_they:
        check = check_regex(they_regex, line[2])
        if check == True:
          unique_they.append(line[0])
          count +=1
        else:
          continue
      else:
        continue
    data_they.append((str(year_list[0][1]), count))

#ze
for year_list in ids_list:
  count = 0
  if len(year_list) == 0:
    continue
  else:
    for line in year_list:
      if line[0] not in unique_ze:
        check = check_regex(ze_regex, line[2])
        if check == True:
          unique_ze.append(line[0])
          count +=1
        else:
          continue
      else:
        continue
    data_ze.append((str(year_list[0][1]), count))
  
#xe
for year_list in ids_list:
  count = 0
  if len(year_list) == 0:
    continue
  else:
    for line in year_list:
      if line[0] not in unique_xe:
        check = check_regex(xe_regex, line[2])
        if check == True:
          unique_xe.append(line[0])
          count +=1
        else:
          continue
      else:
        continue
    data_xe.append((str(year_list[0][1]), count))
  
#sie
for year_list in ids_list:
  count = 0
  if len(year_list) == 0:
    continue
  else:
    for line in year_list:
      if line[0] not in unique_sie:
        check = check_regex(sie_regex, line[2])
        if check == True:
          unique_sie.append(line[0])
          count +=1
        else:
          continue
      else:
        continue
    data_sie.append((str(year_list[0][1]), count))


#This part creates a table by using Pandas to indicate the total number of each pronoun usage for each year. 
count_table = pd.DataFrame(data_she, columns=['year', 'she'])
count_table.insert(2, "he", [data_he[0][1], data_he[1][1], data_he[2][1], data_he[3][1], data_he[4][1], data_he[5][1], data_he[6][1], data_he[7][1], data_he[8][1], data_he[9][1]], True)
count_table.insert(3, "they", [data_they[0][1], data_they[1][1], data_they[2][1], data_they[3][1], data_they[4][1], data_they[5][1], data_they[6][1], data_they[7][1], data_they[8][1], data_they[9][1]], True)
count_table.insert(4, "ze", [data_ze[0][1], data_ze[1][1], data_ze[2][1], data_ze[3][1], data_ze[4][1], data_ze[5][1], data_ze[6][1], data_ze[7][1], data_ze[8][1], data_ze[9][1]], True)
count_table.insert(5, "xe", [data_xe[0][1], data_xe[1][1], data_xe[2][1], data_xe[3][1], data_xe[4][1], data_xe[5][1], data_xe[6][1], data_xe[7][1], data_xe[8][1], data_xe[9][1]], True)
count_table.insert(6, "sie", [data_sie[0][1], data_sie[1][1], data_sie[2][1], data_sie[3][1], data_sie[4][1], data_sie[5][1], data_sie[6][1], data_sie[7][1], data_sie[8][1], data_sie[9][1]], True)
count_table['Total by Year'] = count_table.sum(axis=1)
print(count_table)
print("The sum of the total number of users that use pronoun in their description for each year", sum(count_table["Total by Year"]))

#The scatter plot of the total number of unique ids for each year for each pronoun. Each line in the chart signifies a pronoun as is stated in the legend. 
x_she_val = [i[0] for i in data_she]
y_she_val = [i[1] for i in data_she]

x_he_val = [i[0] for i in data_he]
y_he_val = [i[1] for i in data_he]

x_they_val = [i[0] for i in data_they]
y_they_val = [i[1] for i in data_they]

x_ze_val = [i[0] for i in data_ze]
y_ze_val = [i[1] for i in data_ze]

x_xe_val = [i[0] for i in data_xe]
y_xe_val = [i[1] for i in data_xe]

x_sie_val = [i[0] for i in data_sie]
y_sie_val = [i[1] for i in data_sie]

plt.xlabel("Year")
plt.ylabel("# of unique users")

plt.plot(x_she_val,y_she_val, label="she/her/hers")
plt.plot(x_he_val,y_he_val, label="he/him/his")
plt.plot(x_they_val,y_they_val, label="they/them/theirs")
plt.plot(x_ze_val,y_ze_val, label="ze/zir/zirs")
plt.plot(x_xe_val,y_xe_val, label="xe/xem/xir")
plt.plot(x_sie_val,y_sie_val, label="sie/hir/hirs")
plt.legend()
fig = plt.gcf()
fig.set_size_inches(16.5, 8.5)
plt.show()
