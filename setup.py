from setuptools import setup

setup(
    name='biased-stop-words',
    version='2017.5.11.2',
    description='Generates biased stop word lists for various genres',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    author='Greg Clarke',
    author_email='greg@gho.st',
    url='https://github.com/gregology/python-biased-stop-words',
    packages=['biased_stop_words'],
    package_data={
        'biased_stop_words': [
            'biased-stop-words/*.txt',
            'biased-stop-words/mapping.yaml'
        ]
    }
)
