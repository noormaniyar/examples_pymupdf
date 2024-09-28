# import pymupdf

# input_file_path = "input_files/case.pdf"


# doc = pymupdf.open(input_file_path) # open a document

# for page_index in range(len(doc)): # iterate over pdf pages
#     page = doc[page_index] # get the page
#     image_list = page.get_images()

#     # print the number of images found on the page
#     if image_list:
#         print(f"Found {len(image_list)} images on page {page_index}")
#     else:
#         print("No images found on page", page_index)

#     for image_index, img in enumerate(image_list, start=1): # enumerate the image list
#         xref = img[0] # get the XREF of the image
#         pix = pymupdf.Pixmap(doc, xref) # create a Pixmap

#         if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
#             pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

#         # pix.save("output_files/page_%s-image_%s.png" % (page_index, image_index)) # save the image as png
#         # pix.save("output_files/image_{}_{}.png".format(page_index, image_index))
#         pix.save(f"output_files/image_{page_index}_{image_index}.png")

#         pix = None