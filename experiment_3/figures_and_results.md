<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
        MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

<font size = 4>根据系列标准溶液的乙醇的质量分数及其折射率得到的标准点如下图中蓝色圆点所示.
<div align=center><img src = 'figures/standard_and_interpolate.png ' height=600 width=750></div>

上图中红色和绿色小三角分别表示通过内插法计算得到的气相和液相的成分(以乙醇的质量分数表示)及其折射率(实验值).
&nbsp;

内插法基于的基本公式：$$\frac{RI_{1}-RI_{2}}{x_{1}-x_{2}}=\frac{RI_{1}-RI}{x_{1}-x}$$
这里 $RI$ 是待求成分物质的折射率 (refractive index)，$RI_{1} 和 RI_{2}$ 和  $RI$ 最邻近的(标准溶液的)两个折射率，$x_{1}, x_{2}$ 是它们的成分 (乙醇的质量分数), $x$ 是待求物质的成分 (乙醇的质量分数).

<div STYLE="page-break-after: always;"></div>

实现内插法求解成分 $x$ 的代码如下：</font>
```python
def Interpolate_Calculation(x):
    '''
    argument: x: a specific value of refractive index (float)
    return: composition of the gas/liquid phase
    '''
    for i in range(7):
        if x < standard_RI_list[i] and x > standard_RI_list[i+1]:
            break
    index = i
    """
    use interpolate method to calculate composition:
    (RI[index]-x)/(w[index]-w) = (x-RI[index+1])/(w-w[index+1])
    here w is the target value (the composition)
    """
    slope = (standard_RI_list[index]-standard_RI_list[index+1])
            /(standard_w_list[index]-standard_w_list[index+1])
    w = standard_w_list[index]-(standard_RI_list[index]-x)/slope
    return w
```
<font size = 4>完整数据列表如下：</font>
|      沸点 (°C)     |  79.9  |   76.4  |  73.8  |   68.5  |  66.3  |  65.7  |  66.2  |  67.5  |  69.1  |   72   |   74   |  75.5  |  77.5  |  78.2  |
|:------------------:|:------:|:-------:|:------:|:-------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
|     气相折射率     |    \   |  1.4185 | 1.4125 |  1.4032 | 1.4012 | 1.3981 | 1.3971 |  1.395 | 1.3901 | 1.3829 | 1.3755 | 1.3719 | 1.3642 |    \   |
| 气相中乙醇质量分数 |    0   |  0.0782 | 0.1633 |  0.2785 | 0.3059 | 0.3578 | 0.3734 | 0.4063 | 0.4828 | 0.5953 | 0.7109 | 0.7672 | 0.8875 |    1   |
|     液相折射率     | 1.4238 |  1.4235 |  1.422 |  1.417  |  1.413 | 1.3869 | 1.3805 |  1.376 | 1.3729 |  1.367 | 1.3632 | 1.3623 | 1.3611 | 1.3590 |
| 液相中乙醇质量分数 |    0   | 0.00443 | 0.0266 | 0.10037 | 0.1571 | 0.5328 | 0.6328 | 0.7031 | 0.7516 | 0.8438 | 0.9031 | 0.9172 | 0.9359 |    1   |

<div STYLE="page-break-after: always;"></div>
<font size = 4>做出 $T_{b}-x$ 图如下：</font>
<div align=center><img src = 'figures/Tb-x.png ' height=600 width=750></div>

<font size = 4>从图中可以看出最低恒沸点为 $65.7°C$, 恒沸混合物中乙醇的质量分数约为 $0.38$.</font>