from setuptools import setup


DESCRIPTION = "myopy, run blind python files."

try:
    with open("README.md") as fh:
        LONG_DESCRIPTION = fh.read()
except UnicodeDecodeError:
    LONG_DESCRIPTION = ""

setup(name='myopy',
      author='Loic Coyle',
      author_email='loic.coyle@hotmail.fr',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      packages=['myopy'],
      install_requires=[],
      python_requires='>=3.6',
      setup_requires=['setuptools_scm'],
      use_scm_version=True,
      )
