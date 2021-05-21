import numpy as np
# Ex.1 a
image = np.load("images/car_0.npy")
image1 = np.load("images/car_1.npy")
image2 = np.load("images/car_2.npy")
image3 = np.load("images/car_3.npy")
image4 = np.load("images/car_4.npy")
image5 = np.load("images/car_5.npy")
image6 = np.load("images/car_6.npy")
image7 = np.load("images/car_7.npy")
image8 = np.load("images/car_8.npy")

#Ex.1 b
array =  ([image,image1,image2,
          image3,image4,image5,
          image6,image7,image8])
sum = np.sum(array)
print(sum)

#Ex.1 c
for i in range (len(array)):
    every_elem = np.sum(array[i])
    print(every_elem)

max = np.argmax(array, axis=None, out=None)
print(max)