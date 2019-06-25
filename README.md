# ams-project
Accreditation Management System for HEIs. Programmed with Python, Django framework and SQLite

How to setup AMS
1. Download python and django
2. Open cmd or terminal
3. Set up your virtual environment or venv
4. Go to the ams-project folder
5. Run 'python manage.py runserver'

How to edit screens/htmls
1. Go to the corresponding templates folder
2. Edit the html file

How to add new screens to urls and views
1. Add the new html to the corresponding templates folder
2. Open the corresponding views.py in the app
3. Create the view function<br>
    def <i>functionname</i>(request):<br>
	    &nbsp;&nbsp;&nbsp;&nbsp;return render(request, '<i>appname</i>/htmlfile.html')
4. Add the view function to urlspath in urls.py<br>
    1. Add an import:  <i>from . import views</i>
    2.  Add a URL to urlpatterns:  <i>path('pathname/', views.functionname, name='home')</i>
