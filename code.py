import pygame
import math
import random

pygame.init()  # Important to initialize pygame to prevent any bugs or crash

# Display Setup
WIDTH, HEIGHT = 800, 500  # The dimensions of the pixels to be used in game.
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('HANGMAN!')

# Load images
images = []
for i in range(7):  # The number of images are 0 to 6 images.
    image = pygame.image.load("hangman" + str(i) + ".png")  # This would load the images as per there sequence.
    images.append(image)

# game variables
hangman_status = 0  # 0th image will be displayed initially
words = ["PYTHON", "NEW", "GAME", "GERMANY"]
word = random.choice(words)
guessed = []  # stores guessed letters

# Background colour
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# button variables
RADIUS = 20
GAP = 15  # variable for gap between two buttons
letters = []
startx = round((WIDTH - (GAP + RADIUS * 2) * 13) / 2)  # 13 is the total no. of buttons and 'round' means buttons are round
starty = 400
A = 65  # the uppercase A is represented by 65 in programming languages.
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])  # this will append x,y position,the letters and their visibility condition in the list.

# Fonts
LETTER_FONT = pygame.font.SysFont('arial', 30)
WORD_FONT = pygame.font.SysFont('arial', 40)
TITLE_FONT = pygame.font.SysFont('arial', 50)

# Setup game loops
FPS = 60
clock = pygame.time.Clock()  # Timer in the game
run = True


def draw():
    win.fill(WHITE)  # Proportions of R,G,B colours,to choose background colour.

    # draw title
    text = TITLE_FONT.render("HANGMAN!", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # draw word
    display_word = ""
    for letter in word :
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400,200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter  # this will split up the pairs in the list into two different variables. e.g. [[1,2],..] would be x=1, y=2
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS,3)  # we say pygame, draw me a cricle on the window(win), in black, from centre(x, y) not top-left with radius that I have defined and 3 units thick.
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y -text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))  # Displays the desired image on desired co-ordinates(here (150,200))
    pygame.display.update()  # Updates every frame with the changes we have made

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)

    for event in pygame.event.get():  # For any event like clicking or pressing a key,or quiting happens.

        if event.type == pygame.QUIT:  # For x button at the top, to quit the game
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # We need to click on the letter buttons.
            m_x, m_y = pygame.mouse.get_pos()  # Hence, we need to determine mouse position when it is clicked.
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y) **2)  # Pythagoras' theorem
                    if dis < RADIUS:
                        letter[3] = False  # when the letter is clicked, it should disappear
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("CONGRATULAIONS! " + "YOU WON")
        break
    if hangman_status == 6:
        display_message("Sorry! You Lost!")
        break


pygame.quit()
