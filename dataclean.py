import numpy as np

    


#https://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list
def reject_outliers(data, m = 3):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s<m]

def list_avg(int_arr): #gets average of cleaned list
    return int(np.average(int_arr))

data = np.array([0, 0, -9, 400, 420, 450, 460, 455, 456, 1000])
cleaned = reject_outliers(data)
print(cleaned)
print(list_avg(cleaned))
