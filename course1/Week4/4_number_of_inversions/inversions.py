# Uses python3
import sys

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     for i in range(left,ave):
#         for j in range(ave,right):
#             if a[i]>a[j]:
#                 a[i],a[j]=a[j],a[i]
#                 number_of_inversions+=1
#
#
#     return number_of_inversions
# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions = get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     number_of_inversions += merge(a,b,left,right)
#     return number_of_inversions

# def merge(a,b,left,right):
# 	mid = (left+right)//2
#
# 	#1st while loop runs as long as any subarray has
# 	#elements left and inversion occurs if a[i] > a[j]
# 	#no of inversions is mid - j
# 	inv_count = 0
# 	i=left
# 	j=mid
# 	k=left
# 	while i<mid and j<right:
# 		if a[i]<=a[j]:
# 			#no inversion
# 			b[k] = a[i]
# 			i+=1
# 			k+=1
# 		else : #inversion occurs
# 			inv_count+=mid-i
# 			b[k] = a[j]
# 			k+=1
# 			j+=1
#
#
# 	while i<mid :
# 		b[k] = a[i]
# 		i+=1h
# 		k+=1
# 	while j<right :
# 		b[k] = a[j]
# 		k+=1
# 		j+=1
#
# 	for ind in range(left,right):
# 		a[ind] = b[ind]
#
#
# 	return inv_count

# if __name__ == '__main__':
#     input = sys.stdin.read()
def merge (a,b,l,mid,h):
	i=l
	j=mid+1
	k=l
	count=0
	while i<=mid and j<=h:
		if a[i]<=a[j]:
			b[k]=a[i]
			i+=1
			k+=1
		else:
			count+=(mid-i)+1
			b[k]=a[j]
			j+=1
			k+=1
	# print(b,k,i)
	while i<=mid:
		b[k]=a[i]
		i+=1
		k+=1
	while j<=h:
		# print(k,i,a,b)
		b[k]=a[j]
		j+=1
		k+=1
	for idx in range(l,h+1):
		a[idx]=b[idx]
	return count
#
def get_number_of_inversions(a,b,l,h):
	count=0
	if l<h:
		mid= (h+l)//2
		count+=get_number_of_inversions(a,b,l,mid)
		count+=get_number_of_inversions(a,b,mid+1,h)
		count+= merge(a,b,l,mid,h)
	print(a,b)
	return count
# def get_number_of_inversions(arr, temp_arr, left, right):
#
#     # A variable inv_count is used to store
#     # inversion counts in each recursive call
#
#     inv_count = 0
#
#     # We will make a recursive call if and only if
#     # we have more than one elements
#
#     if left < right:
#
#         # mid is calculated to divide the array into two subarrays
#         # Floor division is must in case of python
#
#         mid = (left + right)//2
#
#         # It will calculate inversion counts in the left subarray
#
#         inv_count += get_number_of_inversions(arr, temp_arr, left, mid)
#
#         # It will calculate inversion counts in right subarray
#
#         inv_count += get_number_of_inversions(arr, temp_arr, mid + 1, right)
#
#         # It will merge two subarrays in a sorted subarray
#
#         inv_count += merge(arr, temp_arr, left, mid, right)
#     return inv_count

# This function will merge two subarrays in a single sorted subarray
def qmerge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1 # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count
n=int(input())
a = list(map(int, input().split()))
b = n * [0]
print(get_number_of_inversions(a, b,0,len(a)-1))
