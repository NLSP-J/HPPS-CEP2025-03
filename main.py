##### --- GAME SETTINGS --- #####

import pygame as pg
import time
import asyncio

pg.init()

white = (250, 250, 250)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the full window width and height
win_width = 400
win_height = 500
screen = pg.display.set_mode([win_width, win_height])
pg.display.set_caption('Tic-Tac-Toe')

font = pg.font.Font(None, 30)

player = 'X'
moves = 0
draw = False
winner = False
running = True

b_width = 400
b_height = 400
board = [['','','',''],
   ['','','',''],
   ['','','',''],
   ['','','','']]


X_img = pg.image.load('./assets/images/x_modified.png')
O_img = pg.image.load('./assets/images/o_modified.png')

X_img = pg.transform.scale(X_img, (70, 70))
O_img = pg.transform.scale(O_img, (70, 70))



##### --- UPDATE_TEXT FUNCTION --- #####

def update_text():

  global draw, player

  if draw:
    text = "It's a draw!"
  elif winner != False:
    text = f"Congrats! {winner} wins!"
  else:
    text = f"It's {player}'s turn"

  # Fill the entire screen to black colour
  screen.fill(black, (0, 400, 500, 100))
  # Render the text surface
  text = font.render(text, True, white)
  # Create rectangle object for text surface
  text_rect = text.get_rect(center=(b_width / 2, win_height-50))
  screen.blit(text, text_rect)  
 


##### --- GAME_WINDOW FUNCTION --- #####    

def game_window():

  screen.fill(white)

  # Draw vertical lines
  pg.draw.line(screen, black, (b_width / 4, 0),
        (b_width / 4, b_height), 7)
  pg.draw.line(screen, black, (b_width / 4 * 2, 0),
        (b_width / 4 * 2, b_height), 7)
  pg.draw.line(screen, black, (b_width / 4 * 3, 0),
        (b_width / 4 * 3, b_height), 7)

  # Draw horizontal lines
  pg.draw.line(screen, black, (0, b_height / 4),
        (b_width, b_height / 4), 7)
  pg.draw.line(screen, black, (0, b_height / 4 * 2),
        (b_width, b_height / 4 * 2), 7)
  pg.draw.line(screen, black, (0, b_height / 4 * 3),
        (b_width, b_height / 4 * 3), 7)
 
  update_text()



##### --- CHECK_WIN FUNCTION --- #####

def check_win():
   global draw, winner

  # Checks for winning rows
   for row in range(4):
     if board[row][0] == board[row][1] == board[row][2] == board[row][3] and board[row][0] != '':
      winner = board[row][0]
      pg.draw.line(screen, red,
            (0, (row + 1)*b_height / 4 - b_height / 6),
            (b_width, (row + 1)*b_height / 4 - b_height / 6),
            4)

  # Checks for winning columns
   for col in range(4):
    if board[0][col] == board[1][col] == board[2][col] == board[3][col] and board[0][col] != '':
      winner = board[0][col]
      pg.draw.line(screen, red, ((col + 1) * b_width / 4 - b_width / 6, 0),
            ((col + 1) * b_width / 4 - b_width / 6, b_height),4)

   if (board[0][0] == board[1][1] == board[2][2] == board[3][3]) and (board[0][0] != ''):
     winner = board[0][0]
     pg.draw.line(screen, red, (50, 50), (350, 350), 4)

   if (board[1][2] == board[2][1] == board[3][0] == board[0][3]) and (board[0][3] != ''):
     winner = board[0][3]
     pg.draw.line(screen, red, (350, 50), (50, 350), 4)

   if (winner == False and moves == 16):
     draw = True



##### --- DRAW_IMG FUNCTION --- #####

def draw_img(row, col):
  global board, player

  if row == 1:
    posy = 15
  elif row == 2:
     posy = (b_width / 4 + 15)
  elif row == 3:
     posy = (b_width / 4 * 2 + 15)
  elif row == 4:
    posy = (b_width / 4 * 3 + 15)

  if col == 1:
     posx = 15
  elif col == 2:
     posx = (b_height / 4 + 15)
  elif col == 3:
     posx = (b_height / 4 * 2 + 15)
  elif col == 4:
    posx = (b_height / 4 * 3 + 15)

  board[row-1][col-1] = player

  if player == 'X':
    screen.blit(X_img, (posx, posy))
    player = 'O'

  else:
    screen.blit(O_img, (posx, posy))
    player = 'X'



##### --- CHECK_CLICK FUNCTION --- #####

def check_click():

    x,y = pg.mouse.get_pos()

    if(x < b_width / 4):
      col = 1
    elif (x < b_width / 4 * 2):
      col = 2
    elif (x < b_width / 4 * 3):
      col = 3
    elif(x < b_width):
      col = 4
    else:
      col = 'Invalid'
    if(y < b_height / 4):
      row = 1
    elif (y < b_height / 4 * 2):
      row = 2
    elif (y < b_height / 4 * 3):
      row = 3
    elif(y < b_height):
      row = 4
    else:
      row = 'Invalid'

    if(row != 'Invalid' and col != 'Invalid' and board[row-1][col-1] == ''):
        global moves
        moves += 1
        draw_img(row, col)


##### --- EVENT HANDLERS --- #####

game_window()

async def main():
  global running
  
  while running:

    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
      elif event.type == pg.MOUSEBUTTONDOWN:
        check_click()
    if draw or winner != False:
      time.sleep(2)
      running = False

    check_win()
    update_text()

    pg.display.update()
    await asyncio.sleep(0)

asyncio.run(main())
