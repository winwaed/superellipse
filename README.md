This is a Python script to an SVG super ellipse

Super ellipses are a little bit of a mathematical oddity, resembling rounded squares or square-ish circles. They are, however, becoming popular for icon outlines. iOS currently uses them, as do recent versions of Android. This article shows you how to use Python to create an arbitrary super ellipse in SVG. This can then be used as an image mask to create a super elliptical icon.

Super ellipses are sometimes mistakenly called “squircles”. True squircles are simply squares with rounded corners. A super ellipse does not have any straight edges and has more of a continuous curve, eg.:

<img src="https://www.winwaed.com/blog/wp-content/uploads/2018/06/test-svgwrite.svg?sanitize=true">

A more complete discussion including some maths can be found on my blog at: https://www.winwaed.com/blog/2018/06/15/drawing-svg-superellipses-with-python/

The se_demo.py script demonstrates how multiple super ellipses can be written to an SVG file, and results in the following sampler of multiple super ellipses of with polynomial orders:

<img src="https://github.com/winwaed/superellipse/blob/master/multiple.svg?sanitize=true">
