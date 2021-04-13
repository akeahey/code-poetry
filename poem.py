# 0: TODAY
sunrise = 1
whereami = "here"
beaboutit = ""
wins = 0
losses = 56
affirmatives = ["yep", 
                "okay", 
                "sure", 
                "fine", 
                "yeah", 
                "okay but I'm gonna be mad about it the whole time", 
                "fine but only if I pick the music", 
                "if I have to", 
                "sure whatever",
                "for sure!",
                "nothing better to do",
                "yeah but only out of spite", 
                "that's gravy", 
                "Hot Dog",
                "ten four",
                "alright"]

# 1: TOMORROW 
def today (dubs, els, thathardshit):
    global sunrise, beaboutit

    if dubs > 0:
        sunrise = 1
    else:
        sunrise = 1

    if els == 0:
        sunrise = 1
    else:
        sunrise = 1

    # TODO: !!
    # make changes
    if thathardshit in affirmatives:
        beaboutit = "i am"

# 2: THOSE DAYS AFTER THAT
today(wins, losses, "sure whatever")

if sunrise == 1:

    print("                | ")
    print("             \  '  / ")
    print("               .-. ")
    print("         -=== (   ) ===-")
    print("               '-' ")
    print("             /  .  \ ")
    print("                |")
    print("   ^~^^~^~^=^=^~=~=~^=^~^~^~^~^~^~^~^~^")
    print("     ~^~  ~^= =~^=~^~^= ~^~^~  ~^~^ ~^~")
    print("   ~^ ~^~  ~^==~^==~^~ = ~^=~ ~^  ~^~")
    print("   .' ..'..''.'.'.  '.'..'.'  .'''..''.'")

    if whereami == "here":
        if beaboutit == "i am":

            print("    ''. ~O     ''       ''")
            print("        /|\ '   .     '     .    '")
            print("    .   /|          .    .      '")
            print("       / |  .               .")
            print("       ` `        '             '")
            wins = 1






        
   