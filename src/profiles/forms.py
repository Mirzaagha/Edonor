from django import forms
from .choices import *
from django.contrib.auth import get_user_model
from .models import MyUser


User = get_user_model()


class RegisterForm(forms.ModelForm):
	"""A form for creating new users. Includes all the required
	fields, plus a repeated password."""
	YEARS= [x for x in range(1940,2021)]

	first_name 	 = forms.CharField(label='Adınız', required=True)
	last_name  	 = forms.CharField(label='Soyadınız', required=True)
	password1    = forms.CharField(label='Şifrə', widget=forms.PasswordInput)
	password2    = forms.CharField(label='Şifrəni təsdiqlə', widget=forms.PasswordInput)
	gender       = forms.ChoiceField(label='Cins', choices=GENDER_CHOICES, required=True)
	blood_group  = forms.ChoiceField(label='Qan qrupunuz',choices=BLOOD_GROUP, required=True)
	birth_date 	 = forms.DateField(label='Doğum gününüz',
	 widget=forms.SelectDateWidget(years=YEARS))
	illness  = forms.ChoiceField(
		label='Sarılıq, dəri xəstəliyi, göz xəstəliyi, qanla ve ürəklə bağlı xəstəliklər keçirmisinizmi?',
		 choices=ILLNESS_CHOICES, required=True)

	illness1  = forms.ChoiceField(
		label='6 ay ərzində əməliyyat olunmusunuzmu?( yüngül əməliyyat)',
		 choices=ILLNESS_CHOICES, required=True)

	illness2  = forms.ChoiceField(
		label='Bədəninizdə tato varmı? ( vardırsa elətdirdiyiniz vaxtdan ən azı 1 il keçməlidir.)',
		 choices=ILLNESS_CHOICES, required=True)

	weight = forms.IntegerField(min_value=0, max_value=1000, label='Çəkiniz', required=True)
	# weight = forms.IntegerField(label='Çəkiniz' , required=True)
	height = forms.IntegerField(min_value=0, max_value=300,label='Boyunuz' , required=True)


	last_blood_date= forms.DateField(
		label='Daha əvvəl qan vermisinizsə qan vermə tarixini qeyd edin',
	 widget=forms.SelectDateWidget(years=YEARS))
	


	class Meta:
		model = MyUser
		fields = ('first_name',
		'last_name',
		'username', 
		'email', 
		'gender',
		'blood_group',
		'birth_date',
		'last_blood_date',
		'illness',
		'illness1',
		'illness2',
		'weight',
		'height',
		   )

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("Cannot use this email. It's already registered")
		return email

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(RegisterForm, self).save(commit=True)
		user.set_password(self.cleaned_data["password1"])
		#user.password = "asdfasd"
		user.is_active = True
	   

		if commit:
			user.save()
			# user.profile.send_activation_email()
			# create a new user hash for activating email.
		return user





