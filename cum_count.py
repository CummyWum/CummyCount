import time, sys, os
import datetime
import json

def save(file, thing):
    with open(file, "w") as f:
        json.dump(thing, f)

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

            contin = input("\n\033[0;37;40mPress \033[1;33;40m\"Enter\" \033[0;37;40mto continue or:\ntype \033[1;36;40m\"most\" \033[0;37;40mfor the most times COOMed\n\nYou can also \033[1;32;40mvisualize \033[0;37;40mhow many times you've\nCOOMed with \033[1;32;40m\"v\"\033[0;37;40m!: ").strip()
            
            if contin.casefold() == "":
                continue

            if contin.casefold() == "most":

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
            
            if contin.casefold() == "v":
                total = sum(bruh) + counts["cum"]
                coomEye = ""
                for i in range(total):
                    coomEye = coomEye + "I"

                os.system("clear")
                
                tally["tally_1"] = ""
                for i in range(len(coomEye)):
                    tally["tally_{}".format(tally["tallies"])] = tally["tally_{}".format(tally["tallies"])] + "I"
                    if total <= 10:
                        divisor = 5
                    else:
                        divisor = 10

                    if len(tally["tally_{}".format(tally["tallies"])]) == divisor:
                        tally["tallies"] += 1
                        tally["tally_{}".format(tally["tallies"])] = ""
                        continue
                    
                    else:
                        continue


                for thing in tally:
                    if thing == "tallies":
                        pass
                    else:
                        print("\033[1;32;40m" + tally[thing])
                        tally[thing] = ""
                
                print("\033[0;37;40m(\033[0;31;40m{} \033[0;37;40mtimes)".format(total))

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

        if plus.casefold() == "h":

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
    \033[0;37;40mAs of CumNutter v1.1.0, the visualizer:
        -Shows you a tally of your COOMs

""")
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
