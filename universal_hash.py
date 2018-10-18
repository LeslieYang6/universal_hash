import random
#计算以ｍ为ｂａｓｅ的向量
def getbasemn(a,m):
    p=[]
    while a!=0:
        p.append(a%m)
        a=a/m
    return p

#根据任意的ａ确定任意的hash的函数


#插入元素，保证
def insert(table,p,key):
    if table[p] is None:
        table[p]=[key]
    else:
        table[p].append(key)

#初始化hash_table
def initializing(table):
    for i in range(503):
        table.append(None)

#得到random hash function
def hash_(array):
    a=88888890
    def universal_hash(b, m):
        vector1 = getbasemn(a, m)
        vector2 = getbasemn(b, m)
        length1 = len(vector1)
        length2 = len(vector2)
        offset = abs(length1 - length2)
        if length1 > length2:
            for i in range(offset):
                vector2.append(0)
        if length1 < length2:
            for i in range(offset):
                vector1.append(0)
        length = len(vector1)
        p = 0
        for i in range(length):
            p = p + vector1[i] * vector2[i]
        p = p % m
        return int(p)
    return universal_hash



def main():
    m=503
    array=[]
    for i in range(500):
        array.append(i+88888888)
    table=[]
    initializing(table)
    for i in range(500):
        insert(table,hash_(array)(array[i],m),array[i])
    k=0
    for i in range(500):
        if table[i]is not None and len(table[i])==1:
            k+=1
    print(k)



main()









