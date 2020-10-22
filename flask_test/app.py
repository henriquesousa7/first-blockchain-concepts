from flask import Flask, jsonify
import sys
sys.path.insert(0,'../src')
from blchain import Blockchain

app = Flask(__name__)

@app.route('/blchain', methods=['GET'])
def get_chain():
   
  data = blchain.get_all()
  
  return jsonify(data)


@app.route('/createblock/<data>', methods=['GET'])
def cresteBlock(data):

  try:

    blchain.add_block(data)
  
  except Exception as e:

    return e

  return 'Success'

if __name__ == '__main__':
  blchain = Blockchain()
  app.run(debug=True, port=5000)
