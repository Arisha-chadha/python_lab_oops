class MergeSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        self.data = self.merge_sort(self.data)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def display(self):
        print(self.data)

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sorter = MergeSort(arr)
merge_sorter.sort()
merge_sorter.display()
