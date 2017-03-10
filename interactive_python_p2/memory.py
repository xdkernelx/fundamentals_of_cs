# implementation of card game - Memory
# Can be run on codeskulptor.org
# Preloaded Link - 

import simplegui, random

CARD_WIDTH = 50
CARD_LENGTH = 100
count = 0
guess = 0

# helper function to initialize globals
def new_game():
    global deck, exposed, cleared, prev
    deck = range(0, 8)
    deck.extend(deck)
    random.shuffle(deck)
    exposed = [0] * 16
    cleared = [0] * 16
    prev = -1
    count = 0
    guess = 0
    print deck
    pass  

     
# define event handlers
def mouseclick(pos):
    global prev, count, exposed, guess
    card_pos = pos[0] / 50
    if prev != card_pos:
        if exposed[card_pos] == 0:
            exposed[card_pos] = 1
            if deck[prev] == deck[card_pos]:
                cleared[prev] = 1
                cleared[card_pos] = 1
                guess = 0
            elif prev != -1:
                print deck[prev] == deck[card_pos]
                guess += 1
                print guess
                if guess == 2:
                    guess = 0
                    exposed = [0] * 16
        elif exposed[card_pos] == 1:
            exposed[card_pos] = 0
            
        prev = card_pos
    label.set_text("Turns = " + str(count))
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global CARD_WIDTH, CARD_LENGTH
    for n in range(len(deck)): 
        if (exposed[n] == 1 or cleared[n] == 1):
            canvas.draw_text(str(deck[n]), ((n * CARD_WIDTH), 75), 80, "Red")
        else:
            point_coords = [
                            [(n * CARD_WIDTH), 0], 
                            [((n + 1) *CARD_WIDTH), 0], 
                            [((n + 1)*CARD_WIDTH), CARD_LENGTH], 
                            [(n * CARD_WIDTH), CARD_LENGTH]
                          ]
            canvas.draw_polygon(point_coords, 4, "Black", "Blue")
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric