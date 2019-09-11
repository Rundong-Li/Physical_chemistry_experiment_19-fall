<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
        MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

#### T = 25 °C
<center class="half">
<img src=figures\25_1.png height=240 width=320> 
<img src=figures\25_2.png height=240 width=320>
</center>
<center> 
# 1 的反应速率为 $3.103 \times 10^{-4}$, &nbsp; # 2 的反应速率为 $3.291 \times 10^{-4}$
</center>
<center class="half">
<img src=figures\25_3.png height=240 width=320> 
<img src=figures\25_4.png height=240 width=320>
</center>
<center> 
# 3 的反应速率为 $7.806 \times 10^{-4}$, &nbsp; # 4 的反应速率为 $7.714 \times 10^{-4}$
</center>

#### T = 35 °C
<center class="half">
<img src=figures\35_1.png height=240 width=320> 
<img src=figures\35_2.png height=240 width=320>
</center>
<center> 
# 1 的反应速率为 $1.208 \times 10^{-3}$, &nbsp; # 2 的反应速率为 $1.310 \times 10^{-3}$
</center>
<center class="half">
<img src=figures\35_3.png height=240 width=320> 
<img src=figures\35_4.png height=240 width=320>
</center>
<center> 
# 3 的反应速率为 $2.751 \times 10^{-3}$, &nbsp; # 4 的反应速率为 $2.652 \times 10^{-3}$
</center>

##### 丙酮的反应级数
由 (9-6) 可知, $p = lg\frac{v_{4}}{v_{2}}/lg\frac{0.3355}{0.1687}$
* T = 25°C 
    
    $p = lg\frac{7.714 \times 10^{-4}}{3.291 \times 10^{-4}}/lg\frac{0.3355}{0.1687} = 1.24 \approx 1$
* T = 35°C
    
    $p = lg\frac{2.652 \times 10^{-3}}{1.310 \times 10^{-3}}/lg\frac{0.3355}{0.1687} = 1.03 \approx 1$
##### 氢离子的反应级数
由 (9-7) 可知, $r = lg\frac{v_{4}}{v_{1}}/lg\frac{0.3548}{0.1862}$
* T = 25°C 
    
    $r = lg\frac{7.714 \times 10^{-4}}{3.103 \times 10^{-4}}/\frac{0.3548}{0.1862} = 1.41 \approx 1$
* T = 35°C
    
    $r = lg\frac{2.652 \times 10^{-3}}{1.208 \times 10^{-3}}/lg\frac{0.3548}{0.1862} = 1.22 \approx 1$
##### 碘的反应级数
同理可知, $q = lg\frac{v_{4}}{v_{3}}/lg\frac{27.82}{14.97}$
* T = 25°C 
    
    $q = lg\frac{7.714 \times 10^{-4}}{7.806 \times 10^{-4}}/lg\frac{27.82}{14.97} = -0.019 \approx 0$
* T = 35°C
    
    $q = lg\frac{2.652 \times 10^{-3}}{2.751 \times 10^{-3}}/lg\frac{27.82}{14.97} = -0.059 \approx 0$
##### 反应速率常数k
$v=kc^{p}(A)c^{q}(I_{2})c^{r}(H^{+})_{p=1,q=0,r=1}=kc(A)c(H^{+})$      &nbsp;  $\therefore k=v \div (c(A)c(H^{+}))$
* T = 25°C
    
    对 #1, $k=\frac{3.103 \times 10^{-4}}{\frac{9}{15}\times0.1862\times\frac{5}{15}\times0.3355}=0.0248$
    
    同理，对 #2, $k = 0.0275$, 对 #3, $k = 0.0328$, 对 #4, $k=0.0324$.
* T = 35°C
    
    对 #1, $k=\frac{1.208 \times 10^{-3}}{\frac{9}{15}\times0.1862\times\frac{5}{15}\times0.3355}=0.0967$
    
    同理，对 #2, $k = 0.109$, 对 #3, $k = 0.116$, 对 #4, $k=0.111$.
##### 反应的活化能
由Arrhenius关系式 $E_{a}=2.303R\frac{T_{1}T_{2}}{T_{2}-T_{1}}\cdot lg\frac{k_{2}}{k_{1}}$

现选取 $T=25°C$ 的 #4 和 $T = 35°C$ 的 #3 进行计算   

$T_{1}=26.57°C=299.72K, T_{2}=37.08°C=310.23K; k_{1}=0.0324, k_{2}=0.116$

$\therefore E_{a}=93835.45\ J/mol$