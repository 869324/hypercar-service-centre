from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        task = request.POST.get("todo")
        status = request.POST.get("important")
        if task not in self.all_todos:
            if status == "true":
                self.all_todos.insert(0, task)
            else:
                self.all_todos.append(task)
        return redirect("/")
