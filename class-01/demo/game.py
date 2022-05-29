"""
Let's create the classic guessing game I Spy. We'll need...
- A list of things to guess
  - Each thing should be a dictionary with name and hints attributes
  - name is a string
  - hints is a list of strings
"""

things = [
    {
        'name': 'clock',
        'hints':[
            'Changes frequently',
            'Day and night',
            'Different shapes and different sizes'
        ]
    },

    {
        'name': 'chair',
        'hints': [
            'Has multi legs',
            'Hsd s restful interface',
            'not used in the stand up meetings'
        ]
    }
]

def guess_a_thing(riddle_index):

    thing = things[riddle_index]
    correct_answer = thing['name']
    hints = thing['hints']
    guess = input("I spy with my little eye... ")
    while len(hints):
        if guess == correct_answer:
            print("Crushed it")
            break
        hint = hints.pop(0)
        print(f"Nope, but here's a hint - {hint}")
        guess = input("I spy with my little eye... ")
    if guess == correct_answer:
        print("Crushed it")
    else:
        print(f"Too bad. It's a {correct_answer}")


if __name__ == "__main__":
    riddle_index = 0

    response = input("Wanna play? ")
    while response != 'n':
        guess_a_thing(riddle_index)
        riddle_index += 1
        if riddle_index > len(things) - 1:
            break