# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, True, False)
print formatter % (
	"i had this thing.",
	"that you could type up right.",
	"but it didn‘t sing.",
	"so i said goodnight."
)
