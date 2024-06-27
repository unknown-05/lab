from django.shortcuts import render

def fruits_and_students(request):
    fruits=['Apple','Banana','Orange','Grape']
    students=['Alice','Bob','Charlie','David']
    context={
        'students':students,
        'fruits':fruits
    }
    return render(request,'fs.html',context)