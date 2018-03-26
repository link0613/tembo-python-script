Tembo Education
===

### Files
- education_json.py
> This uses data.json as input data.
- data.json
> For `education_json.py`
- education_input.py
> This supports manual input to add new items (parents and curriculum)

### Run
```bash
run education_json.py
```
```bash
run education_input.py
```
> Please see the input/output result.

```bash
$ python education_input.py

.::Parent Data::.

Please input the name of parent you are going to add to data. (ex: 'David') : 'testParent'
Please input the name of child (ex: 'Baby') : 'testBaby'
Please input the age of child (ex: 'Baby') : 5
        Added the data of parent and child (parent: testParent  child: testBaby

Please input the name of parent you are going to add to data. (ex: 'David') :
        Inputing parent data is completed!

.::Curriculum Data::.

Please input the age for inputing curriculum data.: 2

Please input the activity you're going to add.: 'new Activity for 2'
Added new activity:new Activity for 2

Please input the activity you're going to add.:
Adding activities for this age is completed.

Please input the age for inputing curriculum data.: 5
Added new age: 5

Please input the activity you're going to add.: 'activity for 5'
Added new activity:activity for 5

Please input the activity you're going to add.: 'new one'
Added new activity:new one

Please input the activity you're going to add.:
Adding activities for this age is completed.

Please input the age for inputing curriculum data.:
Inputing parent data is completed!

 Inputing data is completed.



Parent: Henry

        Child: Calvin    Age: 2

        .::Activity::.
        Go outside and feel surfaces.
        Draw with crayons.
        Play with soundmaking toys or instruments.
        Look at family pictures together.
        new Activity for 2

Parent: Ada

        Child: Lily      Age: 3

        .::Activity::.
        Build with blocks.
        Try a simple puzzle.
        Read a story together.

Parent: Emilia

        Child: Petra     Age: 1

        .::Activity::.
        Try singing a song together.
        Point and name objects.

Parent: Biff

        Child: Biff Jr   Age: 4

        .::Activity::.
        Curriculum complete!

Parent: Milo

        Child: None

Parent: testParent

        Child: testBaby  Age: 5

        .::Activity::.
        activity for 5
        new one
```
