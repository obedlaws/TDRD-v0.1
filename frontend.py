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
        while True:
                answer = input("""
        ///CHOOSE THE DICE YOU ARE LOOKIN FOR////

        1.[D20]  2.[D12]   3.[D10]   4.[D8]   5.[D6]   6.[D4]

                """ )
                if answer == "D20":
                        backendfunctions.dtwenty()
                if answer == "D12":
                        backendfunctions.dtwelve()
                if answer == "D10":
                        backendfunctions.dten()
                if answer == "D8":
                        backendfunctions.deight()
                if answer == "D6":
                        backendfunctions.dsix()
                if answer == "D4":
                        backendfunctions.dfour()
                else:
                        print("____________________________________________")
                        

else: 
        print("Ok, see you soon")