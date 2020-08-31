import csv
f = '/home/luizf/anaconda3/python_learning/simple-mvc/dogs.csv'
with open(f, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print("Dog name:{} | Dog color:{}".format(row[0], row[1]))


