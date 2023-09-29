#Lambo, a 'Camel-Based Game' created by Justin Lee

#Start Menu
#Game Variables
import random
bolDone = False
bolEmpty = False 
intBoot = 5
intFuel = 0 
intCarMiles = 0
intCopsMiles = -20
intMotor = 0
intDifficulty = 300
intNitrousUsed = 0
intNitrous = 3
intMoney = 500
intMotorLevel = 1
intWeather = "Sunny" #stormy, wavy ( do womething with tidal waves), sunny, boiling, freezing, rainstor with lkightning
bolElectroConductor = False #gives you fuel but has 5% chance of electrocuting you.  
bolHardWheels = False #immune to spikes but slip in the rain. 
bolBPShell = False
bolBPWindows = False 
bolSponsors = False #make you money you drive.
bolQuantumShield = False 
bolShopDone = False
bolVictory = False

#Car Graphics
road1 = "you  elon  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road2 = "you  ===  elon  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road3 = "you  ===  ===  elon  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road4 = "you  ===  ===  ===  elon  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road5 = "you  ===  ===  ===  ===  elon  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road6 = "you  ===  ===  ===  ===  ===  elon  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road7 = "you  ===  ===  ===  ===  ===  ===  elon  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road8 = "you  ===  ===  ===  ===  ===  ===  ===  elon  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road9 = "you  ===  ===  ===  ===  ===  ===  ===  ===  elon  ===  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road10 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon  ===  ===  ===  ===  ===  ===  ===  ===  === ==="
road11 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon  ===  ===  ===  ===  ===  ===  ===  === ==="
road12 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon  ===  ===  ===  ===  ===  ===  === ==="
road13 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon  ===  ===  ===  ===  ===  === ==="
road14 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon  ===  ===  ===  ===  === ==="
road15 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon  ===  ===  ===  === ==="
road16 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon  ===  ===  === ==="
road17 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon  ===  === ==="
road18 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon  === ==="
road19 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  elon ==="
road20 = "you  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  ===  === elon"
road21 = "you ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  == elon  ==  ==  ==  =="
road22 = "you ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  == elon  ==  ==  =="
road23 = "you ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  == elon  ==  =="
road24 = "you ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  == elon  =="
road25 = "you ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  == elon"
road51 = "you = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = = = = = = = = = = " 
road52 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = = = = = = = = = " 
road53 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = = = = = = = = " 
road54 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = = = = = = = " 
road55 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = = = = = = " 
road56 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = = = = = " 
road57 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = = = = " 
road58 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = = = " 
road59 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = = " 
road60 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = = " 
road61 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = = " 
road62 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = = " 
road63 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = = " 
road64 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = = " 
road65 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = = " 
road66 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = = " 
road67 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = = " 
road68 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = = " 
road69 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = = " 
road70 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = = " 
road71 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = = " 
road72 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon = " 
road73 = "you = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = elon " 
roadxl = "you ==  ==  ==  == ==  ==  ==  elon   is   too  far  away  to  display  data  ==  ==  ==  ==  ==  ==  ="

print("||======================================================================================================||")
print()
print("Welcome, to... ")
print()
print("   ▄▄▄▄▀ ▄███▄     ▄▄▄▄▄   █    ██   ")
print("▀▀▀ █    █▀   ▀   █     ▀▄ █    █ █  ")
print("    █    ██▄▄   ▄  ▀▀▀▀▄   █    █▄▄█ ")
print("   █     █▄   ▄▀ ▀▄▄▄▄▀    ███▄ █  █ ")
print("  ▀      ▀███▀                 ▀   █ ")
print("                                  █  ")
print("                                 ▀   ")
print("... a Camel-based game created by Justin lee.")
print("NOTE: Please play in fullscreen")
print()
print("||======================================================================================================||")
print("Before beginning, please enter a few custom details.")
print("||======================================================================================================||")
print()
print("Customise the name of your friends [e.g, 'Ruby']")
print()
print("Friend 1: ")
friendOne = input("NAME: ")
print()
print("Friend 2: ")
friendTwo = input("NAME: ")
print()
print("Friend 3: ")
friendThree = input("NAME: ")
print()
print("Your friend's are",friendOne,",",friendTwo,"and",friendThree)
print()
print("--------------------")
print("Level of Difficulty (default = moderate)")
print()
print("[A] Certain")
print("[B] Easy")
print("[C] Moderate")
print("[D] High")
print("[E] Insane")
print("[F] Impossible")
print()
print("[S] Sandbox (Great for learning game strategies.) ")
print("--------------------")
print()
user_difficulty = input("Choice: ")


#A

if user_difficulty.upper() == "A":
    bolDone = True
    intDifficulty = 0
    print("||=====================================================================================================||")
    print("      Congratulations, you won! No, this is not a glitch or bug, you had a 100% chance of winning.")
    print("||=====================================================================================================||")

elif user_difficulty.upper() == "B":
    intDifficulty = 200
    intCopsMiles = -35
    intBoot = 6
    intFuel = 0 
    intCarMiles = 0
    intMotor = 0
    intNitrous = 4
    intMoney = 700
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")
    print("Your game difficulty has been set to easy (you can do better, Mr Anderson!) ")
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")

elif user_difficulty.upper() == "C":
    intDifficulty = 300
    intCopsMiles = -25
    intBoot = 5
    intFuel = 0 
    intCarMiles = 0
    intMotor = 0
    intNitrous = 4
    intMoney = 600
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")
    print("Your game difficulty has been set to moderate.")
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")

elif user_difficulty.upper() == "D":
    intDifficulty = 400
    intCopsMiles = -20
    intBoot = 4
    intFuel = 0 
    intCarMiles = 0
    intMotor = 0
    intNitrous = 3
    intMoney = 400
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")
    print("Your game difficulty has been set to high, good luck!")
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")

elif user_difficulty.upper() == "E":
    intDifficulty = 1000
    intCopsMiles = -15
    intBoot = 4
    intFuel = 0 
    intCarMiles = 0
    intMotor = 0
    intNitrous = 3
    intMoney = 250
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")
    print("Your game difficulty has been set to insane.")
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")

elif user_difficulty.upper() == "F":
    bolDone = True
    intDifficulty = "0"
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")
    print("Your game difficulty has been set to Impossible. You never began the game. You cannot win the game.")
    print("Therefore, you lose. Thanks for playing!")
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")

elif user_difficulty.upper() == "S":
    intDifficulty = "1000"
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")
    print("Your game difficulty has been set to Sandbox. You have all items from the shop.  ")
    print("||/////////////////////////////////////////////////////////////////////////////////////////////////////||")
    bolElectroConductor == True 
    bolHardWheels == True
    bolBPShell == True
    bolBPWindows == True
    bolSponsors == True

    bolQuantumShield == True
    intBoot == 999
    intNitrous == 999 
    

