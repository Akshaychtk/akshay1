from django.forms import ModelForm
from . models import Newuser_details
class work(ModelForm):
    class Meta:
        model = Newuser_details
        fields = '__all__'