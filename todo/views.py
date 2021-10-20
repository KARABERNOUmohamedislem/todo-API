import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib import messages
from .models import Todo
from .serializer import TodoSerializer


# Create your views here.


@api_view(['GET'])
def getTodos(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUrgentTodos(request):
    queryset = Todo.objects.filter(priority=3)
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTodayTodos(request):
    today = datetime.date.today()
    queryset = Todo.objects.filter(dueDateTime=today)
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCompletedTodos(request):
    queryset = Todo.objects.filter(done=True)
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def setDone(request):
    _id = request.data['id']
    _done = request.data['done']
    try:
        todo = Todo.objects.get(pk=_id)
        todo.done = _done
        todo.save()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response()


@api_view(['POST'])
def createOrUpdateTodo(request):
    _id = request.data['id']
    todoType = request.data['type']
    if not _id:
        _id = Todo.pk
    todoDueDateTime = datetime.datetime.now()
    # 'daily', 'weekly', 'monthly', 'yearly')
    if todoType == 'daily':
        todoDueDateTime = todoDueDateTime.__add__(datetime.date(0, 0, 1))
    elif todoType == 'weekly':
        todoDueDateTime = todoDueDateTime.__add__(datetime.date(0, 0, 7))
    elif todoType == 'monthly':
        todoDueDateTime = todoDueDateTime.__add__(datetime.date(0, 1, 0))
    elif todoType == 'yearly':
        todoDueDateTime = todoDueDateTime.__add__(datetime.date(1, 0, 0))
    try:
        newtodo = Todo.objects.update_or_create(pk=_id,
                                                title=request.data['title'],
                                                priority=request.data['priority'],
                                                type=request.data['type'],
                                                dueDateTime=todoDueDateTime,
                                                done=request.data['done']
                                                )
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response()


@api_view(['DELETE'])
def deleteTodo(request):
    _id = request.data['id']
    try:
        todo = Todo.objects.get(pk=_id)
        todo.delete()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response()
