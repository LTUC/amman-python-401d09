"""Things to cover...
* What is a module
* What is a script
* How to execute it from CLI
* print/input
* string concatenation
* formatted strings
* if __name__ == "__main__": snippet
"""


# import importer
from importer import b , format_my_string

print(b)

def input_output():
    """
    This function is just printing
    :return: None
    """
    multi_line_str = """no console.log for me!'
that 's the standard output"""
    # print('no console.log for me!')
    # print("that's the standard output")
    # print(multi_line_str)

    color = input("What's my fav color? ")
    # print(color)
    color_response = "Your fav color is " + color + ".Great choice"
    print(color_response)

    formatted_string = f'Your fav color is {color}.Great choice'
    print(formatted_string)

    second_color = input("What's your second fav color? ")

    # fav_colors = f"Your two fav colors are {color} and {second_color}. Great combo!!"
    # fav_colors = "Your two fav colors are {} and {}. Great combo!!".format(color, second_color)
    fav_colors = "Your two fav colors are %s and %s. Great combo!!"%(color, second_color)

    print(fav_colors)
    # print(color := input("What's my fav color? "))


# input_output()

def in_out():
    name = input('What is your name? ')
    age = input('What is your age? ')
    # formatted_string = importer.format_my_string(name, age)
    formatted_string = format_my_string(name, age)

    print(formatted_string)

# in_out()