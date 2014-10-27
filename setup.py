import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='AoikUrlToFile',

    version='0.1.0',

    description="""A command to create Windows ".url" file. And tips on how to use it to save URL in Chrome or Iron's location bar to a ".url" file in one hotkey.""",
    
    long_description="""`Documentation on Github 
<https://github.com/AoiKuiyuyou/AoikUrlToFile>`_""",

    url='https://github.com/AoiKuiyuyou/AoikUrlToFile',

    author='Aoi.Kuiyuyou',
    
    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='Chrome Iron location bar save Windows url file hotkey',
      
    package_dir={'':'src'},
    
    packages=find_packages('src'),

    entry_points={
        'console_scripts': [
            'aoikutf=aoikurltofile.aoikurltofile_:main',
        ],
    },
)
