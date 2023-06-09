from plotter import Plotter
from math import pi
from plot_text import draw_text

plotter = Plotter(185, 185, 0, 50, 5, 7)

def connection_dot():
    global plotter
    from math import sqrt
    d = 0.05
    f = 0.075
    with plotter.with_pen():
        plotter.up()
        plotter.move(-f, 0.025)
        plotter.down();
        plotter.move(d, d)
        plotter.move(d, 0)
        plotter.move(d, -d)
        plotter.move(0, -d)
        plotter.move(-d, -d)
        plotter.move(-d, 0)
        plotter.move(-d, d)
        plotter.move(0, d)
        plotter.up()
        plotter.move(f, -0.025)

def diode():
    global plotter
    from math import sqrt
    d = sqrt(2)
    with plotter.with_pen():
        plotter.up()
        plotter.move(-d/2, 0)
        plotter.down()
        plotter.move(d, 0)
        plotter.move(-d/2, d)
        plotter.move(-d/2, -d)
        plotter.up()
        plotter.move(0, d)
        plotter.down()
        plotter.move(d, 0)
        plotter.up()
        plotter.move(-d/2, 0)
        

plotter.goto(70, 100)

with plotter.with_local_zero(s=5):
    plotter.goto(0, -10)
    plotter.down()
    plotter.move(-2, 2)
    with plotter.with_local_zero(a=pi/4):
        diode()
    plotter.move(-3, 3)
    plotter.move(2, 2)
    with plotter.with_local_zero(a=-pi/4):
        diode()
    plotter.move(3, 3)
    plotter.move(2, -2)
    with plotter.with_local_zero(a=-pi/4*3):
        diode()
    plotter.move(3, -3)
    plotter.move(-2, -2)
    with plotter.with_local_zero(a=pi/4*3):
        diode()
    plotter.move(-3, -3)
    connection_dot()
    plotter.move(0, -1)
    plotter.move(-8.5, 0)
    plotter.move(0, 5)
    plotter.up()
    plotter.move(-1, 0.75)
    plotter.down()
    plotter.move(0.5, 0.5)
    plotter.move(0.2, 0)
    plotter.move(0.6, -0.5)
    plotter.move(0.2, 0)
    plotter.move(0.5, 0.5)
    plotter.up()
    plotter.move(-1, 0.75)
    plotter.down()
    plotter.move(0, 5)
    plotter.move(8.5, 0)
    plotter.move(0, -1)
    connection_dot()
    plotter.up()
    plotter.move(-5, -5)
    plotter.down()
    connection_dot()
    plotter.up()
    plotter.move(-1, 0)
    draw_text(plotter, '-')
    plotter.move(0.2, 0)
    plotter.down()
    plotter.move(-1, 0)
    plotter.move(0, -8)
    plotter.move(20, 0)
    plotter.up()
    plotter.move(0.3, 0)
    with plotter.with_local_zero(s=4):
        connection_dot()
    plotter.move(1, -0.5)
    draw_text(plotter, '0V')
    plotter.move(-2, 8)
    draw_text(plotter, '+V')
    plotter.move(-2.3, 0.5)
    with plotter.with_local_zero(s=4):
        connection_dot()
    plotter.move(-0.3, 0)
    plotter.down()
    plotter.move(-8.9, 0)
    connection_dot()
    plotter.up()
    plotter.move(0.25, 0)
    draw_text(plotter, '+')
    plotter.move(3.25, 0)
    plotter.down()
    connection_dot()
    plotter.move(0, -3.5)
    plotter.move(0.8, 0)
    plotter.move(0, -0.3)
    plotter.move(-1.6, 0)
    plotter.move(0, 0.3)
    plotter.move(0.8, 0)
    plotter.up()
    plotter.move(0, -1)
    plotter.down()
    plotter.move(0.8, 0)
    plotter.move(0, 0.3)
    plotter.move(-1.6, 0)
    plotter.move(0, -0.3)
    plotter.move(0.8, 0)
    plotter.move(0, -3.5)
    connection_dot()
    plotter.up()
    plotter.move(-7, 13)
    draw_text(plotter, 'BRIDGE RECTIFIER')
    plotter.move(-13, -11)
    with plotter.with_local_zero(s=0.75):
        draw_text(plotter, 'SMOOTHING')
        plotter.move(-0.8*9, -1.5)
        draw_text(plotter, 'CAPACITOR')
    plotter.goto(-11, 3)
    plotter.down()
    plotter.move(30, 0)
    plotter.move(0, -18)
    plotter.move(-30, 0)
    plotter.move(0, 18)
    plotter.up()
    plotter.move(-0.2, 0.2)
    plotter.down()
    plotter.move(30.4, 0)
    plotter.move(0, -18.4)
    plotter.move(-30.4, 0)
    plotter.move(0, 18.4)