wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloths in wardrobe.keys():
	for colors in wardrobe.values():
		print("{} {}".format(colors, clothes))