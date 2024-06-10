from django.shortcuts import render

# Create your views here.
def calculate(request):
    result = None
    if request.method == 'POST':
        operation = request.POST['operation']
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])

        if operation == 'add':
            result = num1+num2
        elif operation == 'sub':
            result = num1-num2
        elif operation == 'mul':
            result = num1*num2
        elif operation == 'div':
            if num2 !=0:
                result = num1/num2
            else:
                result = 'ERROR'
    return render(request, 'calculator/index.html',{'result': result})

