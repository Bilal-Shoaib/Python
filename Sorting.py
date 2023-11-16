def bubble_sort(array):
    for _ in range(len(array)):
        for index in range(len(array)-1):
            if array[index] > array[index+1]: #For descending '<'
                temporary = array[index]
                array[index] = array[index+1]
                array[index+1] = temporary
    return array

def insertion_sort(array):
    for count in range(1, len(array)):
        current_value, index = array[count], count
        while index > 0 and array[index-1] > current_value:
            array[index] = array[index-1]
            index -= 1
        array[index] = current_value
    return array

def patience_sort(list):
    piles = []
    for item in list:
        new_pile = [item]
        for pile in piles:
            if item < pile[-1]:
                pile.append(item)
                break
        else: piles.append(new_pile)
    sorted_list = []
    while piles:
        smallest_pile = min(piles, key=lambda pile: pile[-1])
        sorted_list.append(smallest_pile.pop())
        if not smallest_pile: piles.remove(smallest_pile)
    return sorted_list


#Insertion Sort is far more efficient than Bubble Sort
#This Insertion Sort Algo loops about 26 times for an Array of length 10
#This Bubble Sort Algo loops about 90 times for an Array of length 10
#array = ["Ali", "Bilal", "Murtaza", "Rayan", "Babar", "Yasir", "Talal", "Huzaifa", "Soomro", "Azhar"]
