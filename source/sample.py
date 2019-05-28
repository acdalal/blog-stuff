from audit import audit

'''
This is a sample decision algorithm, to demonstrate how to use the Scenario and Person classes. 

The algorithm saves the group with more cats. In case of a tie, or in case of no cats, the algorithm saves the group with more children. If neither of these conditions are met, the algorithm saves the passengers. 
'''
def automatic_decision(scenario):
	# count the number of cats and children in each group
	numCatsInCar = 0
	numCatsInCross = 0
	numKidsInCar = 0
	numKidsInCross = 0

	pedestrians = scenario.getPedestrians()
	passengers = scenario.getPassengers()

	for person in pedestrians:
		if person.getCharType() == "cat":
			numCatsInCross += 1
		elif person.getCharType() == "human" and person.getAge() == "child":
			numKidsInCross += 1

	for person in passengers:
		if person.getCharType() == "cat":
			numCatsInCar += 1
		elif person.getCharType() == "human" and person.getAge() == "child":
			numKidsInCar += 1

	# determine which group to save
	# prioritize cats, then kids
	if numCatsInCar > numCatsInCross:
		return "passengers"
	elif numCatsInCross > numCatsInCar:
		return "pedestrians"
	elif numKidsInCar > numKidsInCross:
		return "passengers"
	elif numKidsInCross > numKidsInCar:
		return "pedestrians"
	else:
		# if all else fails, save the passengers
		return "passengers" 

if __name__ == '__main__':
	audit(automatic_decision, 10, seed=8675309)
