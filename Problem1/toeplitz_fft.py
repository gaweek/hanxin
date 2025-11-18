算法：toeplitz_fft（FFT优化卷积算法）
输入：整数n，数组a[0..2n-2]，数组v[0..n-1]
输出：数组y[0..n-1]（满足y = A × v）

pseudo code：
1. //1.计算FFT长度
2. m ← 2^⌈log₂(2n-1)⌉     // 最小的大于等于2n-1的2的幂
3. 
4. //2.构造扩展数组
5. 创建数组x_ext[0..m-1]，初始化为0
6. 创建数组v_ext[0..m-1]，初始化为0
7. 
8. for i ← 0 to 2n-2 do
9.     x_ext[i] ← a[2n-2-i]    // 反转a数组
10. end for
11. 
12. for i ← 0 to n-1 do
13.     v_ext[i] ← v[i]
14. end for
15. 
16. //3.计算FFT
17. X ← FFT(x_ext)     // 计算x_ext的FFT
18. V ← FFT(v_ext)     // 计算v_ext的FFT
19. 
20. //4.：频域相乘
21. 创建数组Y[0..m-1]
22. for k ← 0 to m-1 do
23.     Y[k] ← X[k] × V[k]
24. end for
25. 
26. //5.计算逆FFT
27. y_ext ← IFFT(Y)
28. 
29. //6.提取结果
30. 创建数组y[0..n-1]
31. for i ← 0 to n-1 do
32.     y[i] ← REAL_PART(y_ext[n-1+i])
33. end for
34. 
35. return y
