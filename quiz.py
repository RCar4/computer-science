def question1():
    print("question 1")
    print("what is the largest single exposure of limestone rock?")
    print("is it: ")
    print("a. ularu/ayers rock")
    print("b. bryce canyon national park")
    print("c. the nullarbor")
    choice = input()
    if choice == 'a':
        print("ularu is not the correct answer")
        print("Uluru, or Ayers Rock, is a massive sandstone monolith in the heart of the Northern Territory’s arid Red Centre. The nearest large town is Alice Springs, 450km away. Uluru is sacred to indigenous Australiansand is thought to have started forming around 550 million years ago.")
        return question1()
    
    elif choice == 'b':
        print("the bryce canyon national park is not correct")
        print("Bryce Canyon National Park, a sprawling reserve in southern Utah, is known for crimson-colored hoodoos, which are spire-shaped rock formations. The park’s main road leads past the expansive Bryce Amphitheater, a hoodoo-filled depression lying below the Rim Trail hiking path.")
        return question1()
    elif choice == 'c':
        print("the nullarbor is correct")
        print("It is the world's largest single exposure of limestone bedrock, and occupies an area of about 200,000 square kilometres")
        return question2()
    else:
        return question1()



def question2():
    print("question 2")
    print("why do chickens have gyroscopic heads?")
    print("is it: ")
    print("a. so they can eat easier")
    print("b. because they cant move their eyes")
    print("c. to impress females")
    choice = input()
    if choice == 'a':
        print("so they can eat easier is not the correct answer")
        return question2()
    elif choice == 'b':
        print("because they cant move their eyes is correct")
        print("chicken unlike humans cant move their eyes around to stabilize their sight while hunting or moving over rough terrain, so their necks act to stabilize movement on the x, y and z axis as well as rotational axis so they can see their target easier.")
        return question3()
    elif choice == 'c':
        print("to impress females is incorrect")
        return question2()
    else:
        return question2()


def question3():
    print("question 3")
    print("which of these is true?")
    print("is it: ")
    print("a. the city of troy")
    print("b. you can see the Great Wall of China from space")
    print("c. alcohol keeps you warm")
    choice = input()
    if choice == 'a':
        print("the city of troy is the correct answer")
        print("The ancient city of Troy, which was once believed to be a myth, was discovered by Heinrich Schliemann in the 19th century, proving the legendary city was real.")
        return question4()
    elif choice == 'b':
        print("you can see the great wall of china from space is not correct")
        return question3()
    elif choice == 'c':
        print("alcohol keeps you warm is not correct")
        print("Alcohol causes blood vessels near the skin to dilate, giving a temporary feeling of warmth but leading to heat loss from the body.")
        return question3()
    else:
        return question3()



def question4():
    print("question 4")
    print("what is the native animal of new zealand?")
    print("is it: ")
    print("a. the casuary")
    print("b. the kiwi bird")
    print("c. the takahe")
    choice = input()
    if choice == 'a':
        print("the casuary in not the correct answer")
        return question4()
    elif choice == 'b':
        print("the kiwi bird is correct")
        return question5()
    elif choice == 'c':
        print("the takahe is not the correct answer")
        return question4()
    else:
        return question4()


def question5():
    print("question 5")
    print("which bone is known as the funny bone?")
    print("is it: ")
    print("a. the tibia")
    print("b. the fibia")
    print("c. the humorouse")
    choice = input()
    if choice == 'a':
        print("the tibia in not the correct answer")
        return question5()
    elif choice == 'b':
        print("the fibia in not the correct answer")
        return question5()
    elif choice == 'c':
        print("the humorouse is correct")
        return question1()
    else:
        return question5()




question1()
question2()
question3()
question4()
question5()