算法：toeplitz_direct（直接暴力计算）
输入：整数n，数组a[0..2n-2]，数组v[0..n-1]
输出：数组y[0..n-1]（满足y = A × v）

pseudo code：
1. 初始化数组y[0..n-1]为0
2. for i ← 0 to n-1 do
3.     for j ← 0 to n-1 do
4.         k ← n-1 + i - j    
5.         y[i] ← y[i] + a[k] × v[j]
6.     end for
7. end for
8. return y
