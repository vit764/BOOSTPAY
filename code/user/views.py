from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from orders.models import ProductInOrder
from user.models import Requisite, Dialog
from user.forms import AskForm


def displayOrders(request):
    if request.user.is_authenticated:
        context = {
            'orders': ProductInOrder.objects.filter(order__user__username=request.user.username),
            'requisites': Requisite.objects.all(),

        }

        return render(request, 'user/my_orders.html', context)
    else:
        return redirect("/login/")


def askQuestion(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = AskForm(request.POST)
            if form.is_valid():
                data = request.POST

                question = data["question"]
                #question = form.cleaned_data['question']
                print(question)
                if question:
                    print("save")
                    Dialog.objects.filter(user=request.user).delete()
                    dialog = Dialog.objects.create(user=request.user, user_meessage=question)
                    dialog.save()

                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            context = {
                 'dialogs': Dialog.objects.filter(user=request.user),
            }

        return render(request, 'user/ack.html', context)
    else:
        return redirect("/login/")


def askkQuestion(request):
    if request.user.is_authenticated:
        form = AskForm(request.POST or None)
        if form.is_valid():

            if request.POST:
                question = form.question
                print(question)
                # phone = data["phone"]

                Dialog.objects.filter(user=request.user).delete()
                dialog = Dialog.objects.create(user=request.user, user_meessage=question)
                dialog.save()

                context = {
                    'dialog':  Dialog.objects.filter(user=request.user),

                    }
                return render(request, 'user/ask.html', context)
    else:
        return redirect("/login/")


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "user/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "user/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
