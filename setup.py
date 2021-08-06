import os
import re
import setuptools

VERSIONFILE = "./pythondsa/_version.py"
# print(VERSIONFILE)
verstrline = open(VERSIONFILE, "rt").read()
# print(verstrline)
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
# print(mo)
pkg_name = os.getenv("PKG_NAME", "pythondsa")

if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open("README.md", "rb") as fh:
    long_description = fh.read().decode('utf-8', errors='ignore')
    
setuptools.setup(
      name=pkg_name,
      version=verstr,
      author="ayush-vns",
      author_email="ayush.mishra.ald@gmail.com",
      description="DSA Utility Module",
      long_description=long_description,
      packages=setuptools.find_packages(),
      )