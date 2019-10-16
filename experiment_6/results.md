<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
        MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

#### 原始数据表

| 电极 (负极-正极) | 检零指示 (mV) | 当前示数 (V) | 电池电动势 (V) |
|:----------------:|:-------------:|:------------:|:--------------:|
|     Zn-甘汞-1    |     -5767     |    1.05767   |     1.05739    |
|     Zn-甘汞-2    |     -5749     |    1.05749   |     1.05759    |
|     甘汞-Cu-1    |     -5063     |    0.05063   |     0.05063    |
|     甘汞-Cu-2    |     -4646     |    0.04646   |     0.04646    |
|      Zn-Cu-1     |     -10764    |    1.10764   |     1.10764    |
|      Zn-Cu-2     |     -10410    |    1.1041    |     1.10411    |
|   AgCl-AgNO$_{3}$-1   |     -2764     |    0.32764   |     0.32765    |
|   AgCl-AgNO$_{3}$-2   |     -2718     |    0.32718   |     0.32699    |

-1为试验性 (tentative) 测量, 仅用于辅助-2的实验组, 下面计算都只使用-2实验组的数据.

#### 数据处理与分析
查得饱和甘汞电极在20°C时的电极电势为 $0.2471\ V^{[1]}$.

##### 1. 锌的标准电极势
根据Zn-甘汞电池的结构可知, $$\epsilon=\epsilon_{right}-\epsilon_{left}=\epsilon(甘汞)-(\epsilon^{\theta}(Zn/Zn^{2+})+\frac{RT}{nF}lna(Zn^{2+}))$$
移项得到 $$\epsilon^{\theta}(Zn/Zn^{2+})=\epsilon(甘汞)-\epsilon-\frac{RT}{nF}lna(Zn^{2+})$$
其中 $a(Zn^{2+})=\gamma(Zn^{2+})\times c(Zn^{2+}), n=2, F=96485\ C \cdot mol^{-1}, T=293.15K, R=8.314\ J \cdot mol^{-1} \cdot K^{-1}$

代入数据计算得 $\epsilon^{\theta}(Zn/Zn^{2+})=-0.75745\ V$

理论值 (20°C时) 为 $-0.76218\ V^{[1]}$, 相对误差为 0.62 %.

##### 2. 铜的标准电极势
根据Cu-甘汞电池的结构可知, $$\epsilon=\epsilon_{right}-\epsilon_{left}=\epsilon^{\theta}(Cu/Cu^{2+})+\frac{RT}{nF}lna(Cu^{2+})-\epsilon(甘汞)$$
移项得到 $$\epsilon^{\theta}(Cu/Cu^{2+})=\epsilon(甘汞)-\epsilon-\frac{RT}{nF}lna(Cu^{2+})$$
其中 $a(Cu^{2+})=\gamma(Cu^{2+})\times c(Cu^{2+}), n=2, F=96485\ C \cdot mol^{-1}, T=293.15K, R=8.314\ J \cdot mol^{-1} \cdot K^{-1}$

代入数据计算得 $\epsilon^{\theta}(Cu/Cu^{2+})=0.34579\ V$

理论值 (20°C时) 为 $0.34182\ V^{[1]}$, 相对误差为 1.16 %.

##### 3. 电池(5)的电动势

电池(5): $Zn|ZnSO_{4}(0.1\ mol \cdot dm^{-3})||CuSO_{4}(0.1\ mol \cdot dm^{-3})|Cu$

3.1 电池电动势的计算值可以通过1、2的实验值相加得到, 为 $1.10405\ V$  

3.2 电池电动势的实验值直接测得, 为 $1.10411\ V$  

3.3 电池电动势的理论值可通过锌、铜的标准电极势来计算:

根据Zn-Cu电池的结构可知 $$\epsilon=\epsilon_{right}-\epsilon_{left}=\epsilon^{\theta}(Cu/Cu^{2+})+\frac{RT}{nF}lna(Cu^{2+})-(\epsilon^{\theta}(Zn/Zn^{2+})+\frac{RT}{nF}lna(Zn^{2+}))$$

