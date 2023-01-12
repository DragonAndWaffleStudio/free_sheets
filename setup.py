from setuptools import setup

setup(name='free_sheets',
      version='1.0.0',
      description='Steal sheets from musescore',
      author='DragonAndWaffleStudio',
      author_email='pyprogrammer199@gmail.com',
      url='https://github.com/DragonAndWaffleStudio/free_sheets',
      packages=['free_sheets'],
      entry_points={
          'console_scripts': [
              'free_sheets = free_sheets.command_line:main',
          ]
      },
      install_requires=['cairosvg',
                        'selenium',
                        'PyPDF2',
      ],
      include_package_data=True,
      zip_safe=False
     )
