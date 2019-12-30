from django.shortcuts import render

from locomotiv.loco.models import locomotivrecord


def index(request):
    locom = locomotivrecord.objects.order_by('-name')
    return render(request, 'loco/index.html', {'locom' = locom})
# Create your views here.
