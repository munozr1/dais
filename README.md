## Description
This program processes a text file line by line and randomly adds extra whitespace (0-3 spaces) to the end of each line with a 30% probability. The modified content is saved to an output file. It's a simple utility script for text manipulation.

## Features
- Reads an input file line by line.
- Adds 0-3 spaces randomly to the end of lines with a 30% chance.
- Outputs the modified content to a specified file.

## Prerequisites
- Python 3.x installed on your system.

---

## Installation Instructions

### macOS/Linux
1. **Clone the repository or download the script**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
   *(If the script is provided directly, save it to your desired location.)*

2. **Make the script executable**:
   ```bash
   chmod +x dais.py
   ```

3. **Move the script to a directory in your PATH**:
   ```bash
   sudo mv dais.py /usr/local/bin/
   ```

4. **Run the program**:
   ```bash
   dais <input_file> <output_file>
   ```

### Windows
1. **Download the script**:
   Save the script as `dais.py` to your desired directory.

2. **Add the script directory to PATH**:
   - Navigate to **Control Panel** → **System and Security** → **System** → **Advanced system settings**.
   - Click **Environment Variables** → Locate the `Path` variable under **System Variables**.
   - Add the directory containing `dais.py` to the `Path` variable.

3. **Run the program**:
   Open a command prompt and type:
   ```cmd
   python dais.py <input_file> <output_file>
   ```
   *(Alternatively, use `dais.py` directly if `.py` files are associated with Python.)*

---

## Usage
Run the script with the following arguments:
```bash
dais <input_file> <output_file>
```

### Example
```bash
dais input.txt output.txt
```

This command reads `input.txt`, processes it to add random spaces to lines, and writes the output to `output.txt`.

---

## License
MIT License

---

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

