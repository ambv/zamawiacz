# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

setup (
    name = 'langacore.zamawiacz',
    version = '0.2.0',
    author = 'Łukasz Langa',
    author_email = 'support@langacore.org',
    description = "Simplistic order management tool.",
    long_description = '',
    keywords = '',
    platforms = ['any'],
    license = 'GPL v3',
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = [],
    zip_safe = True,
    install_requires = [
        'langacore.kit.django',
        'django_evolution',
        ],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )
