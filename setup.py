import setuptools

setuptools.setup(
    name='coinmarketcap_scrape_top',
    version='2.2.0',
    packages=['coinmarketcap_scrape_top',],
    license='MIT',
    description = 'Python3 wrapper around the CoinMarketCap',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Kuanysh Mansurov',
    author_email = 'kukakukakuka2017@mail.ru',
    install_requires=['requests'],
    url = 'https://github.com/kuka666/coinmarketcap_scrape_top.git',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )
