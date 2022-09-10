Django-Admin-Buttons
====================

This package used to add a button functionality to the change list
columns in the django admin, it uses the action methods used in the
**ModelAdmin**\ 

I wrote this package as an implementation for this article, it not hard
to write the button yourself

Getting Started
---------------

1. Install the app

::

   pip install django-admin-buttons

2. Add the app to the **INSTALLED_APPS** above the admin and static apps

.. code::


   INSTALLED_APPS = [
       'django_admin_buttons', # add here

       'django.contrib.admin',
       'django.contrib.staticfiles',

3. Use the button as needed

.. code::

   from django.contrib import admin
   from django_admin_buttons.admin_button import AdminActionButton


   def Test_function(modeladmin, request, queryset):
       # write you implementation here
       pass 

   class AdminTest(admin.ModelAdmin):
       # add the button 
       list_display = ('id', 'name', 'button') 
       
       # register the function
       actions = [Test_function] 
       
       # create the function that displays the button
       @admin.display()
       def button(self, obj):
           return AdminActionButton(obj.id, 'this', disabled = False, Class='btn-primary', label=None).render()
