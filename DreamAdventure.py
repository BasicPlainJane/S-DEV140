from tkinter import *
root = Tk()
root.title('Dream Adventure')
root.geometry("700x350")
Font_tuple = ("Book Antiqua", 18, "italic", "bold")
Font_tuple2 = ("Book Antiqua", 13, "italic")
Font_tuple3 = ("Book Antiqua", 10)


root.config(cursor="heart")


def raise_frame(frame1):
    frame1.tkraise()


f1 = Frame(root, bg="#C4BCCB")
f2 = Frame(root, bg="#C4BCCB")
f3 = Frame(root, bg="#C4BCCB")
f4 = Frame(root, bg="#C4BCCB")
f5 = Frame(root, bg="#C4BCCB")
f6 = Frame(root, bg="#C4BCCB")
f7 = Frame(root, bg="#C4BCCB")
f8 = Frame(root, bg="#C4BCCB")
f9 = Frame(root, bg="#C4BCCB")
f10 = Frame(root, bg="#C4BCCB")
f11 = Frame(root, bg="#C4BCCB")
f12 = Frame(root, bg="#C4BCCB")
f13 = Frame(root, bg="#C4BCCB")
f14 = Frame(root, bg="#C4BCCB")
f15 = Frame(root, bg="#C4BCCB")
f16 = Frame(root, bg="#C4BCCB")
f17 = Frame(root, bg="#C4BCCB")
f18 = Frame(root, bg="#C4BCCB")
f19 = Frame(root, bg="#C4BCCB")
f20 = Frame(root, bg="#C4BCCB")
f21 = Frame(root, bg="#C4BCCB")
f22 = Frame(root, bg="#C4BCCB")
f23 = Frame(root, bg="#C4BCCB")
f24 = Frame(root, bg="#C4BCCB")
f25 = Frame(root, bg="#C4BCCB")
f26 = Frame(root, bg="#C4BCCB")
f27 = Frame(root, bg="#C4BCCB")
f28 = Frame(root, bg="#C4BCCB")

for frame in (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23,
              f24, f25, f26, f27, f28):
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, sticky="nsew")


label = Label(root, bg="#C4BCCB")
label.place(x=0, y=0)

Label(f1, font=Font_tuple, text='Welcome,'
                                '\n if you are ready to start your adventure' 
                                '\nclick the start button.', bg="#C4BCCB").pack()
Button(f1, bg='#BCC7A7', font=Font_tuple3, text='Start', command=lambda: raise_frame(f2)).pack()


Label(f2, font=Font_tuple2, text='You find yourself dreaming and come across this place, '
                                 '\n clouds cover all around you and there is only two things that you can make out.'
                                 '\n There is a bench and a staircase, which one will you choose? ', bg="#C4BCCB").pack()
Button(f2, bg='#BCC7A7', font=Font_tuple3, text='Go up the staircase', command=lambda: raise_frame(f3)).pack()
Button(f2, bg='#BCC7A7', font=Font_tuple3, text='Sit down on the bench', command=lambda: raise_frame(f4)).pack()

Label(f3, font=Font_tuple2, text='You step on to the staircase and it looks like glass under your feet. '
                                 '\n When you reach the top, the stairs seem to fade away and a hallway '
                                 '\nof doors come into view.'
                                 '\n There is a door on the right and a door on the left '
                                 '\nwhich door will you pick?', bg="#C4BCCB").pack()
Button(f3, font=Font_tuple3, bg='#BCC7A7', text='Open the first door on the right?', command=lambda: raise_frame(f5)).pack()
Button(f3, font=Font_tuple3, bg='#BCC7A7', text='Open the first door on the left?', command=lambda: raise_frame(f6)).pack()


Label(f4, font=Font_tuple2, text='You chose to sit on the bench but this is supposed to be an adventure'
                                 ' want to try again?', bg="#C4BCCB").pack()
Button(f4, bg='#BCC7A7', font=Font_tuple3, text='Restart?', command=lambda: raise_frame(f1)).pack()


Label(f5, font=Font_tuple2, text='As you step threw the door you are hit in the face'
                                 '\n with the sounds and smell of the sea.'
                                 '\n Your eyes adjust and you see a woman '
                                 '\nthe only other person here besides yourself. Will you talk to her?', bg="#C4BCCB").pack()
Button(f5, bg='#BCC7A7', font=Font_tuple3, text='walk along the beach.', command=lambda: raise_frame(f7)).pack()
Button(f5, bg='#BCC7A7', font=Font_tuple3, text='Talk to the woman?', command=lambda: raise_frame(f8)).pack()
Button(f5, bg='#BCC7A7', font=Font_tuple3, text='Take a swim in the ocean.', command=lambda: raise_frame(f9)).pack(),

Label(f6, font=Font_tuple2, text='As you walk threw the door you enter a building,'
                                 '\n you can see the outside from here due to windows all along the wall '
                                 '\n ahead of you, you can see a plain door and to the right is'
                                 '\n a see through door to the forest outside. ', bg="#C4BCCB").pack()
