import backendfunctions

answer = input("""
|||||||||||||||||||||||||||||||||||||||||||||
TTTTTTT    DDDDD       RRRRRR     DDDDD
  TTT      DD   DD     R     R    DD   DD
  TTT      DD    DD    RRRRRR     DD     DD
  TTT      DD    DD    R  R       DD     DD
  TTT      DD   DD     R   R      DD   DD
  TTT      DDDDD       R    R     DDDDD
           Treminal DnD Random Dice          
|||||||||||||||||||||||||||||||||||||||||||||
     Ready to start, Hero!? (y/n)?
""" )

if answer.lower().strip() == "y":
        answer = input("""
     1. Create New Character  2. Use Dice 3. Exit
        """ )

else:
        print("Ok, see you soon")
