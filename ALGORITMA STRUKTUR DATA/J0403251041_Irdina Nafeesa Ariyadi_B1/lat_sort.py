a = [1,2,5,8,3,10]
a.sort()
print(a)

#bubble
def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
# Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
data = [8,5,11,4,7]
bubbleSort(data)
print(data)
