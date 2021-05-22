from ascii_art import art_enjoy

class Brew:
    def __init__(self):
        self.ratio = 0
        self.water = 0
        self.ground_coffee = 0
        self.brewed_coffee = 0
        self._ratio_dict = {
          "A": 15,
          "B": 16,
          "C": 17
        }
        
    def ask(self, query):
        if query == "ratio":
            while not self.ratio:
              try:
                ratio_answer = input(f"\n \n \nWhat ratio would you like to use today? \n A. 1:15 (Stronger) \n B. 1:16 (**Recommended**) \n C. 1:17 (Weaker)\n \n \n")
              except ValueError:
                print(f"Please enter A, B or C")
                continue
              if ratio_answer.upper() not in self._ratio_dict.keys():
                print(f"Please enter A, B or C")
                continue
              else:
                break
            self.ratio = self._ratio_dict[ratio_answer.upper()]

        if query == "ground_coffee":
          while not self.ground_coffee:
            try:
              self.ground_coffee = int(input(f"\n \n \nHow much ground coffee are you using? (in grams)\n \n \n"))
            except ValueError:
              print("Please enter the amount of ground coffee (in grams) \n\n\n")
              continue
            else:
              break

    def calc(self):
        self.water = self.ground_coffee * self.ratio
        self.brewed_coffee = self.water - (self.ground_coffee * 2)

        print(f"\n \n \n YOUR RECIPE \n ----------- \n Ground Coffee: {self.ground_coffee}g \n Brewing Water: {self.water}g \n Brewed Coffee: {self.brewed_coffee}g \n Ratio: 1:{self.ratio} \n \n")
        print(art_enjoy)