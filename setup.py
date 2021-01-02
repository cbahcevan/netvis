from setuptools import setup

setup(
   name='Netvis',
   version='0.1',
   description='D3 based visualization library',
   license="MIT",
   author='Turknet',
   author_email='cenk.bahcevan@turknet.net.tr',
   packages=['turkishsd'],  
   install_requires=['pandas'], 
   test_suite="tests",
   keywords='d3js python visualization',
)