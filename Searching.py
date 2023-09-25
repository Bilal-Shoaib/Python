def binary_search(list):
    upper_bound, lower_bound = len(list)-1, 0
    mid = int((upper_bound + lower_bound)/2)
    item = input("What do you want to search? ").lower().strip()
    if item in list:
        while list[mid] != item:
            if list[mid] > item: upper_bound, mid = mid-1, int((upper_bound + lower_bound)/2)
            elif list[mid] < item: lower_bound, mid = mid+1, int((upper_bound + lower_bound)/2)
        print(f"{item.capitalize()} was found at Index {mid+1}")
    else: print("Item not in List")

def linear_search(list) :
    item = input("What do you want to search? ")
    if item in list:
        for index in range(len(list)):
            if item == list[index]: print(f"{item.capitalize()} was found at Index {index+1}")
    else: print("Item is not in List")

#Binary Search requires a sorted list
#Linear Search is relatively inefficient