import threading
from random import randint
import time
import os

"""
globale Variablen für Höhe, Breite und sleep Time
"""
height = 100
width = 100
sTime = 0.5

class SnowflakeThread(threading.Thread):
    counter = 0
    lock = threading.Lock()

    def __init__(self):
        threading.Thread.__init__(self)
        self.__x = randint(0,width)
        self.__y = 0


    def run(self):
        while self.__y <= height:
            self.__y += randint(0,3)
            self.__x -= randint(-1,2)
            time.sleep(sTime)
        with SnowflakeThread.lock:
            SnowflakeThread.counter += 1

    def get_pos(self):
        return self.__x, self.__y

class Main():
    def draw(self):
        position = []
        for x in self.threads:
            position.append(x.get_pos())

        output = ""
        for y in range(height):
            for x in range(width):
                if (x,y) in position:
                    output += "*"
                else:
                    output += " "
            output += "\n"

        os.system("cls")

        print(output)


    def __init__(self,amount):
        self.threads = []
        for x in range(amount):
            self.threads.append(SnowflakeThread())

        for x in self.threads:
            x.start()

        while SnowflakeThread.counter < amount:
            self.draw()
            time.sleep(sTime)
        for kek in self.threads:
            kek.join()

if __name__ == '__main__':
    Main(300)