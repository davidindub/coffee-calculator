from datetime import datetime

now = datetime.now()

current_hour = now.strftime("%H")
current_time = now.strftime("%H:%M:%S")

def pick_greeting(hour):
    if hour < 6:
        return "Wow, you're up late!"
    elif hour < 12:
        return "Good morning!"
    elif hour < 17:
        return "Good afternoon."
    else:
        return "Good evening."

greeting = pick_greeting(int(current_hour))

art_greeting = """

    __   ___   _____  _____  ___    ___                               
   /  ] /   \ |     ||     |/  _]  /  _]                              
  /  / |     ||   __||   __/  [_  /  [_                               
 /  /  |  O  ||  |_  |  |_|    _]|    _]                              
/   \_ |     ||   _] |   _]   [_ |   [_                               
\     ||     ||  |   |  | |     ||     |                              
 \____| \___/ |__|   |__| |_____||_____|                              
                                                                      
    __   ____  _        __  __ __  _       ____  ______   ___   ____  
   /  ] /    || |      /  ]|  |  || |     /    ||      | /   \ |    \ 
  /  / |  o  || |     /  / |  |  || |    |  o  ||      ||     ||  D  )
 /  /  |     || |___ /  /  |  |  || |___ |     ||_|  |_||  O  ||    / 
/   \_ |  _  ||     /   \_ |  :  ||     ||  _  |  |  |  |     ||    \ 
\     ||  |  ||     \     ||     ||     ||  |  |  |  |  |     ||  . \\
 \____||__|__||_____|\____| \__,_||_____||__|__|  |__|   \___/ |__|\_|

                                                            Version 0.1                                                                      

"""

art_enjoy = """
    ( (
    ) )
  ........
  |      |]
  \      /    Enjoy!
   `----'

        """

# print("Current hour =", current_hour)

class Brew:
    def __init__(self):
        self.ratio = 0
        self.water = 0
        self.ground_coffee = 0
        self.brewed_coffee = 0
    
    def ask(self, query):
        if query == "ratio":
            ratio_answer = input(f"\n \n \nWhat ratio would you like to use today? \n A. 1:15 (Stronger) \n B. 1:16 (**Recommended**) \n C. 1:17 (Weaker)\n \n \n")
            ratio_answer = ratio_answer.upper()
            if ratio_answer == "A":
                self.ratio = 15
            elif ratio_answer == "B":
                self.ratio = 16
            else:
                self.ratio = 17
        if query == "ground_coffee":
            self.ground_coffee = input(f"\n \n \nHow much ground coffee are you using? (in grams)\n \n \n")
            self.ground_coffee = int(self.ground_coffee)

    def calc(self):
        self.water = self.ground_coffee * self.ratio
        self.brewed_coffee = self.water - (self.ground_coffee * 2)
        # print(f"Use {self.water}g water to brew. You will have xx amount of brewed coffee")
        print(f"\n \n \n YOUR RECIPE \n ----------- \n Ground Coffee: {self.ground_coffee}g \n Brewing Water: {self.water}g \n Brewed Coffee: {self.brewed_coffee}g \n Ratio: 1:{self.ratio} \n \n")
        print(art_enjoy)

print(art_greeting)

print(f"{greeting} Welcome to the Coffee Calculator. \n ")

todays_brew = Brew()

todays_brew.ask("ratio")
todays_brew.ask("ground_coffee")


todays_brew.calc()