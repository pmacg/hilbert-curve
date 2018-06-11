import turtle

#------------------------------------------------------------------------------
# The ration of the gap to the original size, is given by the following
# recurrence relation: x(i) = 2 * x(i-1) + 1
#------------------------------------------------------------------------------
def calculateGapDenom(order: int):
  if order == 0:
    return 1
  else:
    return 2 * calculateGapDenom(order - 1) + 1

#------------------------------------------------------------------------------
# Draw a hilbert curve of the given order in a square of the given size.
# Assumes the turtle is at the bottom left of the square, facing upwards.
#
# If flip is true, draws anticlockwise.
#
# Ends with the turtle pointing downwards.
#
# Order 0 is the basic shape:
#   |-|
#   | |
#------------------------------------------------------------------------------
def drawHilbert(order: int, size: int, flip=False, gap=None):
  # The 'flip' parameter is entirelly encoded in the turnAngle - if flip is
  # true, every turn is reversed and this results in the desired
  # mirror-image
  turnAngle = -90 if flip else 90

  # This gap is the distance between each order-1 curve
  # It is basically the length of each line in the hilbert curve
  if gap is None:
    denom = calculateGapDenom(order)
    gap = size/denom

  if order == 0:
    # Draw the basic three-line curve
    turtle.forward(size)
    turtle.right(turnAngle)
    turtle.forward(size)
    turtle.right(turnAngle)
    turtle.forward(size)

  else:
    # Calculate the size of each sub curve
    subSize = (size - gap) / 2

    # Draw an anticlockwise subcurve, facing to the right.
    # (anticlockwise actually means the opposite direction to this curve)
    turtle.right(turnAngle)
    drawHilbert(order - 1, subSize, not flip, gap)

    # Draw a line upwards
    turtle.right(turnAngle)
    turtle.forward(gap)

    # Draw a normal subcurve, facing upwards
    drawHilbert(order - 1, subSize, flip, gap)

    # Draw a joining line to the right
    turtle.left(turnAngle)
    turtle.forward(gap)

    # Draw a normal subcurve, facing upwards
    turtle.left(turnAngle)
    drawHilbert(order - 1, subSize, flip, gap)

    # Draw a joining line downwards
    turtle.forward(gap)

    # Draw an anticlockwise subcurve, facing to the left
    # (anticlockwise actually means the opposite direction to this curve)
    turtle.right(turnAngle)
    drawHilbert(order - 1, subSize, not flip, gap)
    turtle.right(turnAngle)

if __name__ == "__main__":
  # Prepare to ddraw
  turtle.hideturtle()
  turtle.penup()
  turtle.speed(0)
  turtle.setposition(-350, -350)
  turtle.left(90)
  turtle.pendown()

  # Draw an order-6 curve. Anything bigger just takes too long.
  drawHilbert(6, 700)

  # Don't exit immediately - you need to admire your work!
  turtle.exitonclick()