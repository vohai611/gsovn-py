from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Data from Vietnam General Statistic Organization'
LONG_DESCRIPTION = 'This package allow user to select and download data from https://gso.gov.vn'

setup(
  name='gsovn',
  version=VERSION,
  author="Hai Ngoc Vo",
  author_email="hai835559@gmail.com",
  description=DESCRIPTION,
  long_description=LONG_DESCRIPTION,
  packages=find_packages(),
  install_requires=["pandas>=0.19.2", "requests>=2.3.0", "bs4>=0.0.1"], 
  
  keywords=['python', 'data scraping'],
  classifiers= [
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Education",
      "Programming Language :: Python :: 3",
      "Operating System :: MacOS :: MacOS X",
      "Operating System :: POSIX :: Linux",
  ]
)
