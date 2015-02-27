#MenuTitle: OTF Export with Custom Parameter 01.py
# -*- coding: utf-8 -*-
__doc__="""
Export OTF with CustomParameter on the fly and Remove CP again
"""

import time
import GlyphsApp

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs

Glyphs.clearLog()
thisFont.disableUpdateInterface() # suppresses UI updates in Font View

######################################
## CP Handling
######################################

## set the custom parameter
cpName = "Rename Glyphs"
cpValue = ("A=Alpha", "B=Beta", "C=Gamma", "G=Iota") ## must be a tuple

## check each CP for existing ones
for instance in thisFont.instances:
	if not instance.customParameters[cpName]:
		instance.customParameters[cpName] = cpValue
		print "added: %s\nto %s\n" % ( instance.customParameters, instance.name )
	else:
		print "%s already in CustomParameter, not added to %s\n" % ( cpName, instance.name) 
	

######################################
## OTF Export
######################################

Exporter = NSClassFromString("GlyphsFileFormatOTF").alloc().init()
f = Glyphs.fonts[0]

Result = Exporter.writeFont_error_(Glyphs.fonts[0], None)
print Glyphs.fonts[0], "\n", "Result:", Result

######################################
## remove the CP after export
######################################

time.sleep(15) ## delay to finish exporting before removing the CP again
for instance in thisFont.instances:
	for i in reversed(range(len(instance.customParameters))):
		if instance.customParameters[i].name == cpName:
			del(instance.customParameters[i])

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
print "Done!"
Glyphs.showMacroWindow()

