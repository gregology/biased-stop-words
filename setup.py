from setuptools import setup, find_packages

setup(
    name='biased-stop-words',
    version='2017.5.13.2',
    description='Generates biased stop word lists for various genres',
    long_description=open('README.rst').read(),
    url='https://github.com/gregology/biased-stop-words',
    author='Greg Clarke',
    author_email='greg@gho.st',
    license='MIT',
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
    ],
    keywords='stop words machine learning ml bias biased natural language processing nlp',
    packages=find_packages(),
    install_requires=['pyyaml'],
    package_data={
        'biased_stop_words': [
            'biased-words/*.txt',
            'biased-words/stop-word-mapping.yaml'
        ]
    }
)
