# coding=utf-8

from setuptools import setup

# https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
setup(
    name='zip_dir',
    version='0.0.1',
    description='A simple function to create zipped folder.',

    # ########################################################################
    #
    # README.rst is generated from README.md:
    #
    # $ pandoc --from=markdown --to=rst README.md -o README.rst
    #
    # ~ OR ~
    #
    # $ fab build
    # ########################################################################
    long_description=(open('README.md').read()),

    url='https://github.com/illagrenan/python-zip-dir',
    license='MIT',
    author='Vašek Dohnal',
    author_email='vaclav.dohnal@gmail.com',

    # The exclude makes sure that a top-level tests package doesn’t get
    # installed (it’s still part of the source distribution)
    # since that would wreak havoc.
    # find_packages(exclude=['tests*'])
    packages=['zip_dir'],


    install_requires=[],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers'
    ],
)