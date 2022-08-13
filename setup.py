from setuptools import setup, find_packages
from glob import glob


setup(
    name='django_admin_button',
    version='0.2.0',
    license='MIT',
    author="Mina Atef",
    author_email='mina.atef0@gmail.com',
    packages=['django_admin_button','django_admin_button.templates','django_admin_button.static'],
        data_files = [
        ('templates', glob('templates/*')), # files in source_dir only - not recursive
        ('static', glob('static/*')), # includes sub-folders - recursive
        # etc...
    ],

    url='https://github.com/minaaaatef/Django-Admin-Buttons',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],


)