化简得到 $$\epsilon=\epsilon^{\theta}(Cu/Cu^{2+})-\epsilon^{\theta}(Zn/Zn^{2+})-\frac{RT}{nF}ln\frac{a(Cu^{2+})}{a(Zn^{2+})}$$

方程中的 $\epsilon^{\theta}$ 均为理论值 (theoretical value).

其中$\frac{a(Cu^{2+})}{a(Zn^{2+})}=\frac{\gamma(Cu^{2+})\times c(Cu^{2+})}{\gamma(Zn^{2+})\times c(Zn^{2+})}, n=2, F=96485\ C \cdot mol^{-1}, T=293.15K, R=8.314\ J \cdot mol^{-1} \cdot K^{-1}$

代入数据计算得$\epsilon_{Zn-Cu}=1.10481\ V$

计算值和实验值的相对误差为 0.0543 ‰, 计算值和理论值的相对误差为 0.0638 %.

##### 4. 微溶盐AgCl的溶度积和溶解度
根据电池结构, 有 $$\epsilon=\frac{RT}{F}ln\frac{a_{2}(Ag^{+})}{a_{1}(Ag^{+})}=\frac{RT}{F}ln\frac{\gamma_{2}c_{2}}{\gamma_{1}c_{1}}$$
令 $0.01\ mol \cdot dm^{-3}\ KCl$ 溶液中 $Ag^{+}$ 的活度为 $a(Ag^{+})$,又因为 $0.01\ mol \cdot dm^{-3}\ AgNO_{3}$ 的平均离子活度系数为 $0.902$, 上式化简为 $$\epsilon=-\frac{RT}{F}ln\frac{a(Ag^{+})}{0.092 \times 0.01}$$
由于氯化银活度积 $K_{sp}=a(Ag^{+})\cdot a(Cl^{-})$, 代入上式得$$\epsilon=\frac{RT}{F}ln(0.902\times 0.01)-\frac{RT}{F}lnK_{sp}+\frac{RT}{F}lna(Cl^{-})$$所以$$lgK_{sp}=lg(0.902\times 0.01)+lg(0.901\times 0.01)-\frac{\epsilon F}{2.303RT}$$
因为 $AgCl$ 在水中的溶解度极小, 可以认为 $\gamma(Ag^{+})=\gamma(Cl^{-})\approx1$, 因此活度积可以看成溶度积, 所以$$K_{sp}=[c(Ag^{+})/c^{\theta}]^{2}=[c(Cl^{-})/c^{\theta}]^{2}$$ 因此 $AgCl$ 在水中的的溶解度为 $\sqrt{K_{sp}}c^{\theta}$.
代入数据计算得, $K_{sp}=1.946\times 10^{-10}$, 溶解度为 $1.395\times 10^{-5}\ mol\cdot dm^{-3}$.

##### summary table
| electrodes |    $\epsilon$    |   $\epsilon^{\theta}$   |   $\epsilon_{theory}$  |    error    |          |
|:----------:|:-------:|:---------:|:-----------:|:-----------:|:--------:|
|     Zn     | 1.05759 | -0.75745 |   -0.76218  | 0.621% |          |
|     Cu     | 0.04646 |  0.34579 |   0.34182   | 1.16% |          |
| electrodes |    $\epsilon$    | $\epsilon_{compute}$ |   $\epsilon_{theory}$  |   error_1   |  error_2 |
|    Zn-Cu   | 1.10411 |  1.10405  | 1.1048 | 0.0638% | 0.0543‰ |
|            |    $\epsilon$    |    $K_{sp}$    |  solubility |             |          |
|     Ag     | 0.32699 | $1.946\times 10^{-10}$ | $1.395\times 10^{-5}$ |             |          |


#### 参考文献
$[1]$: W. M. Haynes, ed., *CRC Handbook of Chemistry and Physics, 96th Edition* (Internet Version 2016), CRC Press.