#----------------------SPECIALIZED SORTS----------------------

#BUBBLE SORT:

##Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
##
##This algorithm is not suitable for large data sets as its average and worst case time complexity is quite high.
##
##var=[5,2,12,3,8,6]
##for x in range(0,len(var)-1):
##    for y in range(len(var)-1):
##        if (var[y]>var[y+1]):
##            var[y],var[y+1]=var[y+1],var[y]
##print(var)


#MERGE SORT:


def merge_sort(a):
    if (len(a)>1):
        mid=len(a)//2
        L=a[:mid]
        R=a[mid:]
        merge_sort(L)
        merge_sort(R)
        a.clear()
        while (len(L)>0 and len(R)>0):
            if(L[0]<=R[0]):
                a.append(L[0])
                L.pop(0)
            else:
                a.append(R[0])
                R.pop(0)
        for x in L:
            a.append(x)
        for y in R:
            a.append(y)
a=[10,7,12,5,30]
merge_sort(a)
print(a)



#INSERTION SORT:
##IT IS just like bubble sort
##in bubble sort it will compare one by one element:::
##but in insertion sort it will compare to the previous values

a=[44,16,83,7,67,21]
for x in range(1,len(a)):
    key=a[x]
    y=x-1
    while(y>=0 and key <a[y]):
      a[y+1]=a[y]
      y=y-1
    else:
        a[y+1]=key
print(a)


#selection sort:

##10 14 27 33 35 19 42 44
##10 14 19 33 35 27 42 44
##10 14 19 27 35 33 42 44
##10 14 19 27 35 33 42 44
##10 14 19 27 33 35 42 44
##10 14 19 27 33 35 42 44
##10 14 19 27 33 35 42 44


def selection_sort(a):
    length=len(a)
    for x in range(length-1):
        min=x
        for y in range(x+1 ,length):
            if (a[y]<a[min]):
                min=y
        a[x],a[min]=a[min],a[x]
    return a
a=[10,14,27,33,35,19,42,44]
print(selection_sort(a))
