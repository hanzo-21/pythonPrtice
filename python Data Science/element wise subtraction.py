# Replace ___ with your code
import numpy as np

# take list input from user
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

# create two numpy arrays
first = np.array(list1)
second = np.array(list2)

# use - to subtract the second array from first
diff = first-second
print(diff)

# use subtract() to subtract the second array from first
diff = np.subtract(first,second)

print(diff)