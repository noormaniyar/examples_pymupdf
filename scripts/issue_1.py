"""
    doc = fitz.open(pdf_file)
    for page in doc:
    pix = page.get_pixmap()
    img_file = f'{img_file_prefix}-{page.number}.jpg'
    pix.save(img_file)

    Will get_pixmap cause the generated JPG image to be too large in the above code? 
    Is there a better way to convert every page in the PDF into a JPG image?
"""
import pymupdf
import fitz


pdf_file = "input_files/case.pdf"

doc = fitz.open(pdf_file)

print(doc, '---------------------doc----------------')
for page in doc:
    print(page, '------------------page-----------------')
    pix = page.get_pixmap()
    print(pix, '-------------------pix----------------')
    # img_file = f'{img_file_prefix}-{page.number}.jpg'
    img_file = f'aaaaaaaaaaaaa-{page.number}.jpg'
    print(img_file, '-----------------------img_file----------------')
    pix.save(img_file)
    