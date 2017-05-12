from setuptools import setup, find_packages

setup(
    name='biased-stop-words',
    version='2017.5.12.1',
    description='Generates biased stop word lists for various genres',
    long_description=open('README.rst').read(),
    url='https://github.com/gregology/python-biased-stop-words',
    author='Greg Clarke',
    author_email='greg@gho.st',
    license='MIT',
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
     'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    ],
    keywords='stopwords data bias',
    packages=find_packages(),
    install_requires=['pyyaml'],
    package_data={
        'biased_stop_words': [
            'biased-stop-words/*.txt',
            'biased-stop-words/mapping.yaml'
        ]
    }
)
