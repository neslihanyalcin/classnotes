import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('biometric_data_simple.txt',delimiter=',')
data = data[:,1:3]
ca = np.array([6, 11, 12, 23, 24, 34, 38, 41, 44, 45, 47, 50, 53, 55, 56, 60, 62, 67, 71, 76, 77, 78, 85, 98, 99, 100, 101, 102, 104, 106, 116, 117, 118, 125, 126, 127, 129, 130, 131, 136, 141, 144, 150, 155, 160, 167, 169, 173, 184, 188, 191, 199, 204, 205, 206, 207, 209])
cb = np.array([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 39, 40, 42, 43, 46, 48, 49, 51, 52, 54, 57, 58, 59, 61, 63, 64, 65, 66, 68, 69, 70, 72, 73, 74, 75, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 103, 105, 107, 108, 109, 110, 111, 112, 113, 114, 115, 119, 120, 121, 122, 123, 124, 128, 132, 133, 134, 135, 137, 138, 139, 140, 142, 143, 145, 146, 147, 148, 149, 151, 152, 153, 154, 156, 157, 158, 159, 161, 162, 163, 164, 165, 166, 168, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 185, 186, 187, 189, 190, 192, 193, 194, 195, 196, 197, 198, 200, 201, 202, 203, 208])
women = data[ca]
print women
men = data[cb]
print men
plt.plot (women[:,1],women[:,0], 'b.')
plt.hold(True)
plt.plot (men[:,1],men[:,0], 'r.')
plt.show()