Button(f6, bg='#BCC7A7', text='Go see the forest outside? ', command=lambda: raise_frame(f14)).pack()
Button(f6, bg='#BCC7A7', text='choose the door that is probably inside?', command=lambda: raise_frame(f13)).pack()


Label(f7, font=Font_tuple2, text='As you walk along the beach you see a structure under the pier '
                                 '\nas you stride towards it you can make out its a cute little house '
                                 '\nyou walk up to it and knock but no answer what will you do? ', bg="#C4BCCB").pack()
Button(f7, bg='#BCC7A7', text='Open the door as it seems unlocked', command=lambda: raise_frame(f10)).pack()
Button(f7, bg='#BCC7A7', text='Wait for whoever lives here, to come home', command=lambda: raise_frame(f11)).pack()


Label(f8, font=Font_tuple2, text='You say hello to the woman and she smiles back.'
                                 '\nShe then tells you she will answer any question you may want to ask her. '
                                 '\nYou feel warm and safe with this woman although unsure why.', bg="#C4BCCB").pack()
Button(f8, bg='#BCC7A7', text='How did I get here ', command=lambda: raise_frame(f12)).pack()
Button(f8, bg='#BCC7A7', text='How do I get home.', command=lambda: raise_frame(f12)).pack()

Label(f9, font=Font_tuple2, text='You cant swim in a dream so you drown, restart.', bg="#C4BCCB").pack()
Button(f9, bg='#BCC7A7', text='Restart', command=lambda: raise_frame(f1)).pack()

Label(f10, font=Font_tuple2, text='You step through the door and what you see before you now is'
                                  '\n a small cottage and a little lake'
                                  '\n trees and flowers are in full bloom all round and the aroma alone is pleasing'
                                  ' to say the least,'
                                  '\n you decide this is a very cheerful place, '
                                  '\neven though its not at all like you thought it would be.', bg="#C4BCCB").pack()
Button(f10, bg='#BCC7A7', text='Walk over to peer into the pond?', command=lambda: raise_frame(f23)).pack()
Button(f10, bg='#BCC7A7', text='Head toward the cottage?', command=lambda: raise_frame(f24)).pack()

Label(f11, text='You wait all day it seems for someone to come home but a person doesnt actually come home'
                '\n till sunset and when they do and you see'
                '\n that it is a turtle and he is kind enough to offer you to come inside but before he does'
                '\n he gives you a small silver key with a smile.', bg="#C4BCCB").pack()
Button(f11, bg='#BCC7A7', text='Thank him and walk in.', command=lambda: raise_frame(f10)).pack()


Label(f12, text='It is no matter of how you came to be here, or how you are to leave it only matters about'
                '\n the journey that came and went. Her voice so melodious as she spoke.'
                '\n She gives you only one piece of advice and that is to go to the turtles house under the pier. '
                '\nShe also says she believes you will find the way out.'
                '\nWalking up to the charming little house will you open the door or wait for the turtle?').pack()
Button(f12, bg='#BCC7A7', text='Open the door as it is unlocked?', command=lambda: raise_frame(f10)).pack()
Button(f12, bg='#BCC7A7', text='Wait for the turtle to return?', command=lambda: raise_frame(f11)).pack()

Label(f13, text='So the door that you thought to be inside opens up to a hallway. You walk down the hallway'
                '\n but there is nothing out of the ordinary. You see a room full of books on bookcases'
                '\n and at the end of the hall you see another glass door looking out to the forest outside. .',
      bg="#C4BCCB").pack()
Button(f13, bg='#BCC7A7', text='Enter the room of books', command=lambda: raise_frame(f20)).pack()
Button(f13, bg='#BCC7A7', text='The door to the outside ', command=lambda: raise_frame(f14)).pack()

Label(f14, text='You step out side and with a deep breath of fresh air you can smell sweet pine but what now?.',
      bg="#C4BCCB").pack()
Button(f14, bg='#BCC7A7', text='Walk around the forest', command=lambda: raise_frame(f15)).pack()
Button(f14, bg='#BCC7A7', text='Walk around to the back side of this place?', command=lambda: raise_frame(f17)).pack()
Button(f14, bg='#BCC7A7', text='Go back to the door to go back in?', command=lambda: raise_frame(f16)).pack()

Label(f15, text='You walk around the forest but something you did not expect(or maybe you did) was this area is full of'
                'grizzly bears! \n You died please restart and be more careful.', bg="#C4BCCB").pack()
Button(f15, bg='#BCC7A7', text='Restart', command=lambda: raise_frame(f1)).pack()


Label(f16, text='You try to open the door but its locked and you cant get back in.', bg="#C4BCCB").pack()
Button(f16, bg='#BCC7A7', text='Walk around the forest?', command=lambda: raise_frame(f15)).pack()
Button(f16, bg='#BCC7A7', text='Walk around to the back?', command=lambda: raise_frame(f17)).pack()

Label(f17, text='As you walk around from the back you see another door and it is also see through.'
                '\nYou pull to open it and when you see its unlocked you walk in but there is two sets of stairs'
                '\n one that goes up and one that goes down.', bg="#C4BCCB").pack()
