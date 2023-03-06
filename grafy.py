import pylab as pl
from numpy import pi

f = 50
t = pl.linspace(0, 0.1, 300)

u = 3.3 * pl.cos(2*pi*f*t)
i = 1.1 * pl.cos(2*pi*f*t+pi/4)

p = u * i

pl.figure(1)
pl.plot(t, u,"g--+", label ="u(t)", color="#00ff00", )
pl.plot(t, i,"b:1", label ="i(t)", linestyle=":", linewidth=2)
pl.plot(t, p,"r", label ="p(t)", marker="p")
pl.grid(True)
pl.legend(loc="upper right")

pl.title("Vykon stridaveho proudu")
pl.xlim([0, 0.04])
pl.xlabel("t[s]")
pl.ylabel("u(t), i(t), p(t)")



pl.show()
