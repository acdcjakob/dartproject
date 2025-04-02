# Goal
Find the "best" target $t$ (scoring highest points in Darts), depending on the aim.
Definitions:
- A **target** can be $t\in[0,2\pi)\times[0,r_\mathrm{max}]$, with $r_\mathrm{max}$ being the radius of the board (radial coordinates).
- After targeting and throwing, a **hit** can be $h\in[0,2\pi)\times[0,\inf]\approx\mathbb{R}^2$.
- The **score** of a hit is determined with:

$$
S:\quad \mathbb{R}^2\rightarrow\mathbb{R}^+
$$

$$
h\mapsto S(h)=S_\phi(h)\cdot S_r(h)
$$

- where after converting $h=(\phi_h,r_h)$, the dependence is only $S_\phi(\phi_h)$ and $S_r(r_h)$

# Statistics
If one had perfect aim, then one would always hit the targeted position: $t=h$.
Therefore, to find the target with the best *expected* score, it's the same as finding the hit with the best score: $S(h_{opt})=\max_hS$.
This is trivial: it's triple 20, aka *180*.

**But**: most people do not have perfekt aim 🙂.
There are two ways of sucking in darts:
1. bad **accuracy**
    - accuracy is defined as the "offset" of the targeted position
    - example: If you always hit 2cm below your targeted position, then you should (obviously) target 2cm above the triple 20 position.
2. bad **precision**
    - precision is defined as the reproducibility of your results
    - example: Even when hitting triple 20 "on average", a "spread" observed, when trying to hit the same position. There is always some distribution, and developing consistency is the key.

 Considering a fixed target, and different hits (=throwing multiple times), this study will assume the following:
 - perfect accuracy: the **mean** of hits equals the target position (no offset)
 - defined precision: the distributions along $x$- and $y$-coordinates are (i) *independent* and (ii) follow a Gaussian distribution with variance $\sigma$:
    - $W(h_x) = \mathrm{gauss}(h_x,t_x,\sigma_x)$
    - $W(h_y) = \mathrm{gauss}(h_y,t_y,\sigma_y)$

$$
\mathrm{gauss}(h_i,t_i,\sigma_i)=\frac{1}{\sigma_i\sqrt{2\pi}}\exp\left({-\frac{(h_i-t_i)^2}{\sigma_i^2}}\right)
$$

It is clear that

$$
\int\int
\mathrm{gauss}(h_x,t_x,\sigma_x)
\mathrm{gauss}(h_y,t_y,\sigma_y)
\mathrm{d}h_x \mathrm{d}h_y
= 1
$$

To get the "average score", one can now weight this distribution with the score-function $S$:

$$
S_\mathrm{avg}(t_x,t_y,\sigma_x,\sigma_y)
= \int\int
\mathrm{gauss}(h_x,t_x,\sigma_x)
\mathrm{gauss}(h_y,t_y,\sigma_y)
S(h_x,h_y)
\mathrm{d}h_x \mathrm{d}h_y
$$

Because we assumed independence: $\sigma_x=\sigma_y$, and with $t=(t_x,t_y)$ we see that $S_\mathrm{avg}=S_{avg}(t,\sigma)$.
With this quanitity, we can achieve our goal: **find the set of targets with highest average score depending on the badness of aiming**:

$$
t_\mathrm{best}(\sigma)
\in \{
    t\in[0,2\pi)\times[0,r_\mathrm{max}]=T
    \ |\ 
    S_\mathrm{avg}(t)=\max S(T,\sigma)
\}
$$