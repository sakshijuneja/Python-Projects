boat=('''    __/\__
  ~~~\____/~~~~~~
    ~  ~~~   ~.   ''')


door=('''            __________
           |  __  __  |  
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|''')


print(r'''

                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You are standing on a mountain with darkness all around.")
direction=input("Which direction would you choose? left or right?\n").lower()
# direction.lower()

if direction=="left":
  print("Wow, You have reached the river.")
  choose=input("swim or wait? \n").lower()
  # choose.lower()
  if choose=="wait":
    print("Nice,A boat has come to drop you safely to an Island.")
    print(boat)
    print("You have reached the Island.There a three doors in front of you.Behind the red door, there is a deadly poisonous gas. Behind the green door,there are trained assassins with knives. Behind the blue door, there are lions that have not eaten in years.")
    print(door)
    door=input("Enter the color of door which you would choose to open.").lower()
    # door.lower()
    if door=="red":
      print("GAME OVER!")
    elif door==("green"):
      print("GAME OVER!")
    elif door==("blue"):
      print("CONGRATULATIONS,You found the tressure. YOU WIN!")
    else:
      print("You choose a color that does'nt exist, GAME OVER!")
  else:
    print("You are attacked by Crocodiles. GAME OVER!")  


else:
  print("Oops! You fall from the mountain. GAME OVER :(")