Button(f17, bg='#BCC7A7', text='Go upstairs', command=lambda: raise_frame(f18)).pack()
Button(f17, bg='#BCC7A7', text='Go downstairs', command=lambda: raise_frame(f19)).pack()

Label(f18, text='Once up the stairs you can see a door to the outside and another door '
                '\n both doors from when you first came here but now '
                '\n you are pulled to this other door.', bg="#C4BCCB").pack()
Button(f18, bg='#BCC7A7', text='Open the door', command=lambda: raise_frame(f13)).pack()

Label(f19, text='You step downstairs, you can barely see but there is a small window and light from outside'
                '\nglistens inside you now can tell you are in a basement there is nothing down here except'
                '\n as you follow the light from the window it highlight a small golden key on the ground.',
      bg="#C4BCCB").pack()
Button(f19, bg='#BCC7A7', text='Pick up the key then go up stairs?', command=lambda: raise_frame(f18)).pack()
Button(f19, bg='#BCC7A7', text='Leave the key and go upstairs?', command=lambda: raise_frame(f18)).pack()

Label(f20, text='You step into the room, it smells like old books and it reminds you of something or perhaps someone. '
                '\n You walk around the room with your fingers tapping the bindings of all the books when something '
                '\nseems out of place. A book is not pushed in all the way', bg="#C4BCCB").pack()
Button(f20, bg='#BCC7A7', text='Push the book back in?', command=lambda: raise_frame(f21)).pack()
Button(f20, bg='#BCC7A7', text='Pick the book up to look at it?', command=lambda: raise_frame(f22)).pack()

Label(f21, text='When you push the book in a secret door opens.', bg="#C4BCCB").pack()
Button(f21, bg='#BCC7A7', text='Go through the secret door.', command=lambda: raise_frame(f10)).pack()
Button(f21, bg='#BCC7A7', text='Look at the book', command=lambda: raise_frame(f22)).pack()

Label(f22, text='You pick up the book to look at it, the book title is '
                '\n"When one door closes another opens" after reading the book title you notice a secret door.', bg="#C4BCCB").pack()
Button(f22, bg='#BCC7A7', text='Go through the secret door.', command=lambda: raise_frame(f10)).pack()

Label(f23, text='You walk over to the pond and as you peer into it you become dazed and fall into the pond.'
                '\nWhile you are falling further and further away from the surface you hear a voice in your head'
                '\n"You must be more careful!"'
                '\n and because you cant swim in a dream you drown, restart.', bg="#C4BCCB").pack()
Button(f23, bg='#BCC7A7', text='Try again and be more careful?', command=lambda: raise_frame(f1)).pack()


Label(f24, text='You walk up to the little cottage and politely knock on the door that is '
                '\n exactly your height but fits the cottage perfectly. After a short time '
                '\na small man opens the door, not a small man but a dwarf. He gives you a kind smile and says'
                '\n "Hello stranger my name is Wilbur would you like to come in for a cup of tea?', bg="#C4BCCB").pack()
Button(f24, bg='#BCC7A7', text='Accept his offer for tea', command=lambda: raise_frame(f25)).pack()
Button(f24, bg='#BCC7A7', text='Decline and go to the pond', command=lambda: raise_frame(f23)).pack()

Label(f25, text='You step through the door and into the cottage. He offers a tiny chair '
                '\nand you both conduct small conversation as he gets the tea ready. Once the tea is ready '
                '\nyou take a sip and suddenly you have new found consciousness you understand'
                '\n you can create doors of your own to pass through from one place to another or even '
                '\nwake up at this point! ', bg="#C4BCCB").pack()
Button(f25, bg='#BCC7A7', text='Will you create a door?', command=lambda: raise_frame(f27)).pack()
Button(f25, bg='#BCC7A7', text='Are you ready to wake up?', command=lambda: raise_frame(f26)).pack()

Label(f26, text='You woke up! I hope you had a great adventure and thank you for playing my game.', bg="#C4BCCB").pack()


Label(f27, text='You once again step through the door only this time you created the door. '
                '\nYou find yourself back in the hallway that which you started only'
                '\nthe first two doors are gone. '
                '\nThe next two doors on the left and right say that it requires keys... ', bg="#C4BCCB").pack()
Button(f27, bg='#BCC7A7', text='Open the door on the left if you have the silver key?', command=lambda: raise_frame(f28)).pack()
Button(f27, bg='#BCC7A7', text='Open the door on the right if you have the gold key?', command=lambda: raise_frame(f28)).pack()
Button(f27, bg='#BCC7A7', text='Create your own door with no key needed?', command=lambda: raise_frame(f28)).pack()

Label(f28, text='Unfortunately the game ends here but I commend you for wanting to continue. '
                '\nThank you for playing perhaps sometime in the future you will be able to continue '
                '\ntill that day comes keep dreaming.', bg="#C4BCCB").pack()
Button(f28, bg='#BCC7A7', text='Would you like to play again?', command=lambda: raise_frame(f1)).pack()

raise_frame(f1)

root.mainloop()
