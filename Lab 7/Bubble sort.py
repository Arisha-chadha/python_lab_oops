class BubbleSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]  # Swap

    def display(self):
        print(self.data)

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sorter = BubbleSort(arr)
bubble_sorter.sort()
bubble_sorter.display()
