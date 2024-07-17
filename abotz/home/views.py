from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

#def custom_404(request, exception):
#   return render(request, 'home/error.html', {'message': 'The page you are looking for does not exist.'}, status=404)

#def custom_500(request):
#    return render(request, 'home/error.html', {'message': 'An internal server error occurred.'}, status=500)

#def custom_403(request, exception):
#    return render(request, 'home/error.html', {'message': 'You do not have permission to access this page.'}, status=403)

