# Goal
Find the "best" target $t$ (scoring highest points in Darts), depending on the aim.
Definitions:
- A **target** can be $t\in[0,2\pi)\times[0,R]$, with $R$ being the radius of the board (radial coordinates).
- After targeting and throwing, a **hit** can be $h\in[0,2\pi)\times[0,\inf]\approx\mathbb{R}^2$.
- The **score** of a hit is determined with:

$$
S:\quad \mathbb{R}^2\rightarrow\mathbb{R}^+
$$

$$
h\mapsto S(h)=S_\phi(h)\cdot S_r(h)
$$

- where after converting $h=(\phi_h,r_h)$, the dependence is only $S_\phi(\phi_h)$ and $S_r(r_h)$