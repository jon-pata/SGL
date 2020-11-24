import csv
import os

original = open('weekCount.txt', 'r')

count = int(original.read())

original.close()

print(count)

count += 1

count = str(count)

print(count)
print(type(count))

updated = open('weekCount.txt', 'w')
updated.write(count)
updated.close()
