✂️ PDF Page Extractor / Splitter using Python
This is a Python-based PDF page extractor tool that allows users to split or extract specific pages from a PDF file using the PyPDF2 library. It provides two modes:

Extract a range of pages

Extract custom pages manually

🛠️ Features
Extract a specific range of pages (e.g., pages 3 to 7)

Manually select custom pages in any order

Creates a new PDF with the selected pages

Handles invalid page numbers gracefully

⚙️ How It Works
The user is prompted to enter the name of the input PDF and the desired name for the output PDF.

The user chooses one of two options:

Enter a start and end page to extract a continuous range.

Enter individual page numbers manually in any order.

The selected pages are added to a new PDF.

The final output is saved with the name provided by the user.

✅ Example Run

Enter the name of input pdf: source.pdf  
Enter the name of output pdf: extracted  
Enter '1' if you want to give the start and end page number or '2' to enter the page numbers manually: 1  
Enter the starting page: 2  
Enter the ending page: 5  
This will create extracted.pdf containing pages 2 to 5 of source.pdf.

🧰 Requirements
Python 3.x

PyPDF2

Install with:

pip install PyPDF2
🛡️ Error Handling
If the page numbers exceed the number of pages in the PDF, it catches the IndexError.

Non-integer inputs for manual page numbers are not currently handled
