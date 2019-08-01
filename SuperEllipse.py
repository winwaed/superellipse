#!/usr/bin/env python

# Copyright 2019 Winwaed Software Technology LLC
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following
# conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following 
# disclaimer in the documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

""" SuperEllipse Drawing to an SVG file

See the se_demo.py for example usage
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
