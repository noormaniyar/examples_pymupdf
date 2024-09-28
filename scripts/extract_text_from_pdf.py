import pymupdf

input_file_path = "input_files/case.pdf"
output_file_path = "output_files/output.txt"

doc = pymupdf.open(input_file_path) # open a document
print(doc, '=================doc================')
out = open(output_file_path, "wb") # create a text output
print(out, '--------------------------out-----------------')
for page in doc: # iterate the document pages
    print(page, '----------------------page--------------')
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    print(text, '---------------------------text-----------------')
    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
out.close()
