trampolinnternship
==================

Small Test Project (14 hours work) to get my internship in Barcelona. ¡ Arriba !

==================

A unique webpage trip-themed with a form and a parser to test one's ability to learn and code.

### Techs ###
- Unix (os X Mavericks)
- Apache
- MySQL
- Python (Django) 2.7 / ! \
- Web (HTML - CSS)

### Requirements ###

### I worked on the school computers. We do not have access to super users, the Library nor Applications folders, and have to find workarounds for many very simple tasks.
Officially we should use bitnami djangostack, and I started working on it, then switched to a virtual machine with kubuntu. I then placed the project back in os X Mavericks and tested it locally with the python manage.py runserver command. ###


### Though it SHOULD run smoothly with apache and mod-wsgi on os X Mavericks, I haven't fully tested it. ###

#Install:
sudo pip install
    django-bootstrap3
    django_admin_bootstrapped
    libapache2-mod-wsgi
    mysql-python ( ... )

#I chose to use online pictures, so the .tar would not be too large
#in any folder
tar xf internship.tar

#Running:
#create an alias manage="python manage.py"

manage createsuperuser
#hint: there is already a demo user set (name demo, pwd demo), but feel free to create your own account
manage syncdb

### What you need to do ###

Test the konami Code !

Then, if you wish so, add an adress email (spambot free guaranteed),
or many !

/ ! \ to upload a file, I use data() (line 13 in landingpage/views.py) -> if you are using python 3.x, this line must be changed to data.decode() / ! \


### Acknowledgement ###

First of all, Gabrielle Taylor for the Lemonade Grenade http://creator.wonderhowto.com/gabrielletaylor/
I still have placement problems with some of the most inner css, but the overall is good.
StackOverflow && Django Doc && the developer.mozilla.org references && the famous Google Chrome > inspect element console.
jshkurti && agreau for proofreading, help with brew and pip and apache when __you cannot sudo their ass off__, and the innumerable free coffees.
I freely used bootstrap sticky footer css; anything else is mine.
I adapted the javascript for the bonus Konami Code from a script from Mizur.