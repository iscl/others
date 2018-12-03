import numpy as np

def test(value1, rate, totalnumber = 29501):
    temp1 = totalnumber - value1
    temp2 = np.floor(temp1 * rate)
    temp3 = temp1 - temp2
    return temp2, temp3

print(test(21999, 0.46))