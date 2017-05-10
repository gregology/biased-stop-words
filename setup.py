from setuptools import setup, find_packages

setup(
    name='biased-stop-words',
    version=__import__('biased_stop_words').get_version(),
    description='Generates biased stop word lists',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    author='Greg Clarke',
    author_email='greg@gho.st',
    url='https://github.com/gregology/python-biased-stop-words',
    packages=find_packages(),
    package_data={
        'biased_stop_words': [
            'biased-stop-words/*.txt',
            'biased-stop-words/mapping.yaml'
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
