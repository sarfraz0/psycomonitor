from setuptools import setup

setup(name='psycomonitor',
      version='0.1.0.1',
      author='Sarfraz Kapasi',
      author_email='sarfraz@variablentreprise.com',
      license='GPL-3',
      packages=[
          'psycomonitor'
      ],
      install_requires=[
          'sqlalchemy',
          'psycopg2',
          'celery'
      ],
      include_package_data=True,
      zip_safe=False)
