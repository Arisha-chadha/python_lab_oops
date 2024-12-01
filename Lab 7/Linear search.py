class LinearSearch:
    def __init__(self, data):
        self.data = data

    def search(self, target):
        for index, value in enumerate(self.data):
            if value == target:
                return index 
        return -1 

    def display(self):
        print(self.data)

arr = [10, 23, 45, 70, 11, 90, 56]
linear_searcher = LinearSearch(arr)
target = 70
result = linear_searcher.search(target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
