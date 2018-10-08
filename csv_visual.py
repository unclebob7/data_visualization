import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = "univ_temp.csv"

#with open(filename, encoding='utf-8', mode = ‘r') as f:
with open(filename,encoding='utf-8',mode='r') as f:
    item = csv.reader(f)
    tag = next(item)

    univ_item,qoe,alumni_employment = [],[],[]
    for row in item:
        univ_item.append(row[1])
        qoe.append(row[4])
        alumni_employment.append(row[5])
    fig = plt.subplots()
    plt.plot(univ_item,qoe,c='red')
    plt.plot(univ_item,alumni_employment,c='blue')
    plt.title("university assessment")
    plt.xlabel('',fontsize='5')
    plt.xticks(rotation=90)
    plt.show()
