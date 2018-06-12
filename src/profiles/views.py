from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, CreateView
from django.http import Http404
from .forms import RegisterForm
from .models import MyUser
# from django.contrib.messages.views import SuccessMessageMixin


User = get_user_model()

# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration.html'
    success_url = '/'
    # success_message = "Your account was created successfully. Please check your email."

    def dispatch(self, *args, **kwargs):
        # if self.request.user.is_authenticated():
        #     return redirect("/logout")
        return super(RegisterView, self).dispatch(*args, **kwargs)

# class LoginView(CreateView):
#     form_class = LoginForm
#     template_name = 'login.html'
#     success_url = 'index.html'
#     # success_message = "Your account was created successfully. Please check your email."

#     def dispatch(self, *args, **kwargs):
#         # if self.request.user.is_authenticated():
#         #     return redirect("/logout")
#         return super(LoginView, self).dispatch(*args, **kwargs)




class ProfileDetailView(DetailView):
	template_name = 'profiles/user.html'

	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		user = context['user']
