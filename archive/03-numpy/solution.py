import numpy as np

# 1. Create an array of 10 zeros
arr1 = np.zeros(10)
print(arr1)

# 2. Create an array of 10 ones
arr2 = np.ones(10)
print(arr2)

# 3. Create an array of 10 fives
arr3 = np.ones(10) * 5
print(arr3)

# 4. Create an array of the integers from 10 to 50
arr4 = np.arange(10, 51)
print(arr4)

# 5. Create an array of all the even integers from 10 to 50
arr5 = np.arange(10, 51, 2)
print(arr5)

# 6. Create a 3x3 matrix with values ranging from 0 to 8
arr6 = np.arange(0, 9).reshape(3, 3)
print(arr6)

# 7. Create a 3x3 identity matrix
arr7 = np.eye(3)
print(arr7)

# 8. Use NumPy to generate a random number between 0 and 1
arr8 = np.random.rand(1)
print(arr8)

# 9. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
arr9 = np.random.randn(25)
print(arr9)

# 10. Create the following matrix:
arr10 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(arr10)

# 11. Create an array of 20 linearly spaced points between 0 and 1:
arr11 = np.linspace(0, 1, 20)
print(arr11)

# 12. Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
arr12 = np.arange(1, 26).reshape(5, 5)
print(arr12)

# 13. Get the sum of all the values in mat
arr13 = np.sum(arr12)
print(arr13)

# 14. Get the standard deviation of the values in mat
arr14 = np.std(arr12)
print(arr14)

# 15. Get the sum of all the columns in mat
arr15 = np.sum(arr12, axis=0)
print(arr15)

# 16. Get the sum of all the rows in mat
arr16 = np.sum(arr12, axis=1)
print(arr16)

# 17. Get the sum of all the values in mat
arr17 = np.sum(arr12)
print(arr17)

# 18. Get the sum of all the values in mat
arr18 = np.sum(arr12)
print(arr18)

# 19. Get the sum of all the values in mat
arr19 = np.sum(arr12)
print(arr19)

# 20. Get the sum of all the values in mat
arr20 = np.sum(arr12)
print(arr20)
