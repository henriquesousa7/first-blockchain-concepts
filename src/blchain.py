from hashlib import sha256
from datetime import datetime

class Blockchain:

  def __init__(self):
    self.blocks = []
    self.set_genesis_block()

  def set_genesis_block(self):
    data = 'Init block'
    time = datetime.utcnow().timestamp()
    prev_hash = 0
    index = 0
    self.hash_block(data, time, prev_hash, index)

  def hash_block(self, data, time, prev_hash, index):
    hash = ''
    nonce = 1

    while not self.hash_valid(hash):
      block = f'{data}:{time}:{prev_hash}:{index}:{nonce}'
      hash = sha256(block.encode()).hexdigest()
      nonce += 1

    #print('Nonce: ', nonce)
    self.blocks.append(hash)

  def hash_valid(self, hash):
    return hash.startswith('0000')

  def get_last_blockhash(self):
    return self.blocks[-1]

  def add_block(self, data):
    index = len(self.blocks)
    prev_hash = self.get_last_blockhash()
    time = datetime.utcnow().timestamp()
    
    self.hash_block(data, time, prev_hash, index)

  def get_all(self):
    return self.blocks
