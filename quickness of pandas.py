'''
Operating on NumPy arrays is a lot more efficient than operating on Python objects. 
There are two big factors that contribute to this:
1) It takes longer to add 1 to a number in pure Python than in NumPy:
      - Python doesn’t know until runtime that the number is an integer:
            - It must check for each number what its data type is and hence how to compute “x + 1.” 
2) The Python data structure takes up a lot more space compared to the NumPy array:
      - it must also carry around metadata that specifies what data type each list element is. => 
            ... you fill up the high levels of cache faster in Python than in NumPy

'''           



import time, numpy as np, matplotlib.pyplot as plt

def time_numpy(n): # time required to increment all elements of a list of numbers for a NumPy array
    a = np.arange(n)
    start = time.time()
    bigger = a + 1
    stop = time.time()
    return stop - start

def time_python(n): # time required to increment all elements of a list of numbers for a Python list
    l = range(n)
    start = time.time()
    bigger = [x+1 for x in l]
    stop = time.time()
    return stop - start

n_trials = 10
ns = range(20, 500)
ratios = []
for n in ns:
    python_total = sum([time_python(n) for _ in range(n_trials)]) 
    numpy_total = sum([time_numpy(n) for _ in range(n_trials)])
    ratios.append(python_total / numpy_total)
    
plt.plot(ns, ratios)
plt.xlabel("Length of List / Array")
plt.ylabel("Python / Numpy Ratio")
plt.title("Relative Speed of Numpy vs Pure Python")
plt.show()
