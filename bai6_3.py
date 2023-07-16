# Data Structure Exercise - Exercise 3: Slice list into 3 equal chunks and reverse each chunk
def slice3(a):
    la = len(a)
    lchunk = int(la/3)
    lchunknext = lchunk*2
    chunk1 = a[0:lchunk]
    chunk1.reverse()
    chunk2 = a[lchunk:lchunknext]
    chunk2.reverse()
    chunk3 = a[lchunknext:la]
    chunk3.reverse()
    print("chunk1: ", a[0:lchunk], ", chunk1 reverse: ", chunk1)
    print("chunk2: ", a[lchunk:lchunknext], ", chunk2 reverse: ", chunk2)
    print("chunk3: ", a[lchunknext:la], ", chunk3 reverse: ", chunk3)
    
slice3([11, 45, 8, 23, 14, 12, 78, 45, 89])