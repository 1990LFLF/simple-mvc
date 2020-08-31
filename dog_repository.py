import csv
f = '/home/luizf/anaconda3/python_learning/simple-mvc/dogs.csv'
from dog import Dog

class DogRepository:
    def __init__(self):
        self.dogs = []

    def load_csv(self):
        f = '/home/luizf/anaconda3/python_learning/simple-mvc/dogs.csv'
        with open(f, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                dog = Dog(row[0], row[1])
                self.dogs.append(dog)

dog_repo = DogRepository()

dog_repo.load_csv()

for i in range(len(dog_repo.dogs)):
    print("{} - {} | {}".format(i+1, dog_repo.dogs[i].name, dog_repo.dogs[i].color))
