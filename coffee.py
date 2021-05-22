from greeting import greeting
from ascii_art import art_greeting
from Brew import Brew

print(art_greeting)
print(f"{greeting} Welcome to the Coffee Calculator. \n ")

todays_brew = Brew()
todays_brew.ask("ratio")
todays_brew.ask("ground_coffee")


todays_brew.calc()