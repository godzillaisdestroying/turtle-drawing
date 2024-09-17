import turtle

class PolygonDrawer:
    def __init__(self):
        self.screen = turtle.Screen()  # Create a screen object
        self.t = turtle.Turtle()       # Create a turtle object
        self.screen.bgcolor("lightblue")  # Set background color

    def set_pen_color(self, color):
        self.t.pencolor(color)  # Set pen (border) color

    def set_fill_color(self, color):
        self.t.fillcolor(color)  # Set fill color

    def draw_equilateral_triangle(self, side_length):
        self.set_pen_color("red")  # Set pen color to red
        self.set_fill_color("yellow")  # Set fill color to yellow
        self.t.begin_fill()  # Start filling the shape
        for _ in range(3):
            self.t.forward(side_length)
            self.t.left(120)
        self.t.end_fill()  # End filling the shape

    def draw_rectangle(self, width, height):
        self.set_pen_color("blue")  # Set pen color to blue
        self.set_fill_color("green")  # Set fill color to green
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(width)
            self.t.left(90)
            self.t.forward(height)
            self.t.left(90)
        self.t.end_fill()

    def draw_hexagon(self, side_length):
        self.set_pen_color("purple")  # Set pen color to purple
        self.set_fill_color("orange")  # Set fill color to orange
        self.t.begin_fill()
        for _ in range(6):
            self.t.forward(side_length)
            self.t.left(60)
        self.t.end_fill()

    def move_to(self, x, y):
        self.t.penup()  # Lift the pen to stop drawing
        self.t.goto(x, y)  # Move to new position
        self.t.pendown()  # Lower the pen to start drawing

    def complete_drawing(self):
        self.t.hideturtle()  # Hide the turtle after drawing is complete
        turtle.done()  # Complete the drawing and close the window

# Example usage
if __name__ == "__main__":
    drawer = PolygonDrawer()  # Create an instance of PolygonDrawer
    
    # Draw equilateral triangle
    drawer.move_to(-100, 100)  # Move to a position to start drawing the triangle
    drawer.draw_equilateral_triangle(100)
    
    # Draw rectangle
    drawer.move_to(100, 100)  # Move to a position to start drawing the rectangle
    drawer.draw_rectangle(150, 80)
    
    # Draw hexagon
    drawer.move_to(0, -50)  # Move to a position to start drawing the hexagon
    drawer.draw_hexagon(60)
    
    drawer.complete_drawing()  # Complete the drawing
