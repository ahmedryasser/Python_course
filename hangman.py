try == 0
while word != "hello" or:
    guess = input(" Whats your guess, choose a letter ")

    if guess == "h":
        print("H _ _ _ _")
            if guess == "h":
              print (" You have already guessed this ")

            elif guess == "e":
                print("H e _ _ _")
                      if guess == "h" or guess = "e":
                          print (" You have already guessed this ")

                      elif guess == "l":
                          print("H e l l _")
                          if guess == "o":
                                print (" You won ")
                          elif guess == "h" or guess == "e" or guess == "l":
                                print (" You have already guessed this ")
                          else:
                              print(" Try again ")
                              try = try + 1
              
                      elif guess == "o":
                          print("H e _ _ o")
                          if guess == "l":
                                print (" You won ")
                          elif guess == "h" or guess == "e" or guess == "o":
                                print (" You have already guessed this ")
                          else:
                              print(" Try again ")
                              try = try + 1
                      else:
                          print(" Try again ")
                          try = try + 1


            elif guess == "l":
                print("H _ l l _"
                if guess == "h" or guess = "l":
                    print (" You have already guessed this ")

                elif guess == "e":
                    print("H e l l _")
                          if guess == "o":
                                print (" You won ")
                          elif guess == "h" or guess == "e" or guess == "l":
                                print (" You have already guessed this ")
                          else:
                              print(" Try again ")
                              try = try + 1
              
                elif guess == "o":
                          print("H _ l l o")
                          if guess == "e":
                                print (" You won ")
                          elif guess == "h" or guess == "e" or guess == "o":
                                print (" You have already guessed this ")
                          else:
                              print(" Try again ")
                              try = try + 1
                else:
                    print(" Try again ")
                    try = try + 1
            elif guess == "e":
                print("H e _ _ _")
                
        
            elif guess == "o":
                print("H _ _ _ o")

            else:
                print(" Try again ")
                try = try + 1

              
    elif guess == "e":
        print("_ e _ _ _")

    elif guess == "l":
        print("_ _ l l _")

    elif guess == "e":
        print("_ e _ _ _")
        
    elif guess == "o":
        print("_ _ _ _ o")

    else:
        print(" Try again ")
        try = try + 1

    if try == 6:
        print("you lost")
        break    
