from setuptools import setup, find_packages


with open('README.rst') as file:
    long_description = file.read()


setup(
    name='wagtail3-robots',
    long_description=long_description,
    version="0.1.2",
    description='Robots.txt exclusion for Wagtail, complementing Sitemaps.',
    author='dmitriy3342',
    author_email='dmitriy3342@mail.ru',
    url='https://github.com/dmitriy3342/wagtail-robots',
    packages=find_packages(),
    package_data={
        'robots': [
            'templates/robots/*.html',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 3.0',
    ]
)
