import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-collectmessages',
    version='0.1',
    packages=['collectmessages'],
    include_package_data=True,
    license='BSD License',
    description='Collect translated messages from other applications.',
    long_description=README,
    url='https://github.com/UGentPortaal/django-collectmessages',
    author='UGent Portaalteam',
    author_email='portaal@ugent.be',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
    install_requires=["django", "polib"],
)
