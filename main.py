import tkinter as tk
import numpy as np

# CLASSES
class Vector:
    vec: tuple[float]
    def __init__(self, *vec: float):
        self.vec = vec
    
    def asTuple(self):
        return self.vec
    
    def asList(self):
        ret = []

        for v in self.vec:
            ret.append(v)
        return ret

    def __str__(self):
        ret = ""
        i = 1

        for v in self.vec:
            ret += str(v)
            if i < len(self.vec):
                i += 1
                ret += ", "

        return "{" + ret + "}"
    

class Vector2(Vector):
    def __init__(self, x: float, y: float):
        self.vec = (x, y)
    
    def __add__(self, other):
        return Vector2.new(self.vec[0] + other.vec[0], self.vec[1] + other.vec[1])


class Object:
    def __init__(self, mass: float, size: Vector2, position: Vector2, velocity: Vector2 = Vector2(0, 0)):
        self.mass = mass
        self.size = size
        self.position = position
        self.velocity = velocity

    def isCollidedWithScreenBorder(self):
        direction       = -1
        (posX, posY)    = self.position.asTuple()
        (width, height) = self.size.asTuple()
        (vx, vy)        = self.velocity.asTuple()
        if posX <= 0 or posX >= window_width:
            self.velocity = Vector2(vx * -1, vy)
        if posY <= 0 or posY >= window_height:
            self.velocity = Vector2(vx, vy * -1)


class Engine:
    objects: list[Object] = []
    def __init__(self, gravity: float, canvas: tk.Canvas):
        self.gravity = gravity
        self.canvas = canvas

    def update_objects(self):
        for object in iter(self.objects):
            if object.isCollidedWithScreenBorder():  # Is colliding with window?
                return
            (posX, posY) = object.position.asTuple() # Deconstruct position from tuple
            (width, height) = object.size.asTuple()  # Deconstruct size from tuple
            self.canvas.create_rectangle(
                posX, posY,                  # Position
                posX + width, posY + height, # Calculate positions for width and height
                fill="white")
    
    def create_object(self, mass: float, size: Vector2, position: Vector2, velocity: Vector2):
        object: Object = Object(mass, size, position, velocity)
        self.objects.append(object)
        return object




#MAIN
window = tk.Tk()
window_width = 400
window_height = 400
window.geometry(f"{window_width}x{window_height}")
window.configure(bg="black")
window.title("Engine Simulation")

canvas = tk.Canvas(window, background="black", highlightthickness=0, border=0)

Engine1 = Engine(gravity = 9.8, canvas = canvas)
Engine1.create_object(mass=10, 
                      size=Vector2(5, 5), 
                      position=Vector2(100, 100), 
                      velocity = Vector2(1, 2))
Engine1.update_objects()


canvas.pack()

window.mainloop()