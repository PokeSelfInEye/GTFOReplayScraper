import sys
import csv  
import os

def parse_csv(input_file, output_file):
    """
    Parses GTFO replay CSVs and writes data to the output CSV file.
    """
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append(list(row))
            
    if not data:
        return
        
    with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Safely extract and strip header identifiers: Expedition, Date, Duration
        expedition = data[0][1].strip()
        date_val = data[0][3].strip()
        
        # Duration can shift index due to dynamic player counts. Search for its index.
        duration_val = "Unknown"
        for i, val in enumerate(data[0]):
            clean_val = val.strip().lower()
            if "duration:" in clean_val:
                if i + 1 < len(data[0]):
                    duration_val = data[0][i+1].strip()
                break
                
        identifier = [expedition, date_val, duration_val]
        for row in data:
            # Skip empty lines, metadata headers, and player headers
            if not row or "# Run ID:" in row[0] or "Player Name" in row[0]:
                continue
            writer.writerow(identifier + row)


def main():
    """
    Main function to parse and compile GTFO replay CSV data
    """
    if len(sys.argv) < 2:
        print("Error: No output file specified.")
        sys.exit(1)
    output_file = sys.argv[1]

     # If output file does not exist, initialize it with headers
    if not os.path.exists(output_file):
        print(f"Output file '{output_file}' not found, creating new file.")
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            csvfile.write(f"# Compiled GTFO Replay Data\n")
            writer = csv.writer(csvfile)
            headers = [
                "Expedition", "Date", "Duration", "Player Name", "Steam ID", "Bullet Damage", "Melee Damage", "Sentry Damage", 
                "Explosive Damage", "Total Damage Dealt", "Stagger Damage", "Sentry Stagger Damage",
                "Kills", "Sentry Kills", "Mine Kills", "Total Kills", "Ammo Packs Used", 
                "Tool Packs Used", "Health Packs Used", "Disinfect Packs Used", "Revives", "Downs", "Tongue Dodges"
            ]
            writer.writerow(headers)
    
    # Parse a specified file
    if len(sys.argv) > 2:
        target_file = sys.argv[2]
        if not os.path.exists(target_file):
            print(f"Error: {target_file} does not exist.")
            sys.exit(1)
        parse_csv(target_file, output_file)
    else:
        # Parse all CSV files in the 'CSVs' directory
        base_dir = "."
        csv_root = os.path.join(base_dir, "CSVs")
        if not os.path.exists(csv_root):
            print(f"Error: {csv_root} does not exist.")
            sys.exit(1)
        
        parsed_count = 0
        for file in os.listdir(csv_root):
            if file.endswith(".csv"):
                parse_csv(os.path.join(csv_root, file), output_file)
                parsed_count += 1
        if parsed_count == 0:
            print("No CSV files found in the 'CSVs' directory.")
        else:
            print(f"Successfully parsed {parsed_count} CSV files.")

if __name__ == "__main__":
    main()
