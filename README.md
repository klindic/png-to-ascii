# ASCII Image Converter

This script converts an image to an ASCII art representation and saves it to a text file.

## Requirements

- Python 3.x
- Pillow (PIL)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the Pillow library using pip:
   ```
   pip install pillow
   ```

## Usage

1. Place the image you want to convert in the same directory as the script and name it `logo.png`. Alternatively, you can modify the `path` variable in the script to point to your image file.
2. Run the script:
   ```
   python main.py
   ```
3. The ASCII art will be saved to `ascii_image.txt` in the same directory.

## Notes

- The `chars` list can be modified to use different characters for the ASCII art.
- The `new_width` variable can be adjusted to change the width of the ASCII art.
- Ensure the path to the image file is correct if not using `logo.png`.

---

Feel free to modify the script to suit your needs. Contributions are welcome!
