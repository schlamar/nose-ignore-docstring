# coding: utf-8

from setuptools import setup


def get_version(fname='nose_ignoredoc.py'):
    f = open(fname)
    try:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])
    finally:
        f.close()


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        f = open(fname)
        try:
            descr.append(f.read())
        finally:
            f.close()
    return '\n\n'.join(descr)


setup(
    name='nose-ignore-docstring',
    version=get_version(),
    description='Ignore docstring to name tests in nose.',
    long_description=get_long_description(),
    keywords='nose testing',
    author='Marc Schlaich',
    author_email='marc.schlaich@gmail.com',
    url='https://github.com/schlamar/nose-ignore-docstring',
    license='MIT',
    py_modules=['nose_ignoredoc'],
    zip_safe=False,
    entry_points={
        'nose.plugins': [
            'nose_ignoredoc = nose_ignoredoc:IgnoreDocstrings',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
