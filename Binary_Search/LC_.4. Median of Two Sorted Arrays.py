
#Accepted but not optimal.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #TC: O(n1 + n2); SC: O(n1 + n2)
        n1, n2 = len(nums1), len(nums2)
        n  = n1 + n2
        arr = [-1] * n
        
        i, j, k = 0, 0, 0
        
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                arr[k] = nums1[i]
                i += 1
            else:
                arr[k] = nums2[j]
                j += 1
            k += 1
            
        while i < n1:
            arr[k] = nums1[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = nums2[j]
            j += 1
            k += 1
            
        if n % 2:
            return arr[n//2]
        return (arr[n//2 -1] + arr[n//2]) / 2

#=============================================================================================#

            
            
