from p2pool.bitcoin import networks

PARENT=networks.nets['vertcoin']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=3 # blocks
IDENTIFIER='a07e81d83ddafd83'.decode('hex')
PREFIX='7c3814fffcdcf988'.decode('hex')
P2P_PORT=9348
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=9191
BOOTSTRAP_ADDRS='p2pool3.vertcoin.org c0de.review 45.76.68.176 45.32.212.220'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-vtc'
VERSION_CHECK=lambda v: True
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16
DUST_THRESHOLD=0.015e8
