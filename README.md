# Picture to Text Converter

This is a simple Python script that allows you to convert an image containing text into its corresponding textual representation using the Tesseract OCR engine. The script uses the `pytesseract` library, which acts as a wrapper for Tesseract OCR.

## Prerequisites

Before running this script, ensure you have the following installed:

- Python (version 3.x recommended)
- Tesseract OCR engine (Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki))
- pytesseract Python library (`pip install pytesseract`)
- Tkinter (usually included with Python installations)

## Installation

1. Install Tesseract OCR engine using the provided link above.
2. Install pytesseract by running the following command:

```bash
pip install pytesseract
```

## Usage

1. Clone the repository or download the script directly.
2. Make sure Tesseract OCR is installed and the `tesseract` command is available on your system's PATH.
3. Run the script using the following command:

```bash
python picture_to_text.py
```

4. The script will open a file dialog to select an image file from your local system.
5. After selecting the image file, the script will process the image and print the extracted text to the console.

## Contributing

Contributions are welcome! If you find any issues with the script or want to enhance its functionality, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The script uses `pytesseract` library, which is a Python wrapper for Tesseract OCR.
- Tesseract OCR is an open-source OCR engine maintained by UB Mannheim.
