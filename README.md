# PDF Text Extractor
This script extracts text from a PDF file and saves each page's text into separate text files. It utilizes the pdfreader library to read and process PDF files.

Usage
  ```shell
  python main.py <pdf_file>
  ```
## Dependencies
- pdfreader: Install it using pip install pdfreader.

## Code Explanation
1. Import the necessary modules: os, sys, warnings, and pdfreader.
2. Check if the PDF file argument is provided via command-line. If not, display the usage instructions and exit.
3. Get the PDF file name from the command-line argument.
4. Create a directory named "hasil" (if it doesn't exist) to store the extracted text files.
5. Open the PDF file in binary mode using the open() function.
6. Create a SimplePDFViewer object to read the PDF file.
7. Ignore warning messages during PDF processing using the warnings.filterwarnings() function.
8. Iterate over each page in the PDF document.
9. Retrieve the text content from the current page using the canvas.strings attribute.
10. Determine the output file name based on the PDF file name and the page index.
11. Write the extracted text to a text file with the determined output name.
12. Repeat the process for each page in the PDF file.
13. The script completes and exits.

➡️Make sure to replace <pdf_file> with the actual path to the PDF file you want to extract text from. <br>
➡️To run the script, execute the command mentioned in the "Usage" section, and ensure that the pdfreader library is installed.
