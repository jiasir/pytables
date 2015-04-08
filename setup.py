import sys
import os
import shutil

try:
    from setuptools import setup, find_packages
except ImportError:
    print("pytables now needs setuptools in order to build. Install it using"
          " your package manager (usually python-setuptools) or via pip (pip"
          " install setuptools).")
    sys.exit(1)

setup(name='pytables',
      version='0.1.1',
      description='Deny IPs from Queues',
      author='jiasir',
      author_email='jiasir@icloud.com',
      url='https://github.com/jiasir/pytables/',
      license='MIT License',
      install_requires=['pika == 0.9.8'],
      packages=find_packages(),
      scripts=[
          'bin/pytables',
      ],
      data_files=[],)
os.mkdir('/etc/pytables')
shutil.copy('etc/pytables.conf', '/etc/pytables/pytables.conf')