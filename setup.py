from setuptools import setup

setup(name='daemon-loop',
      version='0.0.1',
      description='simple CLI utility to run other programs periodically as daemon without cron',
      url='https://github.com/yaroslaff/daemon-loop',
      author='Yaroslav Polyakov',
      author_email='yaroslaff@gmail.com',
      license='MIT',
      scripts=['bin/loop'],

      long_description = read('README.md'),
      long_description_content_type='text/markdown',

      install_requires=['python-daemon'],
      zip_safe=False
      )

