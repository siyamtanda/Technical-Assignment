from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.gis.geos import Point
from django.urls import reverse_lazy

from .models import CustomUser

def user_profile(request):
    user = request.user
    return render(request, 'profiles/user_profile.html', {'user': user})

class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'email', 'home_address', 'phone_number', 'location']
    template_name_suffix = '_update_form'

    def get_object(self, queryset=None):
        return self.request.user.customuser

    def form_valid(self, form):
        form.instance.location = Point(float(self.request.POST['longitude']), float(self.request.POST['latitude']))
        return super().form_valid(form)

@login_required
def map_view(request):
    users = CustomUser.objects.exclude(location=None)
    return render(request, 'profiles/map.html', {'users': users})

# Create your views here.
