import turtle
import math

def drawKochSF(x1, y1, x2, y2, t):
    d = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    r = d/3.0
    h = r*math.sqrt(3)/2.0
    p3 = ((x1 + 2*x2)/3.0, (y1 + 2*y2)/3.0)
    p1 = ((2*x1 + x2)/3.0, (2*y1 + y2)/3.0)
    c = (0.5*(x1+x2), 0.5*(y1+y2))
    n = ((y1-y2)/d, (x2-x1)/d)
    p2 = (c[0]+h*n[0], c[1]+h*n[1])


def draw_triangle(x1, y1, x2, y2, x3, y3, t):
    # go to start of triangle
    t.up()
    t.setpos(x1, y1)
    t.down()
    t.setpos(x2, y2)
    t.setpos(x3, y3)
    t.setpos(x1, y1)
    t.up()

def main():
    print("Testing turtle graphics")
    t = turtle.Turtle()
    t.hideturtle()

    draw_koch = drawKochSF(-100, 0, 0, -173.2, 100)
    if d > 10:
        # flake #1
        drawKochSF(x1, y1, p1[0], p1[1], t)
        # flake #2
        drawKochSF(p1[0], p1[1], p2[0], p2[1], t)
        # flake #3
        drawKochSF(p2[0], p2[1], p3[0], p3[1], t)
        # flake #4
        drawKochSF(p3[0], p3[1], x2, y2, t)

    else:
        # draw cone
        t.up()
        1 t.setpos(p1[0], p1[1])
        t.down()
        t.setpos(p2[0], p2[1])
        t.setpos(p3[0], p3[1])
        # draw sides
        t.up()
        2 t.setpos(x1, y1)
        t.down()
        t.setpos(p1[0], p1[1])
        t.up()
        3 t.setpos(p3[0], p3[1])
        t.down()
        t.setpos(x2, y2)

    turtle.mainloop()

if __name__ == "__main__":
    main()