Made for use with GTFO replays made from randomuserhi's GTFO replay mod: https://github.com/randomuserhi/GTFOReplay

You must have python3 installed for these scripts to work https://www.python.org/downloads/

To use:
1. Place both scripts in a folder of your choice, then add two folders at the same level as the python files: One called "CSVs" and one called "Replay Files" 

2. In the replay files folder create two folders: "Checked Replays" and "Unchecked Replays"
  ```
               <Parent Directory>
                 /             \
            Replay Files       CSVs
             /       \
  Checked Replays  Unchecked Replays
  ```


3. Place replays you want scanned by the parser in the "Unchecked Replays" folder, and when done move them to the "Checked Replays" folder. (This move might be automated if I get around to it but I probably won't since the file count is manageable right now and I like playing the game more than I like coding.)

4. In a terminal of your choice change directory to your parent folder then run the command:
   ```
   py parse_replay.py
   ```

5. This will parse all replays you have in the "Unchecked Replays" folder and create corresponding CSVs for them in the CSVs folder.

6. To compile CSVs run:
   ```
   py compile_csvs.py <output file name>.csv
   ```
   If the output file already exists in the parent folder the script will append all CSVs in the CSVs folder to the end of the target file. If the output file does not exist the script will make a new one.




Acknowledgements: 

The parse_replay script was made mostly using Gemini 3.5 Flash in Google Antigravity. All of the replay parsing logic is copied from randomuserhi's GTFO replay viewer and translated from JavaScript. 
