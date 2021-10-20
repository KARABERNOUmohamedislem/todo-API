from django.urls import path
from .views import (getTodayTodos,
                    getTodos,
                    getUrgentTodos,
                    getCompletedTodos,
                    setDone,
                    createOrUpdateTodo,
                    deleteTodo,
                    )

urlpatterns = [
    path('/today', getTodayTodos),
    path('/all', getTodos),
    path('/urgent', getUrgentTodos),
    path('/done', getCompletedTodos),
    path('/setDone', setDone),
    path('/create_or_update', createOrUpdateTodo),
    path('/delete', deleteTodo),
]
