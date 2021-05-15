# Imp Points
# When run the program put the array element space seperated. Example down given
# 3 6 7 4 2 7 9 1 0 3 5 6
# 1 5 6 9 7 4 2 7 9 9 2 1

# If you can't do that. Please put this line to the 11 and 12 line number

# arr1 = [3, 6, 7, 4, 2, 7, 9, 1, 0, 3, 5, 6]
# arr2 = [1, 5, 6, 9, 7, 4, 2, 7, 9, 9, 2, 1]

arr1 = list(map(int,input().split(" ")))
arr2 = list(map(int,input().split(" ")))
n = len(arr1)
m = len(arr2)

dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
for i in range(n - 1, -1, -1):
  for j in range(m - 1, -1, -1):

    if arr1[i] == arr2[j]:
      dp[j][i] = dp[j + 1][i + 1] + 1
maxm = 0

for i in range(len(dp)):
  for j in range(len(dp[i])):

    if dp[i][j]>maxm:
      maxm = dp[i][j]
      left = i
      right = j
    else:
      pass
print(arr1[right:right+maxm])
