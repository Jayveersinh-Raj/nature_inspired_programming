# to validate input according to the program, although it accepts from ascii 65-122, and 32, 46
def take_valid_input():
  notValid = True
  # valid discontinues ascii values
  valid = [32, 46]
  # until a valid input is achieved
  while notValid:
      target = input("Enter your to be guessed target string >")
      ascii_target = [ord(ch) for ch in target]
      
      for ascii in ascii_target:
        if(ascii<32 or ascii>125):
            if(ascii in valid):
                notValid = False
            else:
                print("Please enter a valid string")
        else:
            notValid = False

  return target