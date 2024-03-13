from django.shortcuts import render
# Create a list of dictionaries representing books
projectList = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "description": "A novel by F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "description": "A novel by Harper Lee"
    },
    {
        "id": 3,
        "title": "1984",
        "description": "A dystopian novel by George Orwell"
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "description": "A novel by Jane Austen"
    },
    {
        "id": 5,
        "title": "The Catcher in the Rye",
        "description": "A novel by J.D. Salinger"
    }
]

# P

# Create your views here.
# create a view that will be return by the view
def projects(request):
    username = {'name': 'John Doe'}
    number = 20
    context = {'username': username, 'number':number, 'projects': projectList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    # item = {'pk': pk}
    projecObj = None

    for i in projectList:
        # print('Value: {}'.format(i['id']))
        if i['id'] == int(pk):
            print('True')
            projecObj = i

    return render(request, 'projects/single-project.html', {'project': projecObj})