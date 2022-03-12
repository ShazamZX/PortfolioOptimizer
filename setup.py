from setuptools import setup
setup(name='optimustock',
      version='1.0',
      description='Portfolio Calculator',
      author='Sanchar Banerjee, Molla Shitab Tanzim',
      packages=['optimustock'],
      install_requires= ['pandas','numpy','scipy','datetime','pandas-datareader','json']
     )