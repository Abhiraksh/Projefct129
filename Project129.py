import pandas
import csv

df = pandas.read_csv("Project127.csv")
df = df.dropna()
df = df.drop_duplicates()

for i in df:
    try:
        df["radius"][i] *= 0.102763
        df["mass"][i] *= 0.000954588
    except:
        continue

df.to_csv("data1.csv", index=False)

del df

df = pandas.read_csv("Project128.csv")
df = df.dropna()
df = df.drop_duplicates()

# print(len(df))

for k in df:
    try:
        df["radius"][k] *= 0.102763
        df["mass"][k] *= 0.000954588
    except:
        continue

df.to_csv("data2.csv", index=False)

del df

dataset1 = []
dataset2 = []

with open("data1.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset1.append(row)

with open("data2.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset2.append(row)

header1 = dataset1[0]
header2 = dataset2[0]

planetData1 = dataset1[1:]
planetData2 = dataset2[1:]

headers = header1 + header2
# print(planetData2)

planetData = []

# for index,dataRow in enumerate(planetData1):
#     planetData.append(planetData1[index-1]+planetData2[index-1])

for i in planetData1:
    planetData.append(i)

for i in planetData2:
    planetData.append(i)

print(planetData)
with open("finalResult.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)