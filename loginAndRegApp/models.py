import bcrypt
from django.db import models
from datetime import datetime


class usersManger(models.Manager):
    def basic_validtor(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(post_data['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if post_data['password'] != post_data['confirm_password']:
            errors["confirm_password"] = "No match password "
        if datetime.today() < datetime.strptime(post_data['b_date'], "%Y-%m-%d"):
            errors["b_date"] = "Birthday Date should be in the past"
        if User.objects.filter(email=post_data['email']).exists():
            errors["email"] = "Already existsed !!!!"
        if validate_date_less_13_Years(post_data):
            errors['b_date'] = "You are under 13 years old , sorry little kid :("
        return errors

    # def basic_validtor_login(self,post_date):
    #     errors={}
    #     if not User.objects.filter(email=post_date['email']).exists():
    #         errors['email']="This email is not exists"
    #     if not bcrypt.checkpw(post_date['password'].encode(), User.objects.filter(email=post_date['email'])[0].password.encode()):
    #         errors['password']="password Wrong"
    #     return errors

def validate_date_less_13_Years(post_data):
    if int(((datetime.today() - datetime.strptime(post_data['b_date'], "%Y-%m-%d")).days)/365) < 13:
        return True
    return False

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    b_date = models.DateField(null=True)

    objects = usersManger()

    def retrive_user_by_id(id):
        return User.objects.get(id=id)

def Register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    b_date = request.POST['b_date']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if (request.POST['confirm_password'] == password):
        return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash, b_date=b_date)

def Login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        loged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), loged_user.password.encode()):
            request.session['userid'] = loged_user.id
            request.session['username']=loged_user.first_name
            return True
        else :
            request.session['LoginAuth'] = "Username or password does not exist"
            return False
    else:
        request.session['LoginAuth'] = "Username or password does not exist"
        return False

