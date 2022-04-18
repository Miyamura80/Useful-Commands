# Scrape Pdf

(Last updated: 17/04/2022)
Exceedingly difficult. Poorly formatted file, compared to html. Avoid if at all possible.

Solution: Combination of PyPDF2 and OCR e.g. `pytesseract`

## PyPDF2

<details>
  
  <summary> Reading </summary>
  
  ```python
  from PyPDF2 import PdfFileReader, PdfFileWriter

  file_path = 'notes.pdf'
  pdf = PdfFileReader(file_path)
 
  outline_dict = pdf.getOutlines() # Table of contents extraction
  
  named_destinations = pdf.getNamedDestinations() # :: Dict(str, PyPDF2.generic.Destination)
  for k,v in named_destinations:
    destination_page_num = pdf.getDestinationPageNumber(v) # :: int
    pageObj = pdf.getPage(destination_page_num) # :: PyPDF2.pdf.PageObject

  ```
  
</details>

<details>
  
  <summary> Writing </summary>
  
  ```python
  from PyPDF2 import PdfFileReader, PdfFileWriter
  writer = PdfFileWriter()
  
  # Misc Stuff 
  writer.removeLinks()
  writer.removeImages(ignoreByteStringObject=False) 
  
  with open("experiment.pdf", "wb") as f:
    writer.write(f)


  ```
  
</details>
