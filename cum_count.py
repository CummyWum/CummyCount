import time, sys, os
import datetime
import json
from random import randint
#from playsound import playsound

user = "Ofi"
intro = False
def save(file, thing):
    with open(file, "w") as f:
        json.dump(thing, f)

if intro:
    dialogue = {
        "intro": ["Welcome {}, you god damned degenerate!".format(user), "test", "HolyShit"],
        "introTime": [2.7, 1.5, 1],
        "prev": None,
        "dialgoue": []
    }

    #save("dialogue.json", dialogue)

    with open("dialogue.json", "r") as f:
        dialogue = json.load(f)

    while True:
        os.system("clear")
        introSelect = randint(0, len(dialogue["intro"]) - 1)
        
        if dialogue["intro"][introSelect] == dialogue["prev"]:
            continue
        
        else:
            print(dialogue["intro"][introSelect])
            dialogue["prev"] = dialogue["intro"][introSelect]
            time.sleep(dialogue["introTime"][introSelect])
            save("dialogue.json", dialogue)
            break
else:
    pass

counts = {
    "cum": 0
}

entries = {
    "Number of entries": 0
}

tally = {
    "tallies": 1
}


col = "\033[1;31;40m"


with open("counting.json", "r") as f:
    counts = json.load(f)
with open("entries.json", "r") as f:
    entries = json.load(f)



