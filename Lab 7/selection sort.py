class SelectionSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            # Swap the found minimum element with the first element
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

    def display(self):
        print(self.data)
arr = [64, 25, 12, 22, 11]
selection_sorter = SelectionSort(arr)
selection_sorter.sort()
selection_sorter.display() 
