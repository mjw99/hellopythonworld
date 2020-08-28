from setuptools import setup

# Also see
# https://packaging.python.org/tutorials/packaging-projects/

setup(
   name='hellopythonworld',
   version='1.0',
   description='An example test module',
   author='Mark Williamson',
   author_email='mjw@mjw.name',
   packages=['hellopythonworld'],  #same as name
   install_requires=[], #external packages as dependencies
)
