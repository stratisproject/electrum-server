Electrum-stratis-server for the Electrum-Stratis client
=========================================

  * Original Author: Thomas Voegtlin (ThomasV on the bitcointalk forum)
  * Stratis port maintainer: dev0tion
  * Language: Python

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires stratisd, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of Stratis addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-stratis-server' script



License
-------

Electrum-stratis-server is made available under the terms of the MIT License.
See the included `LICENSE` for more details.