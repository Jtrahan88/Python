print("""Welcome to TREASURE ISLAND
Your mission, if you can survive, is to find your treasure!

     .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '

""")

start = input("Type 'START' to start game: ").lower()
if start == 'start':
    print("""It is foggy out and you can not see where the boatman is going. All of a suddent a massive island apears. 
    You hop off the boat and the boatman's lets hope a high picthed laugh and asks you;
    
    
                            will you go left, right or straight?""")
    choice1 = input("Should we answer him? 'LEFT', 'Right', 'STRAIGHT', 'IGNORE'\n Your Choice: ").lower()
    
    if choice1 == 'right':
        print("A strange fog apears again adn you can not even see your hands. You fell into a pit filled with spikes!")
        print("""
                                                ,--.
                                               {    }
                                               K,   }
                                              /  ~Y`
                                         ,   /   /
                                        {_'-K.__/
                            GAME OVER     `/-.__L._
                                          /  ' /`\_}
                                         /  ' /
                                 ____   /  ' /
                          ,-'~~~~    ~~/  ' /_
                        ,'             ``~~~  ',
                       (                        Y
                      {                         I
                     {      -                    `,
                     |       ',                   )
                     |        |   ,..__      __. Y
                     |    .,_./  Y ' / ^Y   J   )|
                     \           |' /   |   |   ||
                      \          L_/    . _ (_,.'(
                       \,   ,      ^^'' / |      )
                         \_  \          /,L]     /
                           '-_~-,       ` `   ./`
                              `'{_            )
                                  ^^\..___,.--`

        """)
    else:
        print('ftw')

        
else:
    print("""
                            GAME OVER
                               .------.
                           ||'||||'|
                          ,|| -.._ |
                          \|`.-. .-.
                           | `-'A'-'
                           | ( --.`|
                          _|`.`___,'__   ____ 
                      _,-'_| _   _/   /';    `.
                   ,-/ / '     /     ; ;       )
                  / (__()     /     (__()\     |
                 |  (__()    |   __(__() : `--  \

                 \ _'__()`------'  (__() \       :
                 ;  |\/|           |\/;\  \      |
                 ;  '__'           |__| `. ;.__, (
                 :   \ /           ;\;|   /  \    ,--.
                 `._ \__\          ;__|  ;   |   /`.,-`.
                 /   |\/|          |\;|  |   :   \`/`.__\ 
                ;    |__|___ __ ___|__;__|    \   `\`/`._`.
                ,     |\;|   _\/_   |\/|\/|     \  _|`,`.`.,--.
                ;    ;|__|___\/\/___|__|__|      `( ,/ /.`/`.,-`.
                   ; |   ,   | |   `.    |       \`.;//;`\`/ ,. \

                                     `-  |        `::_;   `\ `' /
                                                            `--'

    
    
    
    
    """)
