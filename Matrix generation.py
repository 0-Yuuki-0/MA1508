import numpy as np
import matplotlib.pylab as plt
import operator
import requests
import sys

np.set_printoptions(threshold=sys.maxsize)

f = open('urls.txt', 'r')
x = list()
y = list()

urls = []
while True:
    url = f.readline().rstrip('\n')
    if url:
        urls.append(url)
    else:
        break


url_len = len(urls)
relation_matrix = np.zeros((url_len, url_len))
for i in range(0, url_len):
    try:
        r = requests.get(urls[i])
    except:
        print('timeout')
        continue
    print("{}/100".format(i))
    pattern = plt.re.compile(r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')')
    results = pattern.findall(r.content.decode('ISO-8859-1'))
    for j in range(0, url_len):
        if urls[j] in results:
            relation_matrix[i][j] = 1


for i in range(0, 100):
    for j in range(0, 100):
        if relation_matrix[i][j] == 1:
            x.append(i)
            y.append(j)


file = open('connection'+'.txt', 'w+')

file.write('in = [')
for i in range(0, len(x)):
    file.write(str(x[i]+1) + ' ')
file.write('];\n')

file.write('out = [')
for i in range(0, len(y)):
    file.write(str(y[i]+1) + ' ')
file.write('];\n')

file.write('urls = ' + str(list(urls)) + ';\n')

file.close()
