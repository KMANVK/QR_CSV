import csv
import matplotlib.pyplot as plt
import numpy as np

matrix = np.zeros((29,29))
with open('secret.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        coords = row[0].split(',')
        matrix[int(coords[0]), int(coords[1])] = 1

plt.imshow(matrix, cmap='gray')
plt.show()