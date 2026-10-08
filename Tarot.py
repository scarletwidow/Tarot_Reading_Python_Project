import random

#Tarot Card Draw Project. I have to build a terminal program that welcomes user, asks what they want their reading on.
#and what kind of three card reading they want
print("***********************")
print("Welcome to Tara's Tarot")
print("***********************")

#List of all the cards in a traditional tarot deck
tarot_deck = ["1 The Fool", "2 The Magician", "3 Empress", " 4 Emperor", "5 Hierophant", "6 The Lovers", "7 The Chariot", "8 Strength", "9 The Hermit", "10 Wheel of Fortune", "11 Justice", "12 The Hanged Man", "13 Death", "14 Temperance", "15 The Devil", "16 The Tower", "17 The Star", "18 The Moon", "19 The Sun", "20 Judgment", "21 The World",
"Ace of Wands", "One of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands",
"Ace of Cups", "One of Cups", "Two of Cups", "Three of Cups", "Four of Cups", "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups",
"Ace of Pentacles", "One of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles", "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles",
"Ace of Swords", "One of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords"]

def pick_tarot_card():
    #use random.choice method from imported random module to set the variables to three random cards from the tarot_deck list
    random_card1 = random.choice(tarot_deck)
    random_card2 = random.choice(tarot_deck)
    random_card3 = random.choice(tarot_deck)

    #logic to ensure that the same "card" isn't pulled from the tarot_desk list 
    if random_card2 == random_card1:
        random_card2 = random.choice(tarot_deck)
    if random_card3 == random_card2:
        random_card3 = random.choice(tarot_deck)
    if random_card3 == random_card1:
        random_card3 == random.choice(tarot_deck)

    #return three random "card" from tarot_desk list
    return random_card1, random_card2, random_card3

#Get user input for name
user_name = input("Thank you for entering the shop today, the cards told me you were coming but they didn't tell me your name. What should I call you? (Type your name then hit enter) ")
#Get user input for what they want a reading on
reading_for = input("Hello " + user_name + " welcome in. What would you like a reading on today? (Relationship, Career, or Personal Growth) ")

#Logic for what kind of three card drawing they want based on which type of reading they picked
if reading_for == "Relationship":
    reading_type = input("So " + user_name + " would you like your " + reading_for + " reading spread to be Past/Present/Future or Situation/Obstacle/Advice? ")
elif reading_for == "Career":
    reading_type = input("So " + user_name + " would you like your " + reading_for + " reading spread to be Past/Present/Future or Situation/Obstacle/Advice? ")
elif reading_for == "Personal Growth":
    reading_type = input("So " + user_name + " would you like your " + reading_for + " reading spread to be Past/Present/Future or Situation/Obstacle/Advice? ")
else:
    reading_for = input("Sorry that's not one of the offered options. Please type Relationship, Career, or Personal Growth ")

#Depending on what kind of drawing user picked give them a personalized answer
if reading_type == "Past/Present/Future":
    print(user_name + ", your cards for the Past, Present, and Future are: ", pick_tarot_card())
elif reading_type == "Situation/Obstacle/Advice":
    print(user_name + ", your cards for the Situation, Obstacle, and Advice are: ", pick_tarot_card())
else:
    reading_type = input("Sorry that's not one of the offered options please type: Past/Present/Future or Situation/Obstacle/Advice")

#print(pick_tarot_card())