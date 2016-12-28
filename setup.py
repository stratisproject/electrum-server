from setuptools import setup

setup(
    name="electrum-stratis-server",
    version="1.0",
    scripts=['run_electrum_stratis_server.py','electrum-stratis-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumstratisserver':'src'
        },
    py_modules=[
        'electrumstratisserver.__init__',
        'electrumstratisserver.utils',
        'electrumstratisserver.storage',
        'electrumstratisserver.deserialize',
        'electrumstratisserver.networks',
        'electrumstratisserver.blockchain_processor',
        'electrumstratisserver.server_processor',
        'electrumstratisserver.processor',
        'electrumstratisserver.version',
        'electrumstratisserver.ircthread',
        'electrumstratisserver.stratum_tcp'
    ],
    description="Stratis Electrum Server",
    author="dev0tion",
    license="MIT Licence",
    url="https://github.com/dev0tion/electrum-stratis-server/",
    long_description="""Server for the Electrum Lightweight Stratis Wallet"""
)
