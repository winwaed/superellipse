#!/usr/bin/env python

"""
Demonstration of different super ellipse shapes
Super ellipses are written to multiple.svg and are labelled with 
the corresponding polynomial order

(C) Copyright Richard Marsden, Winwaed Software Technology LLC 2018
"""

import svgwrite
import SuperEllipse

dia = 100
npnts = 50


svg_document = svgwrite.Drawing(filename = "multiple.svg", size = (500,500))
svg_document.add(svg_document.rect(insert=(0,0), size=('100%','100%'), rx=None, ry=None, fill='rgb(255,255,255)'))

order = 0.3
svg_document = SuperEllipse.SuperEllipse(svg_document, 60,60, dia,dia, npnts, order, "rgb(0,0,0)", "rgb(255,0,0)")
svg_document.add(svg_document.text(str(order),insert=( 55,125)) )

order = 0.5
svg_document = SuperEllipse.SuperEllipse(svg_document, 180,60, dia,dia, npnts, order, "rgb(0,0,0)", "rgb(255,85,0)")
svg_document.add(svg_document.text(str(order),insert=( 175,125)) )

order = 1
svg_document = SuperEllipse.SuperEllipse(svg_document, 300,60, dia,dia, npnts, order, "rgb(0,0,0)", "rgb(255,170,0)")
svg_document.add(svg_document.text(str(order),insert=( 295,125)) )

order = 1.3
svg_document = SuperEllipse.SuperEllipse(svg_document, 60,180, dia,dia, npnts, order, "rgb(0,0,0)", "rgb(255,255,0)")
svg_document.add(svg_document.text(str(order),insert=( 55,245)) )

order = 1.7
svg_document = SuperEllipse.SuperEllipse(svg_document, 180,180, dia,dia, npnts, order, "rgb(0,0,0)", "rgb(220,221,0)")
svg_document.add(svg_document.text(str(order),insert=( 175,245)) )

order = 2.0
svg_document = SuperEllipse.SuperEllipse(svg_document, 300,180, dia,dia, npnts, order, "rgb(0,0,0)", "rgb(85,196,0)")
svg_document.add(svg_document.text(str(order),insert=( 295,245)) )

order = 3.0
svg_document = SuperEllipse.SuperEllipse(svg_document, 60,300, dia,dia, npnts, order, "rgb(0,0,0)", "rgb(0,255,0)")
svg_document.add(svg_document.text(str(order),insert=( 55,365)) )

order = 5.0
svg_document = SuperEllipse.SuperEllipse(svg_document, 180,300, dia,dia, npnts, order, "rgb(0,0,0)", "rgb(0,127,127)")
svg_document.add(svg_document.text(str(order),insert=( 175,365)) )

order = 10.0
svg_document = SuperEllipse.SuperEllipse(svg_document, 300,300, dia,dia, npnts, order, "rgb(0,0,0)", "rgb(0,0,255)")
svg_document.add(svg_document.text(str(order),insert=( 295,365)) )


svg_document.save()
