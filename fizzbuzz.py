# Fizz Buzz Game
#
# "FizzBuzz" ist ein Gruppen-Wortspiel für Kinder, das ihnen etwas über
# die mathematische Division beibringen soll. Die Spieler zählen abwechselnd inkremental,
# wobei jede durch drei teilbare Zahl durch das Wort
# „Fizz“ und jede durch fünf teilbare Zahl durch das Wort „Buzz“ ersetzt wird. 

# Constants
HELP_TEXT_MISS = "Your input was wrong."
HELP_TEXT_WIN = "Your input was correct."
HELP_TEXT_INTRO_1 = """
------------------------------------------------------------------
Hi and welcome to the Fizz Buzz Game
This game teaches you the basics of division in mathematics.
I will count up numbers starting with one and if
the number can be divided by 3 you enter Fizz.
If the number can be divided by 5 you enter Buzz.
And if the number can be divided both by 3 and 5 you enter FizzBuzz.
When the nunber can both not be divied by 3 and 5 you just enter "Enter".
If your input is not correct the game ends and you will be presented
a statistics of how many times your input was correct during the whole game
"""
HELP_TEXT_INTRO_2 = """
Let'S play!
---------------
"""


#Variablen
hit_counter: int = 0
continue_playing = True


# Fuctions
def display_welcome_message():
    print(HELP_TEXT_INTRO_1)
    print(HELP_TEXT_INTRO_2)

def get_input(text):
    return input(text)



# ################################################
# # # Main
# ################################################


if __name__ == '__main__':
    display_welcome_message()
    number_output = 1
    expected_input = ""
    input_variable: str
    actual_case: int
    case_guess: int
    hit_count = 0

    while True:
        print(number_output)

        # calculate input expectation

        if number_output%3 == 0 and number_output%5 == 0:
            # expected_input = "FizzBuzz"
            actual_case = 1
        elif number_output%3 == 0:
            # expected_input = "Fizz"
            actual_case = 2
        elif number_output%5 == 0:
            # expected_input = "Buzz"
            actual_case = 3
        elif number_output%3 != 0 and number_output%5 != 0:
            # expected_input = ""
            actual_case = 4



        input_variable = get_input("Please respond according to the rules of the game: ")

        # commment
      
        if input_variable == "FizzBuzz":
            # expected_input = "FizzBuzz"
            case_guess = 1
        elif input_variable == "Fizz":
            # expected_input = "Fizz"
            case_guess = 2
        elif input_variable == "Buzz":
            # expected_input = "Buzz"
            case_guess = 3
        elif input_variable == '':
            # expected_input = ""
            case_guess = 4
        else:
            print("This was not a valid input. Please enter a valid input.")
            continue


        if (actual_case == case_guess):
            number_output += 1
            hit_count +=1
            print("Correct!")
            continue
        else:
            break

    print("===================================================")
    print(f"Die Anzahl deiner richtigen Eingaben ist {hit_count}. Deine letzte Eingabe war leider falsch, weswegen  das Spiel beendet wurde.")