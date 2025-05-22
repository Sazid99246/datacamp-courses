import numpy as np

np_baseball = np.array([[7.400e+04, 1.800e+02, 2.299e+01],
                        [7.400e+01, 2.150e+02, 3.469e+01],
                        [7.200e+01, 2.100e+02, 3.078e+01],
                        [7.500e+01, 2.050e+02, 2.519e+01],
                        [7.500e+01, 1.900e+02, 3.101e+01],
                        [7.300e+01, 1.950e+02, 2.792e+01]])


avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))
