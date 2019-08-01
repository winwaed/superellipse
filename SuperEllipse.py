#!/usr/bin/env python

""" SuperEllipse Drawing in SVG

(C) Copyright Richard Marsden, Winwaed Software Technology LLC 2018
Code is distributed under the Berkeley (BSD) '3 clause' license
"""


from math import pi,cos,sin,pow,fabs,copysign
import os
import sys

# You will need to import svgwrite using pip3 if you do not already have it
import svgwrite


# Returns x to the power y, but preserves the sign of x
# This allows us to plot all four quadrants with a single loop and
# no additional sign logic
def signed_power(x,y):
    return copysign( pow(fabs(x),y) ,x)


# Draws the super ellipse
#  svgdoc - the svgwrite SVG document
#  cx,cy - Center coordinate for the super ellipse
#  diax,diay - Diameter (x,y) for the super ellipse
#  npnts  - Number of points to use (greater => more accurate shape)
#  order - Order of Super Ellipse. 2=Ellipse. >2 for a super ellipse
#  linecol - line color as a string, eg "rgb(255,0,0)"
#  fillcol - fill color as a string, eg "rgb(255,0,0)"

def SuperEllipse(svgdoc, cx, cy, diax, diay, npnts, order, linecol, fillcol):

    pnts = []
    power = 2.0 / order
    theta = pi * 2.0 / npnts
    radiusx = diax/2.0
    radiusy = diay/2.0

    for i in range(0,npnts):    
        x = cx + radiusx * signed_power(cos( i*theta), power)
        y = cy + radiusy * signed_power(sin( i*theta), power)
        pnts.append( (x,y) )

    svgdoc.add(svgdoc.polygon(points= pnts,
                                   stroke_width = "1",
                                   stroke = linecol,
                                   fill = fillcol))
    return svgdoc



# Command Line Handling

if __name__ == '__main__' :

    if ( len(sys.argv) != 5):
        print("Incorrect parameters\nExpected usage:")
        print("python3 SuperEllipse.py <file> <order> <size> <num points>")
        print("eg.\npython3 SuperEllipse.py output.svg 3 300 50")
        exit(1)

    # creates a red super ellipse of the specified size and order    
    fname = sys.argv[1]
    print(fname)
    order = float(sys.argv[2])
    sz = int(sys.argv[3])
    npnts = int(sys.argv[4])
    svg_document = svgwrite.Drawing(filename = fname,
                                        size = (sz,sz))
    svg_document = SuperEllipse(svg_document, sz/2,sz/2, sz,sz, npnts, order, "rgb(0,0,0)", "rgb(255,0,0)")

    svg_document.save()
