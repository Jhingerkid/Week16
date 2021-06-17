import random

firstNames = ["Bucko", "Flippy", "Zigso",
              "Marco", "Raddoci", "Doggo", "Floofer", "Doge"]
lastNames = ["Flomfer", "Chungo", "McFloof", "Ryklo",
             "Cronk", "Floochung"]
breeds = ["Corgi", "Terrier", "Lab", "Poodle",
          "Border Collie", "Pug", "Bulldog", "Pitbull"]
colors = ["Red", "Blue", "Yellow", "Green", "Purple", "Gray"]
conditions = ["Needs belly rubs", "Need for cuddles", "Infinite love",
              "Too Cute", "Extra Adorable",
              "Chungus", "GDS (Good dog syndrome)"]
dogList = []


class Dog:
    def __init__(self, firstName,
                 lastName, weight, breed, age, color, medical):
        self.first = firstName
        self.last = lastName
        self.weight = weight
        self.breed = breed
        self.age = age
        self.color = color
        self.medical = medical


def createDoggos():
    for x in range(5):
        newDog = Dog(firstNames[random.randint(0, 7)],
                     lastNames[random.randint(0, 5)],
                     random.randint(5, 80),
                     breeds[random.randint(0, 7)],
                     random.randint(1, 10),
                     colors[random.randint(0, 5)],
                     conditions[random.randint(0, 6)])
        dogList.append(newDog)


def askQuestion(question):
    answer = input(question)
    return answer


def showDogInfo(dogNumber):
    i = dogNumber-1
    print(f'{dogList[i].first} {dogList[i].last}\
 is a {dogList[i].color} {dogList[i].breed},\
 who weighs {dogList[i].weight} lbs. They are {dogList[i].age} years old,\
 and are afflicted with: {dogList[i].medical}')
    printDogList(dogList)


def addDog():
    prop1 = askQuestion("First name?")
    prop2 = askQuestion("Last name?")
    prop3 = int(askQuestion("Weight?"))
    prop4 = askQuestion("Breed?")
    prop5 = int(askQuestion("Age?"))
    prop6 = askQuestion("Color?")
    prop7 = askQuestion("Reason for visit?")
    newDoge = Dog(prop1, prop2, prop3, prop4, prop5, prop6, prop7)
    dogList.append(newDoge)
    printDogList(dogList)


def printDogList(dogs):
    print("Current Dogs:")
    for i, dog in enumerate(dogs):
        print(f'{i+1}. {dog.first} {dog.last}')
    print("__________________")
    print("1. Select a dog to know more about")
    print("2. Add a dog to the list")
    print("3. Exit Program")
    selectedOption = int(input(""))
    if selectedOption == 1:
        selectedDog = int(input(
            "Which one would you like to know more about?\n"))
        showDogInfo(selectedDog)
    elif selectedOption == 2:
        addDog()
    elif selectedOption == 3:
        return


createDoggos()
printDogList(dogList)
