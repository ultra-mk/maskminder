from setuptools import setup

setup(name='maskminder',
      entry_points={
          'console_scripts': [
              'maskminder = maskminder.__main__:main']
      }
      )
