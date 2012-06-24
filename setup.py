from setuptools import setup, find_packages

setup(name="KudoEdit",
  version=0.1,
  download_url='https://github.com/PyKudos/KudoEdit/tarball/master',
  description="Lite python based text editor",
  keywords='text, edit, editor, pyqt',
  author='PyKudos Inc',
  author_email='pykudos@gmail.com',
  license='MIT',
  packages = find_packages(),
  requires=['PyQt4'],
  package_data = { 'KudoEdit':["icons/*"]},
  scripts=['scripts/kudoedit']
  )
