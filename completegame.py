answer = input("""
||||||||||||||||||||||||||||||||||||||||||||||||
|||     Welcome to the Forgotten Forest      |||
||||||||||||||||||||||||||||||||||||||||||||||||
        Ready to survive the night? (Y/N)?
""" )

if answer.lower().strip() == "y":

        answer = input("""
        [Pick you option by writing a number]
        You wake with a big headache and everything is in flames around you. You look around and see a gun, a backpack and a knife. What do you do?
                        [1. Pick items up.  2. Start Exploring Around]                      
        """)

                if answer == "1":
                        answer = input(("""
                You check the gun and see that have one magazine in it. Then you check the bag and see that
                there is just one more magazine in it and some meds just in case anything goes wrong and also
                a power bar, 'Nice!' - you say to your self. Atlast you pick up the knife and get ready to
                get into the forest in front of you.
                                [1. Go Next Slide]                      
                """))

                elif answer == "2":
                        answer = input("""
                You check the gun and see that have one magazine in it. Then you check the bag and see that
                there is just one more magazine in it and some meds just in case anything goes wrong and also
                a power bar, 'Nice!' - you say to your self. Atlast you pick up the knife and get ready to
                get into the forest in front of you.
                                [1. Go Next Slide]                      
                """)

        else:
                print("Ok, see you soon")
