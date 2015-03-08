#MenuTitle: OTF Export with Custom Parameter v1
# -*- coding: utf-8 -*-
__doc__="""
Export OTF with CustomParameter on the fly and Remove CP again
"""

import time
import GlyphsApp
from vanilla import *

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs

Glyphs.clearLog()
thisFont.disableUpdateInterface() # suppresses UI updates in Font View

## set the custom parameter
cpName = "Rename Glyphs"
cpValue = ("A=Alpha", "B=Beta", "C=Gamma", "G=Iota") ## must be a tuple


def setCP(cpName, cpValue):
	'''Set the Custom Parameter(s) for all instances'''

	## check each CP for existing ones
	for instance in thisFont.instances:
		if not instance.customParameters[cpName]:
			instance.customParameters[cpName] = cpValue
			## print cmd need to display ONLY the set CP, not all existing ones!
			print "added: %s\nto %s\n" % ( instance.customParameters, instance.name )
		else:
			print "%s already in CustomParameter, not added to %s\n" % ( cpName, instance.name) 


def OTFExport():
	'''Export to OTF'''
	Exporter = NSClassFromString("GlyphsFileFormatOTF").alloc().init()
	f = Glyphs.fonts[0]
	Result = Exporter.writeFont_error_(f, None)
	print f, "\n", "Result:", Result


def removeCP():
	'''Remove Custom Parameter(s) for all instances'''
	for instance in thisFont.instances:
		for i in reversed(range(len(instance.customParameters))):
			if instance.customParameters[i].name == cpName:
				del(instance.customParameters[i])



delay = 5
class ProgressBarDemo(object):
    def __init__(self):
        self.w = Window((200, 65))
        self.w.bar = ProgressBar((10, 10, -10, 16))
        self.w.open()

        setCP(cpName, cpValue)
        OTFExport()

        self.w.bar.set(0)
        barSmooth = 8
        for i in range(delay*barSmooth):
            self.w.bar.increment(100/float(barSmooth)/delay)
            sleepFraction = float(1)/float(barSmooth)
            time.sleep(sleepFraction)

        removeCP()
        self.w.close()
ProgressBarDemo()


thisFont.enableUpdateInterface() # re-enables UI updates in Font View
print "Done!"
Glyphs.showMacroWindow()