while True:
    os.system("clear")
    bruh = []
    print("Number of times COOMed: {}{}".format(col, counts["cum"]))

    try:
        print("\n\033[0;32;40m\"h\" \033[0;37;40mfor more functions/features")
        plus = input("\n\033[0;37;40mType \033[0;31;40m\"entries\" \033[0;37;40mto see entries or:\n\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto add,\n\033[0;35;40m\"r\" \033[0;37;40mto reset counter or \033[1;31;40m\"q\" \033[0;37;40mto quit: ").strip()
        
        if plus.casefold() == "":
            counts["cum"] += 1
            #playsound("sound/nut.mp3", block=False)
            continue

        if plus.casefold() == "-":
            if counts["cum"] - 1 < 0:
                counts["cum"] == 0
                continue

            else:
                counts["cum"] -= 1
                #playsound("sound/un_nut.mp3", block=False)
                continue

        if plus.casefold() == "q":
            save("counting.json", counts)
            save("entries.json", entries)
            os.system("clear")
            sys.exit()

        if plus.casefold() == "r":
            contin = input("\nAre you SURE you want to \033[0;35;40mreset \033[0;37;40mthe counter?(\033[1;32;40my\033[0;37;40m/\033[1;31;40mn\033[0;37;40m)?: ")
            if contin.casefold() == "y":
                entries["Number of entries"] += 1
                entries["entry_{}".format(entries["Number of entries"])] = counts["cum"]
                counts["cum"] = 0
                continue
            
            else:
                continue


        if plus.casefold() == "entries":
            os.system("clear")
            for thing in entries:
                if thing == "Number of entries":
                    pass
                else:
                    bruh.append(entries[thing])
            
            print("Total times \033[0;31;40morgasmed: \033[1;31;40m{}".format(sum(bruh) + counts["cum"]))
            for thing in entries:
                print("\033[0;37;40m" + thing + ": \033[1;31;40m{}".format(entries[thing]))
            #print("\n" + str(bruh))

            contin = input("\n\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue or:\ntype \033[1;36;40m\"most\" \033[0;37;40mfor the most times COOMed\n\nYou can also \033[1;32;40mvisualize \033[0;37;40mhow many times you've\nCOOMed + fun facts with \033[1;32;40m\"v\"\033[0;37;40m!: ").strip()
            
            if contin.casefold() == "":
                continue

            if contin.casefold() == "most":
                try:
                    least = min(bruh)
                    most = max(bruh)

                    os.system("clear")
                    print("Times you've cum the least: \033[1;32;40m{}".format(least))
                    print("\033[0;37;40mTimes you've cum the most:  \033[1;31;40m{}".format(most))
                    time.sleep(2)
                    print("\n(You dirty bastard, what the fuck?)")
                    time.sleep(1)
                    contin = input("\033[0;37;40mPress \"Enter\" to continue: ")
                    continue
                except ValueError:
                    print("\n\033[1;31;40mNo entries found")
                    time.sleep(1)
                    continue
            
            if contin.casefold() == "v":
                total = sum(bruh) + counts["cum"]
                coomEye = ""
                for i in range(total):
                    coomEye = coomEye + "I"

                os.system("clear")
                
                tally["tallies"] = 1
                tally["tally_1"] = ""
                for i in range(len(coomEye)):
                    tally["tally_{}".format(tally["tallies"])] = tally["tally_{}".format(tally["tallies"])] + "I"
                    if total <= 10:
                        divisor = 5
                    else:
                        divisor = 15

                    if len(tally["tally_{}".format(tally["tallies"])]) == divisor:
                        tally["tallies"] += 1
                        tally["tally_{}".format(tally["tallies"])] = ""
                        continue
                    
                    else:
                        continue

                try:
                    numDel = 1
                    while True:
                        print("\033[1;32;40m" + tally["tally_{}".format(numDel)])
                        del tally["tally_{}".format(numDel)]
                        numDel += 1
                        continue
                except:
                    pass
                
                print("\033[0;37;40m(\033[0;31;40m{} \033[0;37;40mtimes)".format(total))

                time.sleep(1)

                fluid = total * 1.5
                print("\n1 \033[0;31;40mejaculation \033[0;37;40m= ~1.5ml+")
                print("You've released around:\n\033[0;31;40m{} \033[0;37;40mml of degenerate juices, what the fuck.".format(fluid))
		
                time.sleep(1)

                time_spent = total * 2
                print("\n\033[1;36;40mIf you're a man,\nyou've spent at LEAST \033[0;31;40m{} \033[1;36;40mminutes or more\ndoing your thing.".format(time_spent))
                time_spent = total * 13.45
                print("\n\033[1;35;40mIf you're a woman,\nyou've spent at LEAST \033[0;31;40m{} \033[1;35;40mminutes or more\ndoing your thing.".format(round(time_spent, 2)))
                contin = input("\n\033[0;37;40mPress \033[1;33;40m\"Enter\"\033[0;37;40m to continue: ")
                continue

            else:
                print("\n\033[1;31;40mInvalid input, please try again.\033[0;37;40m")
                time.sleep(1.5)
                continue



        if plus.casefold() == "edit":
            os.system("nano cum_count.py")
            os.system("clear")
            os.execl(sys.executable, sys.executable, *sys.argv)

        if plus.casefold() == "re":
            chooser = randint (1, 3)
            if chooser == 4:
                print("\n\033[1;31;40mFucking your mom...\033[0;37;40m")
                time.sleep(2)
            else:
                print("\n\033[1;35;40mRestarting...\033[0;37;40m")
                time.sleep(0.5)
            os.execl(sys.executable, sys.executable, *sys.argv)

        if plus.casefold() == "s":
            chooser = randint(1, 7)

            if chooser == 1:
                print("\n\033[1;31;40mStealing YO BITCH...\033[0;37;40m")
                time.sleep(0.2)
            
            elif chooser == 5:
                print("\n\033[1;31;40mStealing your data...\033[0;37;40m")
                time.sleep(0.2)

            else:
                print("\n\033[1;33;40mSaving...\033[0;37;40m")
                time.sleep(0.2)

            save("counting.json", counts)
            save("entries.json", entries)
            #playsound("sound/save.mp3")
            continue

        if plus.casefold() == "qws":
            os.system("clear")
            sys.exit()

        if plus.casefold() == "h":
            
            # Entries   √
            # Reset     √
            # Visualize √
            # Restart   √
            # Saving    x
            # QWS       √

            os.system("clear")
            print("""\033[0;31;40mEntries: 
    \033[0;37;40mUsage: \033[0;31;40mentries
    \033[0;37;40mAn entry is just that: a log of your COOMs!
    Creating an entry is explained
    in the next function.

\033[0;35;40mResetting:
    \033[0;37;40mUsage: \033[0;35;40mr
    \033[0;37;40mRestting of course resets the counter, BUT:
    it also creates an entry!

\033[1;32;40mVisualization:
    \033[0;37;40mUsage: \033[1;32;40mv
    \033[0;37;40mAs of CumNutter v1.2.0, the visualizer:
        -Shows you a tally of your COOMs
        -Calculates approx. COOM produced
        -Calculates time spent COOMing

\033[1;33;40mSaving w/o Quitting:
    \033[0;37;40mUsage: \033[1;33;40ms
    \033[0;37;40mSaves counts and entries without quitting.

\033[0;32;40mSubtracting:
    \033[0;37;40mUsage: \033[0;32;40m-
    \033[0;37;40mSubtracts 1 from COOM counter.

\033[1;35;40mRestart:
    \033[0;37;40mUsage: \033[1;35;40mre
    \033[0;37;40mRestarts program,
    does not save before restarting.

\033[1;31;40mQuit Without Saving:
    \033[0;37;40mUsage: \033[1;31;40mqws
    \033[0;37;40mQuits without saving counter.
""")
            print("(Scroll up to see full list)")
            contin = input("Press \033[1;33;40m\"Enter\" \033[0;37;40mto continue: ")
            continue

        else:
            print("\n\033[1;31;40mInvalid input, please try again.\033[0;37;40m")
            time.sleep(1.5)
            continue

    except KeyboardInterrupt:
        save("counting.json", counts)
        save("entries.json", entries)
        os.system("clear")
        sys.exit()
