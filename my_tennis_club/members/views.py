from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request)) 

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


'''
def testing(request):
  mycars = marcas.objects.all().values()
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
    'firstname': 'Linus',
    'mymembers': mymembers,
    'greeting': 1,       
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
    #'cars': ['Audi', 'Mercedes', 'Porsche']
  'mycars': mycars,
    
  }
  return HttpResponse(template.render(context, request))
  '''


#TESTING TABLA 
'''
def testing(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
'''

#testing mostrar solo columna firsname  
'''
def testing(request):
  mydata = Member.objects.values_list('firstname', flat= True)
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
'''


#Devuelve solo los registros donde firstname es 'Juana'
"""
def testing(request):
  mydata = Member.objects.filter(firstname='Juana').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
"""


''' Buscar donde lastname sea perez y id 4
def testing(request):
  mydata = Member.objects.filter(lastname='Perez', id=4).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
'''


def testing(request):
  mydata = Member.objects.filter(firstname__startswith='m').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))