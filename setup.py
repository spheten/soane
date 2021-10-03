'''
Pypi packaging script.
'''

from setuptools import setup, find_packages

from soane import VERSION_NUMBER

setup(
    name = 'soane',
    url  = 'https://github.com/spheten/soane',
    version = VERSION_NUMBER,

    author       = 'Stephen Malone',
    author_email = 'soane@example.com',

    description      = 'Stephen\'s Old-Ass Note Engine.',
    long_description = open('readme.md', 'r').read(),
    long_description_content_type = 'text/markdown',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Topic :: Terminals',
        'Topic :: Text Processing',
    ],

    keywords = 'cli, command-line, note, notes, note manager',
    packages = find_packages(),
    python_requires  = '>=3.9',
    install_requires = ['click>=8.0.1'],
    extras_require   = {'test': ['pytest>=6.2.2']},
    data_files       = ['changes.md', 'license.md', 'readme.md'],
    entry_points     = {'console_scripts': ['soane=soane.__main__:main']},

    project_urls = {
        'Repository':     'https://github.com/spheten/soane',
        'Bug Tracker':    'https://github.com/spheten/soane/issues',
        'Latest Release': 'https://github.com/spheten/soane/releases/latest',
    },
)
