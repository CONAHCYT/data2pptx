from setuptools import setup, find_packages

import os
requirementPath = './requirements.txt'
install_requires = [] # Examples: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

otherchars = ["-","'"]
install_requires = [x for x in install_requires if len(x)>0 ]
reqs = [x for x in install_requires if x[0] not in otherchars and x[0] != "#"]
deps = [x for x in install_requires if x[0] in otherchars and x[0] != "#"]
print(reqs,"\n\n\n",deps)

setup(name='data2pptx',
      version='0.0.1',
      description='Allows programatic building of pptx slideshows, using pandas and matplotib objects.',
      author='Coordinación de Ciencia de Datos, MX',
      author_email='victor.mireles@conacyt.mx',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
      install_requires=reqs,
      dependency_links=deps
    )
