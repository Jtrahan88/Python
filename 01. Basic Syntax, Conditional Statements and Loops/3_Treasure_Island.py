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
    choice1 = input("Should we answer him? 'LEFT', 'RIGHT', 'STRAIGHT', 'IGNORE'").lower()
    
    if choice1 == 'right':
        print("""\n        A strange fog apears again and you can not even see your hands in front of you.
        
        
                            You fell into a pit filled with spikes!

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
    elif choice1 == 'left':
        print("""The boatman was waiting for you. His name is Charon, the son of Erebus and Nyx.
        
                        Charon takes you back to Hades who offers you to Cerberus!
                        
                                GAME OVER   
                                
                                                            ,--,  ,.-.
                                ,                   \,       '-,-`,'-.' | ._
                               /|           \    ,   |\         }  )/  / `-,',
                               [ '          |\  /|   | |        /  \|  |/`  ,`
                               | |       ,.`  `,` `, | |  _,...(   (      _',
                               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                               \  \_\,``,   ` , ,  /  |         )         _,/
                                 \  '  `  ,_ _`_,-,<._.<        /         /
                                  ', `>.,`  `  `   ,., |_      |         /
                                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                                \_,,.) /\    ` /  / ) (-,, ``    ,        |
                                ,` )  | \_\       '-`  |  `(               \
                                /  /```(   , --, ,' \   |`<`    ,            |
                              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
                        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
                       (-, \           ) \ ('_.-._)/ /,`    /
                       | /  `          `/ \\ V   V, /`     /
                    ,--\(        ,     <_/`\\     ||      /
                   (   ,``-     \/|         \-A.A-`|     /
                  ,>,_ )_,..(    )\          -,,_-`  _--`
                 (_ \|`   _,/_  /  \_            ,--`
                  \( `   <.,../`     `-.._   _,-`
                   `                      ```
        
        """)
    elif choice1 == 'straight':
        print(r"""
        You staied focused on the path and did not get distracted. 
        
                            You are RICH!
                   ____...------------...____
               _.-'` /o/__ ____ __ __  __ \o\_`'-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `''''-''''''''''''''''''''''''''-''''`
              """)
                            
                            
            
    else:
        print('''Trying to be a funny guy huh?!
        
                             Oppy doppy you died
                        
                             )               (
                            / \  .-"""""-.  / \        
                           (   \/ __   __ \/   )
                            )  ; / _\ /_ \ ;  (
                           (   |  / \ / \  |   )
                            \ (,  \0/_\0/  ,) /
                             \_|   /   \   |_/
                               | (_\___/_) |
                               .\ \ -.- / /.
                              {  \ `===' /  }
                             {    `.___.'    }
                              {             }
                               `"="="="="="`
                        
                        ''')

        
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
