class InsertionSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key

    def display(self):
        print(self.data)

arr = [12, 11, 13, 5, 6]
insertion_sorter = InsertionSort(arr)
insertion_sorter.sort()
insertion_sorter.display()
