import setuptools 

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='textprome',
version='1.0',
description='Generate image from text with visual effects ',
long_description=long_description,
long_description_content_type="text/markdown",
url='https://github.com/jeremia49/TextPro.me',
author='jeremia49',
author_email='jeremia49@asia.com',
license='MIT',
packages=['textprome',
		 'tests',
		 'examples'],
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
zip_safe=True,
python_requires='>=3.5',
install_requires=[
        'bs4',
        'requests',
        'lxml'
]
)