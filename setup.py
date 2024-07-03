from setuptools import setup, find_packages
from glob import glob

description = 'Django Admin Buttons is a simple Django app to add buttons to change list page of Django admin.'

setup(
    name='django_admin_buttons',
    version='0.2.6',
    license='MIT',
    author="Mina Atef",
    author_email='mina.atef0@gmail.com',
    long_description=description,
    packages=['django_admin_buttons','django_admin_buttons.templates','django_admin_buttons.static'],
        data_files = [
        ('templates', glob('templates/*')), # files in source_dir only - not recursive
        ('static', glob('static/*')), # includes sub-folders - recursive
        # etc...
    ],

    url='https://github.com/minaaaatef/Django-Admin-Buttons',
    keywords=('django','buttons','admin','actions'),
    install_requires=[
      ],


)