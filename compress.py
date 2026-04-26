import zlib
import base64

data = open('demo.txt', 'r').read()

data_bytes = bytes(data, 'utf-8')

compressed = base64.b64encode(zlib.compress(data_bytes,9))
decoded = compressed.decode('utf-8')
file = open('compressed.txt', 'w')
file.write(decoded)
