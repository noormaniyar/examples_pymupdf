import pymupdf

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 08:34:06 2018

@author: Jorj
@license: GNU AFFERO GPL V3

Create a list of available symbols defined in shapes_and_symbols.py

This also demonstrates an example usage: how these symbols could be used
as bullet-point symbols in some text.

"""

import pymupdf
import sys
sys.path.append('lib') 
import shapes_and_symbols as sas

# list of available symbol functions and their descriptions
tlist = [
         (sas.arrow, "arrow (easy)"),
         (sas.caro, "caro (easy)"),
         (sas.clover, "clover (easy)"),
         (sas.diamond, "diamond (easy)"),
         (sas.dontenter, "do not enter (medium)"),
         (sas.frowney, "frowney (medium)"),
         (sas.hand, "hand (complex)"),
         (sas.heart, "heart (easy)"),
         (sas.pencil, "pencil (very complex)"),
         (sas.smiley, "smiley (easy)"),
         ]

r = pymupdf.Rect(50, 50, 100, 100)  # first rect to contain a symbol
d = pymupdf.Rect(0, r.height + 10, 0, r.height + 10)  # displacement to next rect
p = (15, -r.height * 0.2)  # starting point of explanation text
rlist = [r]  # rectangle list

for i in range(1, len(tlist)):  # fill in all the rectangles
    rlist.append(rlist[i-1] + d)

doc = pymupdf.open()  # create empty PDF
page = doc.new_page()  # create an empty page
shape = page.new_shape()  # start a Shape (canvas)

for i, r in enumerate(rlist):
    tlist[i][0](shape, rlist[i])  # execute symbol creation
    shape.insert_text(rlist[i].br + p,  # insert description text
                   tlist[i][1], fontsize=r.height/1.2)

# store everything to the page's /Contents object
shape.commit()

import os
scriptdir = os.path.dirname(__file__)
doc.save(os.path.join(scriptdir, "symbol-list.pdf"))  # save the PDF




input_file_path = "input_files/case.pdf"

import pymupdf
doc = pymupdf.open(input_file_path)
page = doc[0]
paths = page.get_drawings()  # extract existing drawings
# this is a list of "paths", which can directly be drawn again using Shape
# -------------------------------------------------------------------------
#
# define some output page with the same dimensions
outpdf = pymupdf.open()
outpage = outpdf.new_page(width=page.rect.width, height=page.rect.height)
shape = outpage.new_shape()  # make a drawing canvas for the output page
# --------------------------------------
# loop through the paths and draw them
# --------------------------------------
for path in paths:
    # ------------------------------------
    # draw each entry of the 'items' list
    # ------------------------------------
    for item in path["items"]:  # these are the draw commands
        if item[0] == "l":  # line
            shape.draw_line(item[1], item[2])
        elif item[0] == "re":  # rectangle
            shape.draw_rect(item[1])
        elif item[0] == "qu":  # quad
            shape.draw_quad(item[1])
        elif item[0] == "c":  # curve
            shape.draw_bezier(item[1], item[2], item[3], item[4])
        else:
            raise ValueError("unhandled drawing", item)
    # ------------------------------------------------------
    # all items are drawn, now apply the common properties
    # to finish the path
    # ------------------------------------------------------
    shape.finish(
        fill=path["fill"],  # fill color
        color=path["color"],  # line color
        dashes=path["dashes"],  # line dashing
        even_odd=path.get("even_odd", True),  # control color of overlaps
        closePath=path["closePath"],  # whether to connect last and first point
        lineJoin=path["lineJoin"],  # how line joins should look like
        lineCap=max(path["lineCap"]),  # how line ends should look like
        width=path["width"],  # line width
        stroke_opacity=path.get("stroke_opacity", 1),  # same value for both
        fill_opacity=path.get("fill_opacity", 1),  # opacity parameters
        )
# all paths processed - commit the shape to its page
shape.commit()
outpdf.save("drawings-page-0.pdf")