while not bolDone: 

    print()
    print("You and your friends",friendOne,",",friendTwo, "and", friendThree, "were walking down beautiful Beach Road..")
    print("when you saw an unlocked Tesla on the street!                                                 ")
    print()
    print("||=====================================================================================================||")
    print("||ddddhhhhhyyyyyysssssssssssssooooooosssy/                                      `````````.......--+dsNd||")
    print("||dhhhhyyyyyssssssooooo++///::::::::::://-```````                                  ``````````...../hsNd||")
    print("||hhhyyyyyssssoo+////:/syyyyyyssssoososoooooo++/:-.````````.`````                      ````.-.````:hsNd||")
    print("||hhyyyssssooo++/ssyh+ssNMNNmmddddmmdhhhddhyyhysyyhysoo+/:.``...``.....```````````         `..````-hsNd||")
    print("||hysssooo+++o:.+osyhhsoyMMMMNNNmdmmmNmdyyhddhyyyysyhyy//+yy+::-............-----..-..``````..````.hoNh||")
    print("||hhyyysssosd../oosyssoo/mMMhyyyyhyyhddmNyyddmNdshddhhyy/+hhhhys+/-.`````...-::----:::-.---:/-````.y+my||")
    print("||yyyyyyysomy++++//oy+y//+NMNysoo+oshdhydNdyhddmdyhysdhhhdhhhdh/+sso/-.........--//++:---:::/:os/oy+:y+||")
    print("||+/:-.:/:./mdhhyssohdNy+/+ydmmddddmmdhhhddhyyyhdhyhhdhhhhdhhhho++osyso++:.`.......-:/oooo+++oyysydosdN||")
    print("||yo+s:+o/-.:/++ooooydds:-.::--.--:::--::--...................----------::`  ``````:shysyhhdmmNhddNMMmN||")
    print("||/:o///:::----.--::-+so:-.......``````...--..` `...........``````````            `-+syhddmMMMMMMMMMMMN||")
    print("||++ooyosydh+//-.````./+o++``.-------.........--...........-----::::::::/::::::-:-.../++++/oydNMMMMMMMN||")
    print("||yydsmso-s--:::.ooo/:-:-.:/:---../+ooooo+/:........``........---------::::::::::::::::::+o/://+yNMMMMM||")
    print("||MNMmdhs``     -/.h+o++ymMms/-....ssmmhyyddhmhyso+/:...``.....--------------::://:::-:---:++/:/o/mMMMM||")
    print("||MMNNhmh--``` `::+d/.:sMMMMMy:-....+hmd+hdy+mNdh+++oyhys+:.........--------------::::::::--:::hmNsmMMM||")
    print("||MNNNhmN:.--...::-y:./NMMMNNMo:....`./shhdysddddddmddmmddhhy+-...............-----::::------.:mMNmdNMM||")
    print("||MNMNydy/`.-.-/::::-`+MMNhmmNd:-::-.`````.-:/-..--://++o+//:..:::://+syhhdmmmmmhs+ymmmmmdhhyoo/+ssyhmM||")
    print("||mNMmmy+++:..:hddhhh+oMMMhmNMM+::/:-..`````````````````````...:ohdhmmmmmmmmmmmmdh+ddmmdyhhhdmNdo/+symM||")
    print("||/hMNNNNNmhsy+/oyhhhyyMNNNhMmNy/://:----..``  ``   ````````./hmNNNNNNNNNNNNMNMMMNhmMMMMMNNNNNNNMyosymM||")
    print("||mNMMMMMNNNNNmdhyssyhyNMMNhmNMm+////::::---..`````````````:hNNNMMNNNNNNNNNNmNMMNNNMMMMMMMMMMMMMMNsyhmM||")
    print("||NNMMMMMMMMMMMMNmdyssymMNMMdMNM+/////oo/::--------........sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhyhmNM||")
    print("||MMMMMMMMMMMMMMMMMNmdhhNNMMmNyMy+//:/dNmNNNddyso+/::-----:/hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhhNNNmM||")
    print("||MMMMMMMMMMMMMMMMMMMMMmNmMMNNNMdo////ymmyhdhNmmmNmNmmdo/::::+shdddmmmmmmmmmmmmddddddddhhhhhhhhyyNMMmmM||")
    print("||MMMMMMMMMMMMMMMMMMMMMMMmMMNNNMms+////yNMdhhNNmmmmmmmmmh+::-//////+++++oooossssyyhhhdddmmNNNMNshNdo/mM||")
    print("||MMMMMMMMMMMMMMMMMMMMMMMMMMmMMMNdso/::--/oyhdhddmmNNNNmmy:::dMMMMMMMMMMMMMMMMMMMMMMMMNNNNmmdhyoyhhmMMM||")
    print("||MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdhhyssoo+++//////----sssssssssssssssssssssyyyhhhddmNMMMMMMMMMM||")
    print("||MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM||")
    print("||=====================================================================================================||")
    print()
    print("You look around...")
    print("Elon Musk is standing near the Tesla talking intensively on his phone, his back turned to the car.")
    print()
    print("||========================||")
    print("You weigh out your odds...")
    print()
    print("Should you, ")
    print("[A] Steal the Tesla and just drive!")
    print("[B] Leave Elon and his Tesla alone")
    print()
    steal_choice = input("Your Choice: ")

    #B
    if steal_choice.upper() == "B":
        
        bolDone = True
        bolDone = True
        bolVictory = True
        print("||=====================================================================================================||")
        print("Well, that was quite an anti-climactic game...")
        print()
        print("After",friendTwo,"gets Elon's autograph, you and your friends go to the cinema instead...")
        print()
        print("Later that night, you reflect on the boring day. Maybe stealing the Tesla was the right thing to do...")
        print()
        print("Please don't leave yet, Mr. Anderson, the actual game hasn't even started.")
        print()
        print("||=======================================================================||")
        print(" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
        print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
        print("██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
        print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
        print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
        print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
        print("||=======================================================================||")
        print()
       
    #A
    if steal_choice.upper() == "A":
        print("||=====================================================================================================||")
        print()
        print("You all jump into the Tesla, adrenaline pumping through your veins.")
        print(friendOne,"and",friendThree,"cheer and yahoo, ready for a fun day ahead. ")
        print()
        print("You enjoy the beautiful ocean view to your left as you zoom past traffic at the speed of electricity, ")
        print("when you hear the raging shouts of Elon Musk behind you...")
        print()
        print("Panicked,",friendTwo,"yells at you to pull over, but",friendThree,"tells you to keep driving.")
        print()
        print("Who do you listen to?")
        print("[A]",friendThree)
        print("[B]",friendTwo)
        print()
        friend_choice = input("Choice: ")
        print()
        print()

        #Friend 2
        if friend_choice.upper() == "B":
            
            bolDone = True
            bolVictory = True
            print("||=====================================================================================================||")
            print("You decide to listen to",friendTwo,"and pull over.")
            print("The cops give you a hefty fee of $50 each, and Elon tells you he will strap")
            print("you to one of his rockets and send you to mars if you ever try it again.")
            print()
            print("You didn't even make it to the start of the game?!?!?!")
            print("||=======================================================================||")
            print(" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
            print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
            print("██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
            print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
            print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
            print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
            print("||=======================================================================||")
            print()
            print()
            print("||=====================================================================================================||")
            



        #Friend 3
        if friend_choice.upper() == "A":
            print("---------------------------------------------------------------------")
            print("The game is on! Make it to the safehouse,",intDifficulty," miles away to WIN!")
            print("Buy upgrades for your car in order to survive.")
            print("---------------------------------------------------------------------")
            while not bolDone:
                print("||==============================================SELECT===============================================||")
                print("--------------------------------")
                print("[A] Replace the battery         |")
                print("[B] Stop to repair motor        |") 
                print("--------------------------------")
                print("[C] Drive ahead slowly          |")
                print("[D] Drive ahead normally        |")
                print("[E] Hit the (gas) at full speed.|")
                print("--------------------------------")
                print("[F] Status Check                |")
                print("[G] Shop                        |") 
                print("[H] Use nitrous tank            |")
                print("--------------------------------")
                print("[Q] Surrender                   |")
                print("--------------------------------")
                print()
                print("Current Score:",intCarMiles,"/",intDifficulty," miles.")
                print("Forecast:",intWeather)
                print("MAP: ")
                print("-------------------------------------------------------------------------------------------------------")
            #add neAGatives to thius asok hahaha
                if intCarMiles - intCopsMiles == 40:
                    print(road20)
                    
                elif intCarMiles - intCopsMiles == 39:
                    print(road20)
                elif intCarMiles - intCopsMiles == 38:
                    print(road19)
                elif intCarMiles - intCopsMiles == 37:
                    print(road19)
                elif intCarMiles - intCopsMiles == 36:
                    print(road18)
                elif intCarMiles - intCopsMiles == 35:
                    print(road18)
                elif intCarMiles - intCopsMiles == 34:
                    print(road17)
                elif intCarMiles - intCopsMiles == 33:
                    print(road17)
                elif intCarMiles - intCopsMiles == 32:
                    print(road16)
                elif intCarMiles - intCopsMiles == 31:
                    print(road16)
                elif intCarMiles - intCopsMiles == 30:
                    print(road15)
                elif intCarMiles - intCopsMiles == 29:
                    print(road15)
                elif intCarMiles - intCopsMiles == 28:
                    print(road14)
                elif intCarMiles - intCopsMiles == 27:
                    print(road14)
                elif intCarMiles - intCopsMiles == 26:
                    print(road13)
                elif intCarMiles - intCopsMiles == 25:
                    print(road13)
                elif intCarMiles - intCopsMiles == 24:
                    print(road12)
                elif intCarMiles - intCopsMiles == 23:
                    print(road12)
                elif intCarMiles - intCopsMiles == 22:
                    print(road11)
                elif intCarMiles - intCopsMiles == 21:
                    print(road11)
                elif intCarMiles - intCopsMiles == 20:
                    print(road10)
                elif intCarMiles - intCopsMiles == 19:
                    print(road10)
                elif intCarMiles - intCopsMiles == 18:
                    print(road9)
                elif intCarMiles - intCopsMiles == 17:
                    print(road9)
                elif intCarMiles - intCopsMiles == 16:
                    print(road8)
                elif intCarMiles - intCopsMiles == 15:
                    print(road8)
                elif intCarMiles - intCopsMiles == 14:
                    print(road7)
                elif intCarMiles - intCopsMiles == 13:
                    print(road7)
                elif intCarMiles - intCopsMiles == 12:
                    print(road6)
                elif intCarMiles - intCopsMiles == 11:
                    print(road6)
                elif intCarMiles - intCopsMiles == 10:
                    print(road5)
                elif intCarMiles - intCopsMiles == 9:
                    print(road5)
                elif intCarMiles - intCopsMiles == 8:
                    print(road4)
                elif intCarMiles - intCopsMiles == 7:
                    print(road4)
                elif intCarMiles - intCopsMiles == 6:
                    print(road3)
                elif intCarMiles - intCopsMiles == 5:
                    print(road3)
                elif intCarMiles - intCopsMiles == 4:
                    print(road2)
                elif intCarMiles - intCopsMiles == 3:
                    print(road2)
                elif intCarMiles - intCopsMiles == 2:
                    print(road1)
                elif intCarMiles - intCopsMiles == 1:
                    print(road1)
                elif intCarMiles - intCopsMiles == 41:
                    print(road21)
                elif intCarMiles - intCopsMiles == 42:
                    print(road21)
                elif intCarMiles - intCopsMiles == 43:
                    print(road22)
                elif intCarMiles - intCopsMiles == 44:
                    print(road22)
                elif intCarMiles - intCopsMiles == 45:
                    print(road23)
                elif intCarMiles - intCopsMiles == 46:
                    print(road23)
                elif intCarMiles - intCopsMiles == 47:
                    print(road24)
                elif intCarMiles - intCopsMiles == 48:
                    print(road24)                   
                elif intCarMiles - intCopsMiles == 49:
                    print(road25)
                elif intCarMiles - intCopsMiles == 50:
                    print(road25)
                elif intCarMiles - intCopsMiles == 51:
                    print(road51)
                elif intCarMiles - intCopsMiles == 52:
                    print(road52)
                elif intCarMiles - intCopsMiles == 53:
                    print(road53)
                elif intCarMiles - intCopsMiles == 54:
                    print(road54)
                elif intCarMiles - intCopsMiles == 55:
                    print(road55)
                elif intCarMiles - intCopsMiles == 56:
                    print(road56)
                elif intCarMiles - intCopsMiles == 57:
                    print(road57)
                elif intCarMiles - intCopsMiles == 58:
                    print(road58)
                elif intCarMiles - intCopsMiles == 59:
                    print(road59)
                elif intCarMiles - intCopsMiles == 60:
                    print(road60)
                elif intCarMiles - intCopsMiles == 61:
                    print(road61)
                elif intCarMiles - intCopsMiles == 62:
                    print(road62)
                elif intCarMiles - intCopsMiles == 63:
                    print(road63)
                elif intCarMiles - intCopsMiles == 64:
                    print(road64)
                elif intCarMiles - intCopsMiles == 65:
                    print(road65)
                elif intCarMiles - intCopsMiles == 66:
                    print(road66)
                elif intCarMiles - intCopsMiles == 67:
                    print(road67)
                elif intCarMiles - intCopsMiles == 68:
                    print(road68)
                elif intCarMiles - intCopsMiles == 69:
                    print(road69)
                elif intCarMiles - intCopsMiles == 70:
                    print(road70)
                elif intCarMiles - intCopsMiles == 71:
                    print(road71)
                elif intCarMiles - intCopsMiles == 72:
                    print(road72)
                elif intCarMiles - intCopsMiles == 73:
                    print(road73)
                elif intCarMiles - intCopsMiles >= 74:
                    print(roadxl)
                print("-------------------------------------------------------------------------------------------------------")
                print()
                user_choice = input("Your Choice: ")
                print()
                if user_choice.upper() == "Q":
                    bolDone = True


                #A - Refuel
                elif user_choice.upper() == "A":
                    if intFuel == 0:
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("The Tesla is already fully charged.")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    elif intBoot == 0:
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("There are no more batteries left.")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    else:
                        intBoot -= 1
                        intFuel = 0
                        intMotor + 1
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("The Tesla is now fully charged. This used 1 battery and weakened the motor.")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")

                #B - Repair Motor
                elif user_choice.upper() == "B":
                    if intMotor == 0:
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("The motor is in perfect condition")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    else:
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("The motor has been repaired")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        intMotor = 0
                        cops_random = random.randrange(7,20)
                        intCopsMiles += cops_random
                
                #C - Slowly
                elif user_choice.upper() == "C":
                    car_random = random.randrange(2,5)
                    intCarMiles += car_random
                    print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    print("You travelled a mere",car_random,"miles.")
                    print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    cops_random = random.randrange(7,16)
                    intCopsMiles += cops_random
                    intFuel += 1
                    motor_random = random.randrange (0,1)
                    intMotor += motor_random
                    if bolSponsors == True:
                        intMoney += 50
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("Your sponsors gave you $50.  ")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")

                #D - Moderate
                elif user_choice.upper() == "D":
                    car_random = random.randrange(5,15)
                    intCarMiles += car_random
                    print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    print("You travelled",car_random,"miles.")
                    print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    cops_random = random.randrange(7,15) 
                    intCopsMiles += cops_random
                    intFuel += 2
                    motor_random = random.randrange (1,2)
                    intMotor += motor_random
                    if bolSponsors == True:
                        intMoney += 100
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("Your sponsors gave you $100.  ")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")


                #E - Floor it. 
                elif user_choice.upper() == "E":
                    car_random = random.randrange(15,30)
                    intCarMiles += car_random
                    print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    print("You travelled a massive",car_random,"miles, but this severely affected the Tesla.")
                    print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    cops_random = random.randrange(7,14) 
                    intCopsMiles += cops_random
                    intFuel += 4
                    motor_random = random.randrange (3,6)
                    intMotor += motor_random
                    if bolSponsors == True:
                        intMoney += 150
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("Your sponsors gave you $150.  ")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")


                #F - Status Check 
                elif user_choice.upper() == "F":
                    print("||======================STATUS CHECK===========================||")
                    print("Miles Travelled: ",intCarMiles)
                    print("Miles to lighthouse: ",intDifficulty - intCarMiles,"/",intDifficulty) 
                    print("Batteries left in boot: ",intBoot)
                    print("Nitrous Tanks: ",intNitrous)
                    print("Money: $",intMoney)
                    print("-------------------------")
                    print("Current Upgrades: ")
                    print()
                    print("- Motor Level: ",intMotorLevel)
                    if bolElectroConductor == True:
                        print("- Electroconductor: [Yes] ")
                    else:
                        print("- Electroconductor: [No] ")
                    if bolHardWheels == True:
                        print("- Hard Wheels: [Yes]")
                    else:
                        print("- Hard Wheels: [No] ")
                    if bolBPShell == True:
                        print("- Bullet-Proof Chasis: [Yes]")
                    else:
                        print("- Bullet-Proof Chasis: [No] ")
                    if bolBPWindows == True:
                        print("- Bullet-Proof Windows: [Yes]")
                    else:
                        print("- Bullet-Proof Windows: [No] ")
                    if bolQuantumShield == True:
                        print("- Quantum Blanket: [Yes]")
                    else:
                        print("- Quantum Blanket: [No] ")    
                    if bolSponsors == True:
                        print("- Sponsors: [Yes]")
                    else:
                        print("- Sponsors: [No] ")
                        
                    print("-------------------------")

                #G - Shop
                elif user_choice.upper() == "G":
                    bolShopDone = False
                    while not bolShopDone:
                        print("||============================SHOP=============================||")
                        print("Pay",friendOne,"to install or remove upgrades in the Tesla.")
                        print("-------------------------- ")
                        print("CURRENT BALANCE: $",intMoney)
                        print("-------------------------- ")
                        print()
                        print("[A] Nitrous Tank: $250")
                        print("nitrous tanks can be used in order to instantly gain 20 miles. ")
                        print()
                        print("[B] Electroconductor: $250")
                        print("electroconductors convert lightning strikes into batteries during the rainstorm.")
                        print()
                        print("[C] Hard Wheels: $250")
                        print("hard wheels protect the Tesla from road spikes, ") 
                        print("however will cause the car to slide during rain.")
                        print()
                        print("[D] Bullet-Proof Chasis: $150")
                        print("a bullet-proof chasis protects the chasis from bullets.")
                        print()
                        print("[E] Bullet-Proof Windows: $150")
                        print("bullet-proof windows protect the windows from bullets.")
                        print()
                        print("[F] Sponsors: $250")
                        print("sponsers give you an amount of money each time you drive, based on how fast you drive ")
                        print()
                        print("[G] Quantum Blanket: $1000")
                        print("the quantum blanket protects your from all forms of damage and replenishes energy. ")
                        print()
                        shop_choice = input("Choice: ")
                        #A
                        if shop_choice.upper() == "A":
                            print()
                            print("[A] BUY")
                            print("[B] SELL")
                            print()
                            bos_choice = input("Choice: ")
                            if bos_choice.upper() == "A":
                                if intMoney < 250:
                                    print()
                                    print("-------------------------------------------------")
                                    print("Sorry, you not have enough money to purchase this. ")
                                    print("-------------------------------------------------")
                                    print()
                                    print("Would you like to: ")
                                    print("[A] Stay ")
                                    print("[B] Leave shop ")
                                    print()
                                    shopl_choice = input("Choice: ")
                                    if shopl_choice.upper() == "B":
                                            bolShopDone = True
                                    if shopl_choice.upper() == "A":
                                            bolShopDone = False
                                elif intMoney:
                                    print()
                                    print("------------------------------------------------")
                                    print("You have purchased a nitrous tank successfully. ")
                                    print("------------------------------------------------")
                                    intNitrous += 1
                                    intMoney -= 250
                                    print()
                                    print("Would you like to: ")
                                    print("[A] Stay ")
                                    print("[B] Leave shop ")
                                    print()
                                    shopl_choice = input("Choice: ")
                                    if shopl_choice.upper() == "B":
                                            bolShopDone = True
                                    if shopl_choice.upper() == "A":
                                            bolShopDone = False
                                
                                            
                            if bos_choice.upper() == "B":
                                if intNitrous == 0:
                                    print()
                                    print("-------------------------------------")
                                    print("Sorry, you not own any nitrous tanks.")
                                    print("-------------------------------------")
                                    print()
                                    print("Would you like to: ")
                                    print("[A] Stay ")
                                    print("[B] Leave shop ")
                                    print()
                                    shopl_choice = input("Choice: ")
                                    if shopl_choice.upper() == "B":
                                            bolShopDone = True
                                    if shopl_choice.upper() == "A":
                                            bolShopDone = False

                                if intNitrous > 0:
                                    intNitrous -= 1
                                    intMoney += 200
                                    print()
                                    print("--------------------------------")
                                    print("You sold a nitrous tank for $200")
                                    print("--------------------------------")
                                    print()
                                    print("Would you like to: ")
                                    print("[A] Stay ")
                                    print("[B] Leave shop ")
                                    print()
                                    shopl_choice = input("Choice: ")
                                    if shopl_choice.upper() == "B":
                                            bolShopDone = True
                                    if shopl_choice.upper() == "A":
                                            bolShopDone = False
                                    


                                            
                        #B
                        if shop_choice.upper() == "B":
                            print()
                            print("[A] BUY")
                            print("[B] SELL")
                            print()
                            bos_choice = input("Choice: ")
                            if bos_choice.upper() == "A":
                                if bolElectroConductor == False:
                                    if intMoney < 250:
                                        print()
                                        print("-------------------------------------------------")
                                        print("Sorry, you not have enough money to purchase this. ")
                                        print("-------------------------------------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False
                                    elif intMoney:
                                        print()
                                        print("------------------------------------------------------")
                                        print("You have purchased the electroconductor successfully. ")
                                        print("------------------------------------------------------")
                                        bolElectroConductor = True
                                        intMoney -= 250
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False
                                            
                                elif bolElectroConductor == True:
                                    print("---------------------")
                                    print("You already own this.")
                                    print("---------------------")
                                    print()
                                    print("Would you like to: ")
                                    print("[A] Stay ")
                                    print("[B] Leave shop ")
                                    print()
                                    shopl_choice = input("Choice: ")
                                    if shopl_choice.upper() == "B":
                                            bolShopDone = True
                                    if shopl_choice.upper() == "A":
                                            bolShopDone = False
                                            
                            if bos_choice.upper() == "B":
                                if bolElectroConductor == False:
                                    print()
                                    print("----------------------------------------")
                                    print("Sorry, you not own the electroconductor.")
                                    print("----------------------------------------")
                                    print()
                                    print("Would you like to: ")
                                    print("[A] Stay ")
                                    print("[B] Leave shop ")
                                    print()
                                    shopl_choice = input("Choice: ")
                                    if shopl_choice.upper() == "B":
                                            bolShopDone = True
                                    if shopl_choice.upper() == "A":
                                            bolShopDone = False

                                if bolElectroConductor == True:
                                    bolElectroConductor = False
                                    intMoney += 200
                                    print()
                                    print("--------------------------------------")
                                    print("You sold the electroconductor for $200")
                                    print("--------------------------------------")
                                    print()
                                    print("Would you like to: ")
                                    print("[A] Stay ")
                                    print("[B] Leave shop ")
                                    print()
                                    shopl_choice = input("Choice: ")
                                    if shopl_choice.upper() == "B":
                                            bolShopDone = True
                                    if shopl_choice.upper() == "A":
                                            bolShopDone = False
                        #C
                        if shop_choice.upper() == "C":
                                print()
                                print("[A] BUY")
                                print("[B] SELL")
                                print()
                                bos_choice = input("Choice: ")
                                if bos_choice.upper() == "A":
                                    if bolHardWheels == False:
                                        if intMoney < 250:
                                            print()
                                            print("-------------------------------------------------")
                                            print("Sorry, you not have enough money to purchase this. ")
                                            print("-------------------------------------------------")
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ")
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False
                                        elif intMoney:
                                            print()
                                            print("---------------------------------------------")
                                            print("You have purchased hard wheels successfully. ")
                                            print("---------------------------------------------")
                                            bolHardWheels = True
                                            intMoney -= 250
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ")
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False

                                    elif bolHardWheels == True:
                                        print("---------------------")
                                        print("You already own this.")
                                        print("---------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False
                                                    
                                if bos_choice.upper() == "B":
                                    if bolHardWheels == False:
                                        print()
                                        print("-------------------------------")
                                        print("Sorry, you not own hard wheels.")
                                        print("-------------------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False

                                    if bolHardWheels == True:
                                        bolHardWheels = False
                                        intMoney += 200
                                        print()
                                        print("----------------------------------")
                                        print("You sold your hard wheels for $200")
                                        print("----------------------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False
                                                
                        #D
                        if shop_choice.upper() == "D":
                                print()
                                print("[A] BUY")
                                print("[B] SELL")
                                print()
                                bos_choice = input("Choice: ")
                                if bos_choice.upper() == "A":
                                    if bolBPShell == False:
                                        if intMoney < 150:
                                            print()
                                            print("-------------------------------------------------")
                                            print("Sorry, you not have enough money to purchase this. ")
                                            print("-------------------------------------------------")
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ")
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False
                                        elif intMoney:
                                            print()
                                            print("---------------------------------------------------------")
                                            print("You have purchased a bullet-proofed chasis successfully. ")
                                            print("---------------------------------------------------------")
                                            bolBPShell = True
                                            intMoney -= 150
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ")
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False

                                    elif bolBPChasis == True:
                                        print("---------------------")
                                        print("You already own this.")
                                        print("---------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False
                                                
                                if bos_choice.upper() == "B":
                                    if bolBPShell == False:
                                        print()
                                        print("-----------------------------------------")
                                        print("Sorry, you not own a bullet-proof chasis.")
                                        print("-----------------------------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False

                                    if bolBPShell == True:
                                        bolBPShell = False
                                        intMoney += 100
                                        print()
                                        print("------------------------------------------")
                                        print("You sold your bullet-proof chasis for $100")
                                        print("------------------------------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False

                        #E
                        if shop_choice.upper() == "E": 
                                print()
                                print("[A] BUY")
                                print("[B] SELL")
                                print()
                                bos_choice = input("Choice: ")
                                if bos_choice.upper() == "A":
                                    if bolBPWindows == False:
                                        if intMoney < 150:
                                            print()
                                            print("---------------------------------------------------")
                                            print("Sorry, you not have enough money to purchase this. ")
                                            print("---------------------------------------------------")
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ")
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False
                                        elif intMoney:
                                            print()
                                            print("--------------------------------------------------------")
                                            print("You have purchased bullet-proofed windows successfully. ")
                                            print("--------------------------------------------------------")
                                            bolBPWindows = True
                                            intMoney -= 150
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ")
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False

                                    elif bolBPWindows == True:
                                        print("---------------------")
                                        print("You already own this.")
                                        print("---------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False
                                                
                                if bos_choice.upper() == "B":
                                    if bolBPWindows == False:
                                        print()
                                        print("----------------------------------------")
                                        print("Sorry, you not own bullet-proof windows.")
                                        print("----------------------------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False

                                    if bolBPWindows == True:
                                        bolBPWindows = False
                                        intMoney += 100
                                        print()
                                        print("-------------------------------------------")
                                        print("You sold your bullet-proof windows for $100")
                                        print("-------------------------------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False

                        #F
                        if shop_choice.upper() == "F":
                                print()
                                print("[A] BUY")
                                print("[B] SELL")
                                print()
                                bos_choice = input("Choice: ")
                                if bos_choice.upper() == "A":
                                    if bolSponsors == False:
                                        if intMoney < 250:
                                            print()
                                            print("---------------------------------------------------")
                                            print("Sorry, you not have enough money to purchase this. ")
                                            print("---------------------------------------------------")
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ")
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False
                                        elif intMoney:
                                            print()
                                            print("------------------------------------------")
                                            print("You have purchased sponsors successfully. ")
                                            print("------------------------------------------")
                                            bolSponsors = True
                                            intMoney -= 250
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ")
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False
                                    elif bolSponsors == True:
                                        print("---------------------")
                                        print("You already own this.")
                                        print("---------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False
                                                
                                if bos_choice.upper() == "B":
                                    if bolSponsors == False:
                                        print()
                                        print("----------------------------")
                                        print("Sorry, you not own sponsors.")
                                        print("----------------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False

                                    if bolSponsors == True:
                                        bolSponsors = False
                                        intMoney += 200
                                        print()
                                        print("-------------------------------")
                                        print("You sold your sponsors for $200")
                                        print("-------------------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False


                                
                        #G 
                        if shop_choice.upper() == "G":
                                print()
                                print("[A] BUY")
                                print("[B] SELL")
                                print()
                                bos_choice = input("Choice: ")
                                if bos_choice.upper() == "A":
                                    if bolQuantumShield == False:
                                        if intMoney < 1000:
                                            print()
                                            print("-------------------------------------------------")
                                            print("Sorry, you not have enough money to purchase this. ")
                                            print("-------------------------------------------------")
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ")
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False
                                        elif intMoney:
                                            print()
                                            print("---------------------------------------------------")
                                            print("You have purchased a quantum blanket successfully. ")
                                            print("---------------------------------------------------")
                                            bolQuantumShield = True
                                            intMoney -= 1000
                                            print()
                                            print("Would you like to: ")
                                            print("[A] Stay ")
                                            print("[B] Leave shop ")
                                            print()
                                            shopl_choice = input("Choice: ") 
                                            if shopl_choice.upper() == "B":
                                                    bolShopDone = True
                                            if shopl_choice.upper() == "A":
                                                    bolShopDone = False

                                    elif bolQuantumShield == True:
                                        print("---------------------")
                                        print("You already own this.")
                                        print("---------------------")
                                        print()
                                        print("Would you like to: ")
                                        print("[A] Stay ")
                                        print("[B] Leave shop ")
                                        print()
                                        shopl_choice = input("Choice: ")
                                        if shopl_choice.upper() == "B":
                                                bolShopDone = True
                                        if shopl_choice.upper() == "A":
                                                bolShopDone = False
                                                    
                                if bos_choice.upper() == "B":
                                    print("----------------------------------------------------------------------------")
                                    print("Sorry, you cannot sell quantum shields, just like you cannot uncook an egg. ")
                                    print("----------------------------------------------------------------------------")
                                    print()
                                    print("Would you like to: ")
                                    print("[A] Stay ")
                                    print("[B] Leave shop ")
                                    print()
                                    shopl_choice = input("Choice: ")
                                    if shopl_choice.upper() == "B":
                                            bolShopDone = True
                                    if shopl_choice.upper() == "A":
                                            bolShopDone = False
                            
                     
                    

                #H - Use Nitrous Tank
                elif user_choice.upper() == "H":
                    if intNitrous == 0:
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print(" You have no more nitrous tanks")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    else:
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print(" You used nitrous and went 20 miles, but this had it's toll on the motor.")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        intNitrous -= 1
                        intCarMiles += 20
                        nitrous_random = random.randrange (2,4)
                        intMotor += nitrous_random
                        intNitrousUsed += 1
                        nitrouscops_random = random.randrange(1,7)
                        intCopsMiles += nitrouscops_random


                    

                #Game Engine

#Victory
                if not bolDone:
                    if intCarMiles >= intDifficulty:
                        bolDone = True
                        bolVictory = True
                        print("||======================================================================================================||")
                        print("██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗ ██╗ ")
                        print("██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝ ██║ ")
                        print("██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝  ██║ ")
                        print("╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝   ╚═╝ ")
                        print(" ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║    ██╗ ")
                        print("  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═╝ ")
                        print("||======================================================================================================||")
                        print("You made it to the safehouse,",intDifficulty,"miles away! ")
                        print()
                        print(friendOne,"stumbles out of the Tesla, and immediately regurgitates.")
                        print(friendTwo,"leaps out of the car and does a victory dance.")
                        print(friendThree,"cheers and yahoos. ")
                        print()
                        print("Thanks for playing Mr Anderson! ")
                        print()
                        print("Would you like to play again? ")
                        print("[A] Yeah! ")
                        print("[Q] Nah ")
                        print()
                        replay_choice = input("Your choice: ")
                        if replay_choice.upper() == "A":
                            bolDone = False
                            bolEmpty = False 
                            intBoot = 5
                            intFuel = 0 
                            intCarMiles = 0
                            intCopsMiles = -20
                            intMotor = 0 
                            intNitrousUsed = 0
                            intNitrous = 3
                            intMoney = 500
                            intMotorLevel = 1
                            intWeather = "Sunny"
                            bolElectroConductor = False 
                            bolHardWheels = False 
                            bolBPShell = False
                            bolBPWindows = False 
                            bolSponsors = False 
                            bolQuantumShield = False 
                            bolShopDone = False
                            bolVictory = False
                            print("---------------------------------------------------------------------")
                            print("The game is on! Make it to the safehouse,",intDifficulty," miles away to WIN!")
                            print("Buy upgrades for your car in order to survive.")
                            print("---------------------------------------------------------------------")


                                

                if not bolDone:
                    if intCarMiles - intCopsMiles <= 0:
                        bolDone = True
                        print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                        print("Elon caught up to you, despite the Tesla being one of the fastest cars in the world. ")
                        print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")

                if not bolDone:
                    if intMotor > 12:
                        bolDone = True
                        print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                        print("The motor overheated and exploded, leaving you and the Tesla stuck in the ")
                        print("middle of the street. ")
                        print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")

                if not bolDone:
                    if intFuel > 10:
                        bolDone = True
                        print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                        print("Your Tesla ran out of power, the useless thing. ")                        
                        print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")

                if not bolDone:

                    if intCarMiles - intCopsMiles <= 15:
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("Elon is nearing you, you might want to pick up some speed. ")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    if  intMotor > 8:
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("The motor is beginning to overheat, you may want to slow down and repair it.")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                    if intFuel > 6: 
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        print("The Tesla is running out of power. You may want to replace the battery. ")
                        print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")

#Random Stuff

                if not bolDone:
                    if intCarMiles - intCopsMiles < 14:
                        shoot_random = random.randrange (1,4)
                        if shoot_random == 2:
                            #Chasis Shot 
                            if bolBPShell == True:
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                print("Elon got close enough to shoot at your chasis, but luckily it was bullet-proofed. ")
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            if bolQuantumShield == True:
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                print("Elon got close enough to shoot at your chasis, but the quantum blanket absorbed the kinetic energy,   ")
                                print("and converted it to battery energy. ")
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                intBoot += 1
                            if bolBPShell == False:
                                bolDone = True 
                                print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                                print("Elon got close enough to shoot at your chasis, and the Tesla went up in flames. You should of     ")
                                print("bought a bulletproof chasis from the shop.      ")
                                print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        if intWeather == "Rain":
                            if bolHardWheels == True:
                                rainslide_random = random.randrange (1,2)
                                if rainslide_random == 2:
                                    print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                                    print("Your hard wheels caused the Tesla to slide all around the road. You hit a brick wall and your joyride comes")
                                    print("to a disappointing end. ")
                                    print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                            elif bolHardWheels == False:
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                print("In the rain, the Tesla loses grip and begins sliding around the road. Luckily, you manage to regain traction, ")
                                print("and the tar on the road combined with the friction from the tires causes a hard shell to form around the    ")
                                print("wheels. You are now immune to road spikes, however you may want to sell the hard wheels before the next rainy     ")
                                print("day, or else you will have no traction. ")
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                bolHardWheels = True                            
                                                                                                                                            

                if not bolDone:
                    if intCarMiles - intCopsMiles < 10:
                        spikes_random = random.randrange (1,4)
                        if spikes_random == 2:
                            #Spikes
                            if bolHardWheels == True:
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                print("Elon planted holgraphic road spikes ahead of you, but luckily ")
                                print("you had hard wheels equiped, so you rolled right over them. ")
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            elif bolQuantumShield == True: 
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                print("Elon planted holgraphic road spikes ahead of you, but luckily ")
                                print("you had the quantum blanket, so you rolled right over them. ")
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                intBoot += 1
                            elif bolHardWheels == False:
                                bolDone = True 
                                print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                                print("Elon planted holgraphic road spikes ahead of you, and when you hit the spikes ")
                                print("the wheels exploded, sending you flying around the road.  ")
                                print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")       

                if not bolDone:
                    if intCarMiles - intCopsMiles < 14:
                        shoot_random = random.randrange (1,4)
                        if shoot_random == 2:
                            #Window Shot 
                            if bolBPWindows == True:
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                print("Elon got close enough to shoot at your back window, but luckily it was bulletproofed. ")
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            elif bolQuantumShield == True:
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                print("Elon got close enough to shoot at your back window, but the quantum blanket absorbed the kinetic energy. ")
                                print("and converted it to battery energy. ")
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                intBoot += 1
                            elif bolBPWindows == False:
                                bolDone = True 
                                print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                                print("Elon got close enough to shoot at your back window, ")
                                print("and the Tesla went up in flames. You should of   ")
                                print("bought a bulletproof windows from the shop.      ")
                                print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")


                #Cheers & woos
                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        cheers_random = random.randrange (0,11)
                        if cheers_random == 1:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print(friendOne,"cheers and wees.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        elif cheers_random == 2:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print(friendTwo,"cheers in excitement.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        elif cheers_random == 3:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print(friendThree,"pees their pants in excitement.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        elif cheers_random == 4:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print(friendTwo,"cheers and wees.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        elif cheers_random == 5:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print(friendThree,"cheers in excitement.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        elif cheers_random == 6:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print(friendOne,"pees their pants in excitement.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        elif cheers_random == 7:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("When you accelerate,",friendOne,"chokes on their food.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        elif cheers_random == 8:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("When you accelerate,",friendTwo,"chokes on their water.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        elif cheers_random == 9:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("When you accelerate,",friendThree,"chokes on their food.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                        elif cheers_random == 10:
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("When you accelerate,",friendThree,"chokes on their water.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")



                                
                        
                #Encounters 
                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        supercharge_random = random.randrange (0,8)
                        if supercharge_random == 5: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("The motor accidently hypercharged. Electricity cycled back  ") 
                            print("through the battery. The Tesla is now fully charged.        ")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            intFuel = 0
                            
                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        distraction_random = random.randrange (0,7)
                        if distraction_random == 3: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("Elon got distracted by a rocket passing by...  ") 
                            print("He stopped while you gained 5 miles.        ")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            intCopsMiles -= 5

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        invention_random = random.randrange (0,10)
                        if invention_random == 3: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("Elon accidentally started a million dollar business...  ") 
                            print("He stopped while you gained 10 miles.        ")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            intCopsMiles -= 10

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        lasergun_random = random.randrange (0,8)
                        if intNitrous > 0: 
                            if lasergun_random == 3: 
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                print("Elon shot at you with his super-secret-long-distance laser gun.  ") 
                                print("The laser penetrated and destroyed one of your nitrous tanks and burnt",friendOne,"'s butt.        ")
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                intNitrous -= 1

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        facebook_random = random.randrange (0,5)
                        if facebook_random == 4: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("A Facebook post of your joyride went viral. You got $150 in ad revenue. ")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            intMoney += 150

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        hcompartment_random = random.randrange (0,12)
                        if hcompartment_random == 7: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("You found a hidden compartment in the Tesla, underneath the back left seat.  ")
                            print("in it were 2 spare batteries and $50 cash. ")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            intMoney += 50
                            intBoot += 2

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        bananapeel_random = random.randrange (0,8)
                        if bananapeel_random == 7: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("The cops slipped on a banana peel that",friendOne,"threw out the window.")
                            print("They were set back 5 miles.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            intCopsMiles -= 5

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        seagull_random = random.randrange (0,10)
                        if seagull_random == 9: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("A seagull pooped in your motor, damaging it.")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            intMotor += 1

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        funnycatvideo_random = random.randrange (0,10)
                        if funnycatvideo_random == 7: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("A funny cat video popped up on the screen of the Tesla. You stopped to watch it, and Elon gained 8 miles. ")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")                                               
                            intCopsMiles += 8
                            
                if not bolDone:
                    if user_choice.upper() == "B": 
                        motorfix_random = random.randrange (0,3)
                        if motorfix_random == 1: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("While fixing the motor,",friendThree,"dislodged the supercharger, again.")
                            print("The Tesla malfunctioned and the wheels started spinning backwards.")
                            print("You went back 1 mile. ")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")                                               
                            intCarMiles -= 1

                if not bolDone:
                    if bolEmpty == False:
                        if user_choice.upper() == "A":
                                bolEmpty = True
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                print("However, while getting the battery from the boot, you found a supply pack containing...")
                                print("Nothing! Bad luck. ")
                                print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")                                               
                     

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        bunker_random = random.randrange (0,6)
                        if bunker_random == 1: 
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                            print("You found someone's post-apocolyptic bunker. You and your friends rested, ate, and played Uno, ")
                            print("and then",friendTwo,"replenished and repaired the Tesla to it's former glory")
                            print("using the bunker's supplys. ")
                            print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")                                               
                            intFuel = 0
                            intMotor = 0
                            intBoot += 1

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        if intWeather == "Rainstorm":
                            thunderstruck_random = random.randrange (1,3)
                            if thunderstruck_random == 2:                                   
                                if bolElectroConductor == True:
                                    print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                    print("In the rainstorm, the Tesla was struck by lightning, however your electroconductor absorbed the energy ")
                                    print("from the bolt and converted it to battery energy for the car. Good buy! ")
                                    print("||::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::||")
                                elif bolElectroConductor == False:
                                    print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                                    print("In the rainstorm, the Tesla was struck by a bolt of lightning, and the steel frame absorbed all of the  ")
                                    print("energy, short-cicuiting the whole car and giving you and your friends the shock of your lives. ")
                                    print("You could of avoided this by buying an electroconductor from the shop.  ")
                                    print("||xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||")
                                    bolDone = True
                                    
                            
                if not bolDone:
                    if user_choice.upper() == "A" or user_choice.upper() == "B" or user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E" or user_choice.upper() == "H":
                        weather_random = random.randrange (1,4)
                        if weather_random == 1:
                            intWeather = "Sunny"
                        elif weather_random == 2:
                            intWeather = "Rainstorm"
                        elif weather_random == 3:
                            intWeather = "Windy"
                        elif weather_random == 4:
                            intWeather = "Rain"

                if not bolDone:
                    if user_choice.upper() == "C" or user_choice.upper() == "D" or user_choice.upper() == "E":
                        lottery_random = random.randrange (1,9)
                        if lottery_random == 5:
                            print()
                            print(".------..------..------..------..------..------..------. ") 
                            print("|L.--. ||O.--. ||T.--. ||T.--. ||E.--. ||R.--. ||Y.--. | ") 
                            print("| :/\: || :/\: || :/\: || :/\: || (\/) || :(): || (\/) | ") 
                            print("| (__) || :\/: || (__) || (__) || :\/: || ()() || :\/: | ") 
                            print("| '--'L|| '--'O|| '--'T|| '--'T|| '--'E|| '--'R|| '--'Y| ") 
                            print("`------'`------'`------'`------'`------'`------'`------' ")
                            print("Welcome to the lottery, you have been randomly selected. ")
                            print()
                            print("Enter for a chance to win: ")
                            print("- Money ")
                            print("- Upgrades ")
                            print("- Nitrous ")
                            print("- Batteries ")
                            print()
                            print("Tickets: $100 ")
                            print("[A] Buy ")
                            print("[B] No Thanks ")
                            lottery_choice = input("Choice: ")
                            if lottery_choice.upper() == "A":
                                intMoney -= 100
                                level_random = random.randrange (1,6)
                                if level_random == 1:
                                    print()
                                    print("||++++++++++++++++++++++||")
                                    print("You won... ")
                                    print()
                                    print("- 1x Nitrous Tank") 
                                    print("- $25")
                                    print("- Hard Wheels")
                                    print("||++++++++++++++++++++++||")
                                    intNitrous += 1
                                    intMoney += 25
                                    bolHardWheels = True

                                elif level_random == 2:
                                    print()
                                    print("||++++++++++++++++++++++||")
                                    print("You won... ")
                                    print()
                                    print("- 2x Nitrous Tank") 
                                    print("- 1x Battery")
                                    print("- Bullet Proof Windows")
                                    print("- $25")
                                    print("||++++++++++++++++++++++||")
                                    intNitrous += 2
                                    intMoney += 25
                                    bolBPWindows = True
                                    intBoot += 1

                                elif level_random == 3:
                                    print()
                                    print("||++++++++++++++++++++++|| ")
                                    print("You won... ")
                                    print()
                                    print("- Quantum Blanket ")
                                    print("- $50 ")
                                    print("||++++++++++++++++++++++|| ")
                                    bolQuantumShield = True
                                    intMoney += 50

                                elif level_random >= 4:
                                    print()
                                    print("||++++++++++++++++++++++++++++|| ")
                                    print("Sorry, you didn't win anything. ")
                                    print("||++++++++++++++++++++++++++++|| ")
                                


    #Quit
    if bolVictory == False and bolDone == True: 
        print("||======================================================================================================||")
        print()
        print(" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
        print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
        print("██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
        print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
        print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
        print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
        print()
        print("You and",friendOne,",",friendTwo,",",friendThree,"made it,",intCarMiles,"miles before being caught by Elon. ")
        print("He says he will tie you to a rocket and send you to mars if you ever do it again. ")
        print("You each get fined $50 by the cops, but luckily they release you. You walk off.. maybe you'll find another Tesla.")
        print()
        print("-------------------------------------------------- ")
        print("GAME STATISTICS: ")
        print()
        print("Miles to lighthouse: ",intDifficulty - intCarMiles,"/",intDifficulty) 
        print("Batteries left in boot: ",intBoot)
        print("Nitrous Tanks Left: ",intNitrous)
        print("Nitrous Tanks Used: ",intNitrousUsed)
        print("Money Left: $",intMoney)
        print("Upgrades: ")
        print()
        print("- Motor Level: ",intMotorLevel)
        if bolElectroConductor == True:
            print("- Electroconductor: [Yes] ")
        else:
            print("- Electroconductor: [No] ")
        if bolHardWheels == True:
            print("- Hard Wheels: [Yes]")
        else:
            print("- Hard Wheels: [No] ")
        if bolBPShell == True:
            print("- Bullet-Proof Chasis: [Yes]")
        else:
            print("- Bullet-Proof Chasis: [No] ")
        if bolBPWindows == True:
            print("- Bullet-Proof Windows: [Yes]")
        else:
            print("- Bullet-Proof Windows: [No] ")
        if bolQuantumShield == True:
            print("- Quantum Blanket: [Yes]")
        else:
            print("- Quantum Blanket: [No] ")    
        if bolSponsors == True:
            print("- Sponsors: [Yes]")
        else:
            print("- Sponsors: [No] ")
        print()
        print("---------------------------------------------------------------- ")
        print("Thanks for playing Mr. Anderson, hope you enjoyed! ")
        print("Also, sorry if you lost easily, it's meant to be a fast-paced game. ")
        print("---------------------------------------------------------------- ")
        print()
        print("Would you like to play again? ")
        print("[A] Yeah! ")
        print("[Q] Nah ")
        print()
        replay_choice = input("Your choice: ")
        if replay_choice.upper() == "A":
            bolDone = False
            bolEmpty = False 
            intBoot = 5
            intFuel = 0 
            intCarMiles = 0
            intCopsMiles = -20
            intMotor = 0 
            intNitrousUsed = 0
            intNitrous = 3
            intMoney = 500
            intMotorLevel = 1
            intWeather = "Sunny"
            bolElectroConductor = False 
            bolHardWheels = False 
            bolBPShell = False
            bolBPWindows = False 
            bolSponsors = False 
            bolQuantumShield = False 
            bolShopDone = False
            bolVictory = False
            print("---------------------------------------------------------------------")
            print("The game is on! Make it to the safehouse,",intDifficulty," miles away to WIN!")
            print("Buy upgrades for your car in order to survive.")
            print("---------------------------------------------------------------------")

        else:
            print()
            print("Thanks for playing Mr. Anderson ")
            print()
            
        print("||======================================================================================================||")
