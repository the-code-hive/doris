print("Hello!")
name=input("What is your name? ")
print("Hi",name)

feels=input("How are you? ")

if feels.lower()=="good"or"fine"or"okay"or"great":
    print ("That's not bad! I'm doing well.")
elif feels.lower()=="bad"or"sad"or"mad"or"annoyed"or"ugh":
    print ("Oh that's too bad! I'm sorry.")
else:
    print ("I'm doing well")

interests=["art","sports","music","chess","playing games","being around people","coding","reading","writing"]
iv=[art, sports, music, chess, playing_games, being_around_people, coding, reading, writing]

for x in interests:
    iv=input("Do you like " + x + ", yes or no? ")
    if iv[0].lower()=="yes" or "yeah":
        print ("I like art too!")
        user_art=input("Do you like to draw or paint? ")
        
    
