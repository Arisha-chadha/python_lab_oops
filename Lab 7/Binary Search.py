class BinarySearch:
    def __init__(self, data):
        self.data = data

    def search(self, target):
        low = 0
        high = len(self.data) - 1
        
        while low <= high:
            mid = (low + high) // 2 
            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                low = mid + 1 
            else:
                high = mid - 1 
        return -1

    def display(self):
        print(self.data)
arr = [1, 5, 8, 12, 16, 20, 25, 30, 35]
binary_searcher = BinarySearch(arr)
target = 16
result = binary_searcher.search(target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
