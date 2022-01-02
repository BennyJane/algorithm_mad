class Solution:
    def lastRemaining(self, n: int) -> int:
        step = 1
        interval = 2 ^ (step - 1)
        gap = 2 ^ step

        left, right = 1, n
        isAsc = True
        while (right - left) // interval > 1:
            if isAsc:
                left += interval
                right = ((right - left) // gap) * gap + left
            else:
                right -= interval
                left = right - ((right - left) // gap) * gap
            interval = 2 ^ (step - 1)
            gap = 2 ^ step

        return 0

    def lastRemaining2(self, n: int) -> int:
        arr = [i for i in range(1, n + 1)]

        def delFunc(nums, vec=True):
            temp = list()
            length = len(nums)
            if vec:
                for i in range(1, length, 2):
                    temp.append(nums[i])
            else:
                for i in range(length - 2, -1, -2):
                    temp.append(nums[i])
            return temp

        isAsc = True
        while len(arr) > 1:
            arr = delFunc(arr, isAsc)
            isAsc = not isAsc
        return arr[0]
