from distutils.core import setup

setup(
  name='RolePlay',
  version='0.1',
  packages=['roleplay','roleplay.scanner','roleplay.director'],
  license='MIT',
  install_requires=[
    "PyPNG >= 0.0.15"
  ],
)