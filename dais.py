#!python3
import random
import sys

def add_random_spaces(file_path, output_file):
    try:
        with open(file_path, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if random.random() < 0.3:  # 30% chance
                    spaces_to_add = random.randint(1, 3)  #random spaces between 0-3
                    line = line.rstrip() + (' ' * spaces_to_add) + '\n'
                outfile.write(line)
        print(f"Processed file saved to {output_file}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        add_random_spaces(input_file, output_file)
