def minDifference(arr, n):
	sum = 0;
	for i in range(n):
		sum += arr[i]
	y = sum // 2 + 1
	dp = [False for i in range(y)]
	dd = [False for i in range(y)]
	dd[0] = True
	for i in range(n):
		for j in range(y):
			if (j + arr[i] < y and dp[j]):
				dd[j + arr[i]] = True
		for j in range(y):
			if (dd[j]):
				dp[j] = True
			dd[j] = False
	for i in range(y-1, 0, -1):
		if (dp[i]):
			return (sum - 2 * i)
	return 0;
if __name__ == '__main__':
	arr = list(map(int, input().split()))
	n = len(arr)
	print("The Minimum difference of 2 sets is ", minDifference(arr, n))
