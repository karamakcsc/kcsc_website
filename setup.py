from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kcsc_website/__init__.py
from kcsc_website import __version__ as version

setup(
	name="kcsc_website",
	version=version,
	description="KCSC",
	author="KCSC",
	author_email="info@kcsc.com.jo",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
