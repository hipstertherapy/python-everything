file = open("stop-words.txt")
stopwords = file.readlines()

def testStop(sentence):
    for word in stopwords:
        next = word.strip()
        sentence = sentence.replace(" " + next + " ", " ")
    return sentence

#loop in the whole chat
while True:
    input = raw_input( " Whats your name ?")
    input = " " + input.capitalize() + " "
    name = testStop(input)
    name = name.replace(" name " , " ")
    print("Hi" + " " + name.strip())

    input1 = raw_input(" what's wrong ?")
    input1 = " " + input1
    print( "Great")

    input2 = raw_input(" So, how do you feel right now ? ")
    input2 = " " + input2 + " "
    name1 = testStop(input2)
    name1 = name1.replace(" feeling "," ")
    print(name1.strip() + " " +"eh?")

    input3 = raw_input(" Feeling " + name1.strip() + " is part of emotion, dont you agree ?")
    input3 = " " + input2 + " "
    name2 = testStop(input3)
    print("really ?")

    input = raw_input( " Whats your name ?")
    input = " " + input + " "
    name = testStop(input)
    name = name.replace(" name " , " ")
    print("Hi" + " " + name.strip())

    input3 = raw_input("see what i did there " + name.strip()+" ? ")
    input3 = " " + input2 + " "
    name2 = testStop(input3)
    msg = "hahaha....error"
    print(msg[0:9].capitalize() + msg[9:20].upper())

    

    

    

    
    

    



    #sentence = raw_input("really are you okay ?")
    #sentence = sentence.replace(test, "")
    # print(sentence)
