def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    
    # Define helper function for binary search
    def binary_search_peak(nums, left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        # Check if mid is a peak
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return nums[mid]
        # Move towards the side with the higher value
        elif nums[mid] < nums[mid + 1]:
            return binary_search_peak(nums, mid + 1, right)
        else:
            return binary_search_peak(nums, left, mid - 1)
    
    # Call binary search helper function
    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)

