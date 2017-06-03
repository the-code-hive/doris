#have house variables equal to personality traits
#ask wizard/witch what adjecitive is most like their personality
#determine house
#print house

name= input("What is your name? ")
print(name)

points=0
trait=input("Do you consider yourself to be brave, cunning, smart, or friendly? ")

if trait.lower()=="friendly":
    points +=5
elif trait.lower()=="brave":
    points +=10
elif trait.lower()=="smart":
    points +=15
elif trait.lower()=="cunning":
    points +=20
else:
    points +=0


blood=input("Are you a muggleborn, half-blood, or pureblood? ")

if blood.lower()=="muggleborn":
    points +=5
elif blood.lower()=="half-blood":
    points +=6
elif blood.lower()=="pureblood":
    points +=10
else:
    points +=0


color=input("What is your favorite color? ")
    
if color.lower()=="blue":
    points +=4
elif color.lower()=="purple":
    points +=4
elif color.lower()=="red":
    points +=2
elif color.lower()=="gold":
    points +=2
elif color.lower()=="green":
    points +=6
elif color.lower()=="silver":
    points +=6
elif color.lower()=="grey":
    points +=6
elif color.lower()=="black":
    points +=6
elif color.lower()=="yellow":
    points +=0
elif color.lower()=="orange":
    points +=0
elif color.lower()=="white":
    points +=0
else:
    points +=0


if points >=30:
    print ("SLITHERIN!!!! (Hisses and cheering in the background)")
elif  (points >=23) and (points <=29):
    print ("RAVENCLAW!!!!!! (Fluttered paper and dropped quills and cheers fill the background)")
elif (points >=16) and (points <=22):
    print ("GRYFFINDOR!!!! (Cheers and Gryffindors beating their chests fill the air)")
elif (points >=10) and (points <=15):
    print ("HUFFLEPUFF!!!! (Polite cheers and clapping coming from the Hufflepuff table)")
else:
    print ("You have been escorted off the grounds and back to your muggle home.")
