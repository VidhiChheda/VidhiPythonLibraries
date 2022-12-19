import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='library2',
    version='0.0.3',
    author='Vidhi Chheda',
    author_email='vidhi@swancapital.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/VidhiChheda/VidhiPythonLibraries/Vidhitoolbox/library2',
    #license='MIT',
    packages=['package2'],
    install_requires=['requests'],
)
