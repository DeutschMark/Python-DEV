#MenuTitle: OTF Export with Custom Parameter 01.py
# -*- coding: utf-8 -*-
__doc__="""
Export OTF with CustomParameter on the fly and Remove CP again
"""
# ToDo 	- Add sth to font name (like "Fontname OSF", "Fontname LF") taken from a list
#		  this shall generate a bunch of slightly different fonts with different char sets
#		- ** make another one with color well for putting the instance colors

import time
import GlyphsApp

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
listOfSelectedLayers = thisFont.selectedLayers # active layers of selected glyphs

# brings macro window to front and clears its log:
Glyphs.clearLog()
Glyphs.showMacroWindow()

thisFont.disableUpdateInterface() # suppresses UI updates in Font View
#print dir(thisFont)

## Master Custom Parameter:
print "MasterCP:", thisFontMaster.customParameters

## Font Custom Parameter:
print "FontCP:", thisFont.customParameters


######################################
## CP Handling
######################################

## set the custom parameter (NEW WAY)
cpName = "Rename Glyphs"
#cpValue = "A=Fuck"
cpValue = ("zero.lf=zero", "one.lf=one", "two.lf=two", "three.lf=three", "four.lf=four", "five.lf=five", "six.lf=six", "seven.lf=seven", "eight.lf=eight", "nine.lf=nine")
#cpValue = ("A=Alpha", "B=Beta", "C=Gamma", "G=Iota") ## must be a tuple


### OVERWRITING each CP
# for instance in thisFont.instances:
# 	instance.customParameters[cpName] = cpValue
# 	print "added: %s\nto %s\n" % ( instance.customParameters, instance.name )

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

# familyName = f.familyName.replace(' ', '')
#print len(f.instances), "Instances:", "\n"
# for k in f.instances:
#     print k.name, "\n", k, "\n"    ## k.width / k.weight
#     styleName = k.name.replace(' ', '')   
#     fullName = familyName + '-' + styleName

Result = Exporter.writeFont_error_(Glyphs.fonts[0], None)
print Glyphs.fonts[0], "\n", "Result:", Result

######################################
## remove the CP after export
######################################

''' Georg says: You can only access the entries by index. And you should be careful if youre
interacting a list and change it at the same time. Iterating backwards prevents problems.
customParameters can be more than one w/ same name. So it acts as a list object.
'''

time.sleep(15) ## delay to finish exporting before removing the CP again
for instance in thisFont.instances:
	for i in reversed(range(len(instance.customParameters))):
		if instance.customParameters[i].name == cpName:
			del(instance.customParameters[i])

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
print "Done!"

