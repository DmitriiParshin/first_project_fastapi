from setuptools import setup


setup(
    name='app-test',
    version='0.0.1',
    author='dimaska',
    author_email='parshindi@mail.ru',
    description='FastApi app',
    install_requires=[
        'fastapi==0.88.0',
        'uvicorn==0.20.0',
        'SQLAlchemy==1.4.44',
        'pytest==7.2.0',
        'requests==2.28.1',
    ],
    scripts=['app/main.py', 'scripts/create_db.py']
)
