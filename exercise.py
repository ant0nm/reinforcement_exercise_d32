from random import choice

p = {
  'committee': ["Stella", "Salma", "Kai"],
  'title': "Very Important Project",
  'due_date': "December 14, 2019",
  'id': "3284",
  'steps': [
    {'description': "conduct interviews",
     'due_date': "August 1, 2018"
    },
    {'description': "code of conduct",
     'due_date': "January 1, 2018"
    },
    {'description': "compile results",
     'due_date': "November 10, 2018"
    },
    {'description': "version 1",
     'due_date': "January 15, 2019"
    },
    {'description': "revisions",
     'due_date': "March 30, 2019"
    },
    {'description': "version 2",
     'due_date': "July 12, 2019"
    },
    {'description': "final edit",
     'due_date': "October 1, 2019"
    },
    {'description': "final version",
     'due_date': "November 20, 2019"
    },
    {'description': "Wrap up",
     'due_date': "December 1, 2019"
    }
  ]
}

def assign_tasks(project):
    task_count = {}
    committee = project['committee'].copy()
    tasks = project['steps'].copy()
    while len(tasks) > 0 and len(committee) > 0:
        random_member = choice(committee)
        random_task = choice(tasks)
        random_task_index = project['steps'].index(random_task)
        if random_member in task_count:
            if task_count[random_member] == 3:
                committee.remove(random_member)
            else:
                task_count[random_member] += 1
                project['steps'][random_task_index]['person'] = random_member
                tasks.remove(random_task)
        else:
            task_count[random_member] = 1
            project['steps'][random_task_index]['person'] = random_member
            tasks.remove(random_task)

assign_tasks(p)

print("People and tasks:")
person_to_num_tasks = {}
for step in p['steps']:
    person = step["person"]
    if person in person_to_num_tasks:
        person_to_num_tasks[person] += 1
    else:
        person_to_num_tasks[person] = 1

for person, n_tasks in person_to_num_tasks.items():
    print(f"Name: {person} | Number of tasks: {n_tasks}")

print()
print("A list of all the tasks with the new person key:")
for step in p["steps"]:
    print(f"* Description: {step['description']} \n Person: {step['person']}")
