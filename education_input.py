
#initial data
parents = [
    {'parent': 'Henry', 'child': {'name': 'Calvin', 'age': 2}},
    {'parent': 'Ada', 'child': {'name': 'Lily', 'age': 3}},
    {'parent': 'Emilia', 'child': {'name': 'Petra', 'age': 1}},
    {'parent': 'Biff', 'child': {'name': 'Biff Jr', 'age': 4}},
    {'parent': 'Milo', 'child': {}}
]

curriculum = [
    {
        'age': 1,
        'activity': [
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Go outside and feel surfaces.',
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]



#preparing data
print '\n.::Parent Data::.'
while True:
	try:
		parentName = input('\nPlease input the name of parent you are going to add to data. (ex: \'David\') : ')
	except:
		print '\tInputing parent data is completed!'
		break

	childName = ''
	try:
		childName = input('Please input the name of child (ex: \'Baby\') : ')
	except:
		print '\tAdded parent ' + parentName
		print '\tInputing child data is finished.'
		parentData = {'parent': parentName, 'child': {}}
		parents.append(parentData)
		continue

	childAge = 1
	try:
		childAge = input('Please input the age of child (ex: \'Baby\') : ')
	except:
		print '\tAge should be as \'Integer\'! Its value will be 1.'
	
	parentData = {'parent': parentName, 'child': {'name': childName, 'age': childAge}}
	parents.append(parentData)
	print '\tAdded the data of parent and child (parent: ' + parentName + '\tchild: ' + childName

print '\n.::Curriculum Data::.'
while True:
	try:
		curriculumAge = input('\nPlease input the age for inputing curriculum data.: ')
	except:
		print 'Inputing parent data is completed!'
		break
	curriculumIndexList = [curriculumIndex for curriculumIndex, curriculumEach in enumerate(curriculum) if curriculumEach['age'] == curriculumAge]
	if len(curriculumIndexList) == 0:
		curriculum.append({'age':curriculumAge, 'activity':[]})
		curriculumIndexList = [len(curriculum) - 1]
		print '\tAdded new age: ' + str(curriculumAge)
	
	while True:
		try:
			activityItem = input('\nPlease input the activity you\'re going to add.: ')
			curriculum[curriculumIndexList[0]]['activity'].append(str(activityItem))
			print '\tAdded new activity:' + str(activityItem)
		except:
			print '\tAdding activities for this age is completed.'
			break

print '\n Inputing data is completed. \n\n'

# cycling				
for parent in parents:
	#display parent
	print '\nParent: ' + parent['parent'] 
	
	#display child info
	try: 
		print '\n\tChild: ' + parent['child']['name'] + '\t Age: ' + str(parent['child']['age']) 
	except:
		print '\n\tChild: None'
		continue
	
	#looking for activities with age
	try:
		activities = [curriculumEach['activity'] for curriculumEach in curriculum if curriculumEach['age'] == parent['child']['age']]
		if len(activities)==0:
			activities = [['Curriculum complete!']]
	except:
		activities = [['Curriculum complete!']]

	#display activity	
	print '\n\t.::Activity::.'
	for index, activity in enumerate(activities[0]):
		print '\t' + activity
print '\n\n\n'




