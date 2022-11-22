# we're going to do some deterministic wallet stuff here

# requirements
# pip install hdwallet
# https://github.com/meherett/python-hdwallet
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
from decouple import config
