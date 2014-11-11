from setuptools import setup

setup(name='google-cli',
      version='0.0',
      py_modules=['google'],
      install_requires=[
          'click',
      ],
      entry_points='''
          [console_scripts]
          google=google:cli
      ''')
