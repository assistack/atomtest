from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
def main( request ):

    # template = loader.get_template("atom.html")
    return render( request, 'atom.html', )
