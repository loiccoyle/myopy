from setuptools import setup


DESCRIPTION = "myopy, run blind python files."

with open("README.md") as fh:
    LONG_DESCRIPTION = fh.read()

setup(name='myopy',
      author='Loic Coyle',
      author_email='loic.coyle@hotmail.fr',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown"
      url="https://github.com/loiccoyle/myopy"
      packages=['myopy'],
      python_requires='>=3.6',
      )
