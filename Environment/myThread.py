from Individual.individual import  Individual
import time, threading

class MyThread(threading.Thread):
    def __init__(self, population = [], name = ""):
        threading.Thread.__init__(self)
        self.population = population
        self.name = name

    def run(self):
        self.population.append(Individual())
        self.name.exit()


