

def street_47th():
	print "now you are in 47th street"
	print "your enemy is the butcher, and a gun in you hand"
	print "How are you going to througt?"

	choice = raw_input(">")

	if "shot" in choice:
		print "you shotted the butcher, he dead "
		success()
	else:
		dead("the butcher will skin you")



def jungle():
	print "now you are in jungle"
	print "your enemy is vice, who is the dinosaurs hunter ,and a knife in you hand"
	print "How are you going to througt?"

	hoice = raw_input(">")

	if "knife" in choice:
		print "you kill the hunter, he dead "
		success()
	else:
		dead("the butcher will skin you")


def desert():
	print "now you are in desert"
	print "there is a car"
	print "How are you going to througt the desert?"

	choice = raw_input(">")

	if "car" in choice:
		print "take the car,it would be safe"
		success()
	else:
		dead("you Trapped in the desert")



def success():
	print "you win"
	print "thank you for playing"

def dead(why):
	print "you were killed", why



def start():
	print "welcome to Xenozoic"
	print "please choice a pole: Jack, Hannah or Mess?"
	print "let's go!"

	pole = raw_input(">")

	if "Jack" in pole:
		street_47th()
	elif "Hannah" in pole:
		jungle()
	elif "Mess" in pole:
		desert()	
	else:
		print "you must choice a pole, hurry up"
		start()


start()