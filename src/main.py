import time
time.sleep(1)

while True:
    name = input("What's your name?  ")
    import time
    time.sleep(2)
    print()
    print("So your name is " + name)
    import time
    time.sleep(1)
    print()
    nameResponse = input("Is this correct?  ")
    print()
    if nameResponse.lower() in ["yes", "y", "yes", "yeah", "yep"]:
        break
        print()
setupChoice = input("Would you like the quick setup, or the detailed setup?  ")
import time
time.sleep(1)
print()
if setupChoice.lower() in ["d", "detailed"]:

  gender = input("Are you a boy or a girl?  ")
  import time
  time.sleep(1)
  print()
  if gender.lower() in ["boy", "man", "guy", "male", "m"]:
   print("I hope you can protect all who you meet!")
  elif gender.lower() in ["girl", "woman", "lady", "female", "f"]:
    print("Stay safe out there, and don't let people hurt you!")
  

  import time
  time.sleep(1)
  print()
  favColor = input("What's your favorite color?  ")
  print()
  # Reds
  if favColor.lower() in ["red", "rd"]:
    print("I hope you don't like blood, too!")
  # Red-Oranges
  # Oranges
  # Yellow-Oranges
  # Yellows
  elif favColor.lower() in ["yellow", "yllw", "y"]:
    print("I bet your personality reflects that!")
  # Yellow-Greens
  # Greens
  elif favColor.lower() in ["green", "grn"]:
    print("Calm as swaying trees and soft grass.")
  # Blue-Greens
  elif favColor.lower() in ["teal"]:
    print("")
  elif favColor.lower() in ["sea green", "seafoam"]:
    print("Natural and beautiful, yet non-living.")
  elif favColor.lower() in ["turquoise"]:
    print("")
  # Blues
  elif favColor.lower() in ["blue", "blu"]:
    print("Like the sky?")
  elif favColor.lower() in ["midnight blue"]:
    print("I bet your personality goes as deep as the vast expanse of the universe.")
  # Blue-Purples
  # Purples
  elif favColor.lower() in ["violet", "purple"]:
    print("I sence a royal elegance in you.")
  # Blacks
  elif favColor.lower() in ["black", "blck"]:
    print("Like the vast expanse of space...")
  # Browns
  elif favColor.lower() in ["copper", "copp"]:
    print("Copper's just a start, right?")
  # Whites
  # Other
  elif favColor.lower() in [""]:
    print("")
  elif favColor.lower() in [""]:
    print("")
  elif favColor.lower() in [""]:
    print("")
  else:
    print("Please remember this is still in beta, so send me any ideas for colors to add.")



  import time
  time.sleep(1)
  print()
  domHand = input("Do you perform tasks mostly with your left hand, right hand, or both?  ")
  import time
  time.sleep(1)
  print()
  if domHand.lower() in ["l", "left"]:
    print("That is very unique, and you should embrace it.")
  if domHand.lower() in ["r", "right"]:
    print("Old fashioned, I see.")  
  elif domHand.lower() in ["both", "ambidextrious", "left and right", "l and r"]:
    print("If something happens to one hand, at least you'll still be able to hold your own.")
  import time
  time.sleep(1)
  print()
  fightingStyle = input("Do you prefer to cast spells, power through enemies, or defeat them with finesse?  ")
  import time
  time.sleep(1)
  print()
  battleLove = input("Do you plan to settle down and find love, or keep going, defending the world?  ")
  import time
  time.sleep(1)
  print()
  if battleLove.lower() in ["love", "settle", "settle down", "find love"]:
    print("I hope you make it through long enough to.")
  elif battleLove.lower() in ["going", "defending", "keep going", "defending the world"]:
    print("Don't be gone too long. There may be someone waiting for you back home.")
  import time
  time.sleep(1)
  print()
  protDest = input("Will you protect your friends, or destroy your enemies?  ")
  if protDest.lower() in ["protect", "prot", "pro", "p"]:
    print("It may be hard at times, but doong the right thing WILL pay off.")
  elif protDest.lower in ["destroy", "dest", "destro", "d"]:
    print("Just make sure you aren't doing it selfishly, or in cold blood.")
  import time
  time.sleep(1)
  print()
  murder = input("If you had to, if you couldn't think of any other choice, would you kill someone?  ")
  if murder.lower() in ["yes", "y", "yeah", "probably"]:
    print("I hope it never leads to that, but if it does, remember to keep a noble cause.")
  elif murder.lower() in ["no", "never", "of course not"]:
    print("Keep that kindness in your heart, and you will go far.")
  import time
  time.sleep(1)
  print()
  loveInput = input("Is there anyone you catch yourself staring at or wanting to be near more than others?  ")
  if loveInput.lower() in ["y", "yes"]:
          loveLife = ("do") 
  print()
  import time
  time.sleep(1)
  if loveInput.lower() in ["yes", "y", "yeah"]:
    print("I wonder if they think of you the same way...")
  greatestFear = input("What are you most afraid of?  ")
  import time
  time.sleep(1)
  print()
  if greatestFear.lower() in ["death", "dying", "being killed", "being dead"]:
    print("Don't let it rule your life.")
  elif greatestFear.lower() in ["lonliness", "being alone", "alone", "lonely"]:
    print("Don\'t worry. There are more people who care than you may think.")
  elif greatestFear.lower() in ["change", "difference", "foreign concepts"]:
    print("Doesn't life ever get boring?")
  elif greatestFear.lower() in ["long words", "big words"]:
    print("How can you convey a meaning using only small words?")
  elif greatestFear.lower() in ["blood", "bleed", "bleeding"]:
    print("Don't worry. Seeing blood won't kill you. Unless it's spewing from your head.")
  import time
  time.sleep(1)
  print()
  values = input("Do you care most about friends, reputation, or personal property?  ")
  print()
  import time
  time.sleep(2)
  if values.lower() in ["friends"]:
    print("So you understand something of life.")
    import time
    time.sleep(1)
    print()
  print("So your name is" + name + ", your favorite color is " + favColor + ", you " + loveLife + " love somebody, you prefer to fight ")
  import time
  time.sleep(1)
  print()



print("Hey, it's time to get out of bed!")
import time
time.sleep(1)
print()
print("The neighbors' back yard was broken into again!")
import time
time.sleep(1)
print()
help = input("Are you going to help them?  ")
import time
time.sleep(1)
print()
if help.lower() in ["yes"]:
  print("You get out of bed, and go to the neighbor's house.")
