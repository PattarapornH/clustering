from random import randint
import csv

with open('data5.csv', 'w') as csvfile:
    field = ['V1','V2']
    filewriter = csv.DictWriter(csvfile,fieldnames = field)
    filewriter.writeheader()
    for i in range(0,3000):
        tmp = randint(1,7)
        if tmp == 1:
            x = randint(0,806)
            y = randint(1200,1287)
            filewriter.writerow({'V1': x, 'V2': y})
        elif tmp == 2:
            x = randint(200,858)
            y = randint(1000,1111)
            filewriter.writerow({'V1': x, 'V2': y})
        elif tmp == 3:
            x = randint(200,1403)
            y = randint(2000,2493)
            filewriter.writerow({'V1': x, 'V2': y})
        else:
            x = randint(0,2500)
            y = randint(0,2500)
            filewriter.writerow({'V1': x, 'V2': y})