from django.shortcuts import redirect, Http404
from django.views import View


class TodoView(View):
    all_todos = []

    def delete(self, request, todo, *args, **kwargs):
        if todo not
        self.all_todos.remove(todo)
        return redirect('/') if todo in self.all_todos else Http404
