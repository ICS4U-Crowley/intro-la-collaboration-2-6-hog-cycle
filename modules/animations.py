from turtle import *


def animate():
    print("Action d'animation")
    try:
        t = Turtle()
        t.speed(5)
        for _ in range(4):
            t.forward(100)
            t.left(90)
        mainloop()
    except Terminator as e:
        print("...la fenêtre a été fermée")

# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":
    animate()
