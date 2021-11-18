HEY, ANDROID USERS... you might wanna read the following :)

HOW TO INSTALL ON ANDROID:

1. Download F-Droid if you haven't at https://f-droid.org/
   (F-Droid is an app store for free and open source apps, don't worry, F-Droid is widely trusted,
    so don't be alarmed if your browser asks you to allow downloads from external sources (still, don't go downloading random APKs!)

2. Download Termux from F-Droid, open Termux

3. Type or copy and paste this single line into Termux (make SURE to press enter once you've pasted it, LOOKING AT YOU, OFI):

     pkg install git -y; git clone https://github.com/CummyWum/CummyCount.git; cd CummyCount; chmod +x move.sh; ./move.sh; cd ~;

4. Now that all of that is out of the way, you won't ever have to do all of that again!
   From now on, you can run CummyCounter whenever you'd like by entering the command:
   
   
   python3 cum_count.py


5. As for future updates, if you DON'T wanna lose your entries:
   Since I don't think you can download individual files from Github,
   you can download JUST the "cum_count.py" file from this Google Drive:
   
   https://drive.google.com/drive/folders/1UOWrGRB-DdzSoIRvTGyQqxPW8XAM6hLl?usp=sharing
   
   Then, after downloading it, look for it in your Downloads in the Files app,
   choose "open with," and once the prompt shows up, choose Termux
   
   Then, just click "OPEN DIRECTORY"
   Lastly, you just need to paste:
   
   mv cum_count.txt ~/; cd ~; cp cum_count.txt cum_count.py; rm cum_count.txt
  
  
  
   And now you have the newest version of CummyCount! Of course, just run it with:
   
   python3 cum_count.py
   
