# Author: Jiarou Deng dpj5243@psu.edu
# Collaborator:Max Simpson mes6581@psu.edu
# Collaborator: Alessandro Prieto Bustamante asp5586@psu.edu
# Collaborator: Gabriel Charpentier gbc5202@psu.edu
# Section: 10
# Breakout: 10

def grade(g):
 if g >= 93.0:
  l= "A"
 elif g >= 90.0:
  l="A-"
 elif g >= 87.0:
  l="B+"
 elif g >= 83.0:
  l="B"
 elif g >= 80.0:
  l="B-"
 elif g >= 77.0:
  l="C+"
 elif g >= 70.0:
  l="C"
 elif g >= 60.0:
  l="D"
 elif g < 60.0:
  l="F"
 return l

def run():
 g=float(input("Enter your CMPSC 131 grade:"))
 print(f"Your letter grade for CMPSC 131 is {grade(g)}")

if __name__ == "__main__":
 run()