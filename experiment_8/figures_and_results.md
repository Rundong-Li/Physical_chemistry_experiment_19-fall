<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
        MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

data for $c_{HCl}=2mol/L$
| $t (s)$ | 149  | 215   | 262  | 364   | 439  | 537  | 627  | 720  | 820  | 940  | 1082 | 1201 | 1312 | 1471  | 1591 | 1715 | 1892 | 2046 | 2168 |
|--------------|------|-------|------|-------|------|------|------|------|------|------|------|------|------|-------|------|------|------|------|------|
| $\alpha_{t}$ | 10.9 | 10.15 | 10.1 | 10.05 | 9.65 | 8.5  | 9.3  | 9.2  | 8.05 | 7.15 | 7.6  | 7    | 6.8  | 6.5   | 5.8  | 5.65 | 5.15 | 5.15 | 5.1  |
| $t (s)$      | 2280 | 2497  | 2674 | 2910  | 3154 | 3376 | 3550 | 3620 | 3747 | 3976 | 4213 | 4747 | 5262 | 5405  | 5633 |      |      |      |      |
| $\alpha_{t}$ | 4.65 | 4.05  | 3.6  | 2.9   | 2.4  | 2.45 | 2.05 | 1.8  | 1.4  | 1.45 | 1.35 | 0.3  | 0    | -0.45 | -0.5 |      |      |      |      |

<center>
<img src=figures\alpha-t-2mol.png width=600 height=480>
</center>

data for $c_{HCl}=4mol/L$
| $t (s)$      | 145  | 194  | 233  | 308  | 360 | 445 | 481  | 580 | 669 | 766 | 850 | 999 | 1134 | 1253 | 1353 | 1493 | 1574  | 1675  |
|--------------|------|------|------|------|-----|-----|------|-----|-----|-----|-----|-----|------|------|------|------|-------|-------|
| $\alpha_{t}$ | 10.1 | 8.85 | 8.45 | 7.45 | 7.2 | 6.7 | 6.55 | 5.5 | 4.1 | 3.4 | 3   | 2.9 | 1.7  | 1.1  | 0.7  | 0.25 | -0.45 | -0.75 |

<center>
<img src=figures\alpha-t-4mol.png width=600 height=480>
</center>

<div STYLE="page-break-after: always;"></div>

通过 $\alpha_{t}$ 和 $\alpha_{\infty}$ 可以计算出各个时刻的 $ln(\alpha_{t}-\alpha_{\infty})$，做出 $ln(\alpha_{t}-\alpha_{\infty})-t$  图如下：

<center>
<img src=figures\ln-t-2mol.png width=500 height=400>
</center>
<center>
<img src=figures\ln-t-4mol.png width=500 height=400>
</center>

再根据 $t_{1/2}=\frac{0.693}{k}$ 可计算得，当盐酸浓度为 $2mol/L$ 时，$t_{1/2}=2538.46s$，当盐酸浓度为 $4mol/L$ 时，$t_{1/2}=703.84s$.

设氢离子反应级数为 $h$，则 $h=ln\frac{k_{c=4mol/L}}{k_{c=2mol/L}}÷ln2=1.85$

查阅相关文献可知，$H^{+}$ 在该反应中的反应级数为 $1$，我得到的 $1.85$ 与实际值有较大的误差，分析原因如下：

* 第一组（$HCl$ 浓度 $2mol/L$）实验中，旋光仪镜头的焦距没有调至使视野最清晰，不能很好地读出 $t$ 时刻的旋光度 $\alpha_{t}$，反应开始阶段有很多跳点，旋光度 $\alpha_{t}$ 忽升忽降，导致拟合曲线时斜率（的绝对值）偏小，继而所求反应级数偏大

* 第二组（$HCl$ 浓度 $4mol/L$）实验前，旋光仪镜头的焦距已调整至最佳位置，可基本排除读数不准确的情况. 但因为操作不够熟练，读数记录速度较慢，反应初始阶段记录数据的时间间隔较长，导致数据量不足，可能影响了后续的拟合，使拟合曲线时斜率（的绝对值）偏大，继而所求反应级数偏大