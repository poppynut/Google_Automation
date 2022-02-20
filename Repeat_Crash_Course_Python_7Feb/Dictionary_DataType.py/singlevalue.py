wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes in wardrobe.keys():
	for colors in wardrobe.values():
		print("{} {}".format(colors, clothes))