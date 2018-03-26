import json

#read data
try:
	data = json.load(open('data.json'))
except:
	print '\tCan\'t read data from \'data.json\''
	quit()

try:
	parents = data['parents']
	curriculums = data['curriculum']
except:
	print '\tPlease check data structure. Can\'t find out `parents` or `curriculum`'
	quit()

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
		activities = [curriculum['activity'] for curriculum in curriculums if curriculum['age'] == parent['child']['age']]
		if len(activities)==0:
			activities = [['Curriculum complete!']]
	except:
		activities = [['Curriculum complete!']]

	#display activity	
	print '\n\t.::Activity::.'
	for index, activity in enumerate(activities[0]):
		print '\t' +  parent['parent'] + ' : ' + activity
print '\n\n\n'




