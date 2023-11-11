import fitz  # PyMuPDF

# Open the PDF file
pdf_document = fitz.open("/var/www/html/bank_statements/media/DANIEL.pdf")

# Specify the page number you want to extract coordinates from (e.g., page 2)
page_number = 2
page = pdf_document.load_page(page_number - 1)  # Page numbering starts from 0

# Define the coordinates (x1, y1, x2, y2) in points
x1 = 100  # Replace with the actual x-coordinate for the top-left corner
y1 = 200  # Replace with the actual y-coordinate for the top-left corner
x2 = 300  # Replace with the actual x-coordinate for the bottom-right corner
y2 = 400  # Replace with the actual y-coordinate for the bottom-right corner

# Print the coordinates
print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")

# Close the PDF document
pdf_document.close()
