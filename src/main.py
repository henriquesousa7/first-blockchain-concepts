from blchain import Blockchain

if __name__ == '__main__':
  
  blchain = Blockchain()

  blchain.add_block('First block')
  blchain.add_block('Second block')
  blchain.add_block('Third block')

  print(blchain.get_all())
