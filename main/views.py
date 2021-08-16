from django.shortcuts import render

# Create your views here.
def homepage(request):
    pass

def peoples(request):
    people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]
    lst = []
    y = 0
    while y <len(people):
        x = people[0]
        for person in people:
            if person['age'] > x['age']:
                x = person
        lst.append(x) 
        people.remove(x)
               
    context = {'people': lst }
    return render(request, 'peoples.html', context)

def id(request,num): 
    people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]
    for person in people:
        if person['id'] == num:
            context = {'id': person }
            return render(request, 'id.html', context)
    return render(request, 'id.html')        