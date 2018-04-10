import turtle


# Python Programming Projects
# Author: Bryce Sulin
# Date: 4/8/18

# Problem 1: Sierpinski Triangle
def drawTriangle(turtle, points, color):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0], points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(turtle, points, degree):
    colormap = ['gray', 'white', 'white', 'white']
    drawTriangle(turtle, points, colormap[degree])
    if degree > 0:
        sierpinski(turtle, [points[0],
                            getMid(points[0], points[1]),
                            getMid(points[0], points[2])],
                   degree - 1)
        sierpinski(turtle, [points[1],
                            getMid(points[0], points[1]),
                            getMid(points[1], points[2])],
                   degree - 1)
        sierpinski(turtle, [points[2],
                            getMid(points[2], points[1]),
                            getMid(points[0], points[2])],
                   degree - 1)


# Problem 2A: Collatz
def collatz(n):
    if n % 2 == 0:
        print(n // 2)
        return n // 2

    elif n % 2 == 1:
        result = 3 * n + 1
        print(result)
        return result


# Problem 2B: Longest Collatz
sequence_length = {1: 0}


def longestCollatz(n):
    global sequence_length
    if n in sequence_length:
        return sequence_length[n]

    if n % 2 == 0:
        length = longestCollatz(n // 2)
    else:
        length = longestCollatz(3 * n + 1)
    length += 1
    sequence_length[n] = length
    return length


# Problem 3: Wisconsinite
def toWisconsinite(paragraph, dict):
    for i, j in dict.items():
        paragraph = paragraph.replace(i, j)
    paragraph = "By golly, I tell ya, " + paragraph
    return paragraph


def main():
    # Test Sierpinski Triangle (#1)
    turtles = turtle.Turtle()
    window = turtle.Screen()
    points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(turtles, points, 3)
    window.exitonclick()

    # Test Collatz (#2A)
    print("Testing Collatz:")
    n = input("Enter a number: ")
    while n != 1:
        n = collatz(int(n))

    # Test Longest Collatz (#2B)
    print("")
    print("Testing Longest Collatz:")
    result = 0
    longest = 0
    for n in range(1, 1000000):
        length = longestCollatz(n)
        if length > longest:
            result = n
            longest = length
    print("Number that produces the longest chain:", result)

    # Test Wisconsinite (#3)
    print("")
    print("Testing Wisconsinite:")

    paragraph = 'I was at a stoplight on my way to Piggly Wiggly to buy some sweet rolls, when another driver ' \
                'cut me off, almost causing an accident. Hello, let\'s drink some soda, or have a drink from the water fountain. ' \
                'The upper peninsula of Michigan has terrible mosquitos.'

    # Dictionary with our key:values
    dictionary = {'soda': 'pop', 'water fountain': 'bubbler', 'stoplight': 'stop \'n go light',
                  'Piggly Wiggly': 'da Pig',
                  'Hello': 'Hey', 'yes': 'you betcha', 'sweet rolls': 'bakery', 'card game': 'Sheepshead',
                  'lend me': 'borrow me',
                  'thaw': 'unthaw', 'have': 'got', 'G*d d#m': 'guldarn', 'galoshes': 'rubbers', 'factory': 'da mill',
                  'okay': 'fair to midlin', 'gee whiz': 'geez', 'almost': 'pert-neer', 'mosquitos': 'skeeters',
                  'The upper peninsula of Michigan': 'Da U.P.'}
    print(toWisconsinite(paragraph, dictionary))


main()
