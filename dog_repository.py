import csv
f = '/home/luizf/anaconda3/python_learning/simple-mvc/dogs.csv'
from dog import Dog

class DogRepository:
    def __init__(self):
        self.dogs = []
        self.load_csv()

    def load_csv(self):
        f = '/home/luizf/anaconda3/python_learning/simple-mvc/dogs.csv'
        with open(f, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                dog = Dog(row[0], row[1])
                self.dogs.append(dog)

    def all_dogs(self):
        return self.dogs
