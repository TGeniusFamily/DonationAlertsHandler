from distutils.core import setup

setup(name='DonationAlertsHandler',
      version='1.0',
      description='Donation Alerts Handler',
      author='bezumnui',
      author_email='bezumnui.mistikgt@gmail.com',
      url='https://github.com/TGeniusFamily/DonationAlertsHandler',
      packages=['distutils', 'distutils.command'],
      requires=[
          "aiohttp"
      ]
      )
