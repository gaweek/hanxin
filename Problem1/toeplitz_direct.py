算法思路步骤：
    // 输入：n - 矩阵维度
    //       a - 压缩数组（长度2n-1）
    //       v - 输入向量（长度n）
    // 输出：y - 矩阵向量乘积（长度n）
算法实现：
function DirectMatrixMultiply(n, a, v):
    y = new array of size n initialized to 0
    for i from 0 to n-1:
        for j from 0 to n-1:
            k = n-1 + i - j  // 计算对角线索引
            y[i] = y[i] + a[k] * v[j]
    
    return y
