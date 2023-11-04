def binary_search(num_list,key,low,high):
    l=low
    h=high
    while(l<=h):
        mid=(l+h)//2
        if key==num_list[mid]:
            return mid
        elif key<num_list[mid]:
            h=mid-1
        else:
            l=mid+1
    return -1

num_list=[]
n=int(input('Enter the number of elements in list:'))
print('Enter the elements in the list')
for i in range(n):
    num_list.append(int(input()))
key=int(input('Enter the keys to be searched'))
low=0
high=len(num_list)-1
key_index=binary_search(num_list,key,low,high) 

if key_index==-1:
    print('The key is not found')
else:
    print('The key{} is found at index{}'.format(key,key_index))