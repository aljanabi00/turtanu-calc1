from django.http import JsonResponse


def calc(num1, num2, op):
    num1 = int(num1)
    num2 = int(num2)
    if op == 'sum':
        return num1 + num2
    elif op == 'sub':
        return num1 - num2
    elif op == 'mul':
        return num1 * num2
    elif op == 'div':
        if num2 == 0:
            return "cant divide by zero"
        return num1 / num2


def index(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    op = request.GET.get('op')
    return JsonResponse({
        "result": calc(num1, num2, op),
    })
