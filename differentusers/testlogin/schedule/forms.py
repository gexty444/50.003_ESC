from django import forms
from schedule.models import Schedule
from loginpage.models import User
import datetime as dt

HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]

class CreateSchedule(forms.ModelForm):

    lecturer = forms.ModelChoiceField(queryset=User.objects.all()) # TODO: change to Professor model in future
    
    class Meta:
        model = Schedule
        fields = ['title','description','start_time','end_time', 'lecturer', 'location']
        widgets = {'start_time': forms.Select(choices=HOUR_CHOICES),
        'end_time':forms.Select(choices=HOUR_CHOICES)
        }