from setuptools import setup

version = __import__("src").get_version()

setup(
    name="django_asserts",
    version=version,
    description="Helpers for testing Django using context managers",
    author="Kalinin Mitko",
    author_email="kalinin.mitko@gmail.com",
    url="https://github.com/null-none/django-asserts",
    license="MIT",
    packages=["src"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "lxml",
        "cssselect",  # split out of lxml.cssselect in v3.0
    ],
)
