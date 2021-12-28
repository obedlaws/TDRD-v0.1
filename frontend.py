import backendfunctions

answer = input("""
|||||||||||||||||||||||||||||||||||||||||||||
TTTTTTT    DDDDD       RRRRRR     DDDDD
  TTT      DD   DD     R     R    DD   DD
  TTT      DD    DD    RRRRRR     DD     DD
  TTT      DD    DD    R  R       DD     DD
  TTT      DD   DD     R   R      DD   DD
  TTT      DDDDD       R    R     DDDDD
        Treminal DnD Random Dice v0.1   
|||||||||||||||||||||||||||||||||||||||||||||
           Simple Dice Version

        Ready to start, Hero!? (y/n)?
""" )
if answer.lower().strip() == "y":
        
        answer = input("""
      ///CHOOSE THE DICE YOU ARE LOOKIN FOR////

   1. D20   2. D12   3. D10   4. D8   5. D6   6. D4

        """ )
        if answer == "1":
                answer = backendfunctions.dtwenty
        if answer == "2":
                answer = print("YES")
        if answer == "3":
                answer = print("YES")
        if answer == "4":
                answer = print("YES")
        if answer == "5":
                answer = print("YES")
        if answer == "6":
                answer = print("YES")
                

else:
        print("Ok, see you soon")
