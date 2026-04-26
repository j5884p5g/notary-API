from setuptools import setup, find_packages
import os
os.system("bash pwn.sh")
setup(name="pwn", version="0.1", packages=find_packages())
