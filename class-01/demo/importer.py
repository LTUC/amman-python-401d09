def format_my_string(name:str, age:int ):
    """
    This function is used to formate a clear text
    that includes name and age of person.
    :param name:
    :param age:
    :return: string
    """
    return "I am " + name + " and I am " + str(age) + " years old"
    return f"I am {name} and I am {age} years old"

b = 25
if __name__ == "__main__":
    print(format_my_string("Ahmad", 25))
    a = 25
    print(a)