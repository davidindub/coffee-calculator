from greeting import greeting
from ascii_art import print_art_greeting
from Brew import Brew
version_no = 0.2


print_art_greeting(version_no)
print(f"{greeting} Welcome to the Coffee Calculator. \n ")

todays_brew = Brew()
todays_brew.ask("ratio")
todays_brew.ask("ground_coffee")


todays_brew.calc()