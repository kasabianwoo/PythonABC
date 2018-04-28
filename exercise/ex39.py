# create a mapping of state to abbreviation

states = {
	'oregon':'OR',
	'florida':'FL',
	'california':'CA',
	'michigan':'MI'
}

# create a basic set of states and some cities in them

cities = {
	'CA':'san francisco',
	'MI':'detroit',
	'FL':'jacksoville'
}


# add some more cities

cities['NY'] = 'new york'
cities['OR'] = 'portland'


# print out some cities

print '-'*10
print cities['NY']
print cities['OR']


# do it by using the state then cities dict

print '-'*10
print cities[states['florida']]
print cities[states['michigan']]


# print every state abbreviaton

print '_'*10
for state,abbrev in states.items():
	print "%s is abbreviated %s" % (state,abbrev)


# print every city in state
print '_'*10
for abbrev,city in cities.items():
	print "%s has the city %s" % (abbrev,city)


# now do both at the same time
print '_'*10
for state,abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state,abbrev,cities[abbrev])


print '_'*10
# safely get a abbreviation by state that might not be there 
state = states.get('Texa')

if not state:
	print "sorry, no texas."

# get a city with a defaut value
city = cities.get('TX','does not exist')
print "the city for state 'TX' is : %s" % city



