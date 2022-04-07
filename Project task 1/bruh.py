import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def birthday_paradox(n):
    number_of_students = []
    probabilities = []
    product = 1
    for k in range(1,n+1):
        product*= (365-k+1)/365
        number_of_students.append(k)
        probabilities.append(1-product)
        print(k, "=", 1 - product)
    return number_of_students, probabilities

birthday_paradox(14)