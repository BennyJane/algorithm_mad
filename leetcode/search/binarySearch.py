from typing import List


class Solution1:
    # 33.搜索旋转排序数组
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 先判断mid值位于哪个有序部分
            # TODO 更通用解法，此处的0 可以更换为 l
            if nums[0] <= nums[mid]:
                # 判断target是否位于左侧有序部分内部
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # 判断target是否位于右侧有序部分内部
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


# 81. 搜索旋转排序数组 II
class Solution2:
    """
    存在重复数据
    思路1： 删除数组中重复数组，只保留唯一值，然后使用# 33.搜索旋转排序数组的方法解决
    思路2：

    """

    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        l, r = 0, n - 1
        # 将左右两端存在相等值的情况，转化为不同值的情况，然后直接套用 # 33.搜索旋转排序数组 的解法
        while l <= r and nums[l] == nums[r]:
            if nums[l] == target:
                return True
            l += 1
        left = l
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # FIXME 此处必须包含等号
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

    def search2(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        n = len(nums)
        if n == 1:
            return nums[0] == target

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # 单独处理两端相等的情况
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:  # FIXME 比较对象就是l边界值
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False


# 153. 寻找旋转排序数组中的最小值
class Solution3:
    """
    题目分析：每次任意旋转随机元素个数，经历n次旋转后，结果仍然保留特征：
    可以划分为两个有序数组的连接
    后面的有序数组，全部值一定小于前面的有序数组，即 nums[r] < nums[l], 因为原数组连续递增

    思路1： 暴力循环，数据量不大

    """

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


# 154. 寻找旋转排序数组中的最小值 II
class Solution4:
    """
    这道题是 寻找旋转排序数组中的最小值 的延伸题目。
    允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
    """

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[r]:
                r -= 1
                if nums[mid] == nums[l]:
                    l += 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]

    def findMin2(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]


# 面试题 10.03. 搜索旋转数组
class Solution5:
    def search(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1
        n = len(arr)
        # 需要特殊处理起始值为target 的情况
        if n > 0 and arr[0] == target:
            return 0
        MAX_VAL = 10 ** 20
        ans = MAX_VAL
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                ans = min(ans, mid)
                r = mid - 1
            else:
                if arr[l] == arr[mid]:
                    l += 1
                elif arr[l] > arr[mid]:
                    if arr[mid] < target <= arr[n - 1]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if arr[l] <= target < arr[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1

        return ans if ans < MAX_VAL else -1

    # FIXME 只需要特别处理 数组首位相等的情况
    def search2(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l, r = 0, n - 1
        # 初始值给最大值
        ans = float("inf")
        while l <= r:
            # 如果target位于[l,r]范围内，且arr[l] == target, 直接返回l
            if arr[l] == target:
                return l
            mid = l + (r - l) // 2
            if arr[mid] == target:
                # 直接省去mid右侧左右点，即使存在target值，也不满足索引最小
                ans = min(ans, mid)
                r = mid - 1
            else:  # 需要判断mid位于那个有序部分
                if arr[l] == arr[mid]:
                    l += 1
                elif arr[l] > arr[mid]:
                    if arr[mid] < target <= arr[n - 1]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if arr[l] <= target < arr[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
        return ans if ans != float("inf") else -1

    def search3(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l, r = 0, n - 1
        while l <= r and arr[l] == arr[r]:
            if arr[l] == target:
                return l
            l += 1

        startIndex = l
        ans = float("inf")
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                ans = min(ans, mid)
                r = mid - 1
            else:
                # 需要判断mid位于那个有序部分
                if arr[startIndex] > arr[mid]:
                    if arr[mid] < target <= arr[n - 1]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if arr[startIndex] <= target < arr[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
        return ans if ans != float("inf") else -1


class Solution30:
    # 4. 寻找两个正序数组的中位数
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        ans = 0
        if n % 2 == 0:
            right = n // 2
            left = n // 2 - 1
            ans = (nums1[left] + nums1[right]) / 2
        else:
            index = n // 2
            ans = nums1[index]
        return ans

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2
