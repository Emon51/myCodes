
# TC = O(N), SC = O(N)
def f(arr):
	n = len(arr)
	if n == 1:
		return arr[0]
	dp = [-1] * n
	dp[0]  = arr[0]
	dp[1] = max(arr[0], arr[1])
	for i in range(2, n):
		dp[i] = max(arr[i]+dp[i-2], dp[i-1]) 
	return dp[-1]
	
if __name__ == "__main__":
	arr = [2, 1, 4, 9]
	print(f(arr))
	