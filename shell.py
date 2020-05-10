import interpreter

while True:
    text = input('test > ')
    result,error = interpreter.run('<stdin>',text)

    if error != None:
        #print("it's an error")
        #adding this comment just to initialize git
        print(error.as_string())
    else:
        #print("it's not an error....its a ast")
        print(result)