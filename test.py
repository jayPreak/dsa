def min_houses(nums, x): 
    n = len(nums) 
    curr_sum = 0 
    min_len = n + 1 
    start = 0 
    end = 0 

    while (end < n): 

        # Keep adding array elements while current sum is smaller than x 
        while (curr_sum <= x and end < n): 
            curr_sum += nums[end] 
            end += 1

        # If current sum becomes greater than x. 
        while (curr_sum > x and start < n):

            # Update minimum length if needed
            if (end - start < min_len):
                min_len = end - start

            # remove starting elements
            curr_sum -= nums[start]
            start += 1

    # Check if last window has minimum length required.
    if (min_len > n):
        return 0;

    return min_len;

     # Driver code to test above function.
nums = [1, 2, 3, 4, 5] 
x = 10;
print(min_houses(nums, x))