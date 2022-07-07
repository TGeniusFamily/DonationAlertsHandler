from distutils.core import setup

from setuptools import find_packages
setup(name='donation_alerts_handler',
      version='1.2.0',
      description='Donation Alerts Handler',
      author='bezumnui',
      author_email='bezumnui.mistikgt@gmail.com',
      url='https://github.com/TGeniusFamily/DonationAlertsHandler',
      requires=[
          "aiohttp"
      ],
      packages=find_packages("src"),
      package_dir={'': 'src'},

      )
