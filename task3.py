import glob
import sys
import os

files = []
for filename in glob.glob('cash*.txt'):
    files.append(filename)

count = 0
data_array = []
while len(files)!= count:
    file = open(files[count])
    file_read = file.read().splitlines()
    file.close()
    transform_file = [float(index) for index in file_read]
    data_array.append(transform_file)
    count += 1

index = 0
sum_intervals=[]
while index != len(data_array[0]):
    sum_intervals.append(data_array[0][index]+data_array[1][index]+data_array[2][index]+data_array[3][index]+data_array[4][index])
    index += 1
num_interval = [(x+1) for x in range(len(sum_intervals))if sum_intervals[x] == max([elem for elem in sum_intervals])]
print(num_interval)


