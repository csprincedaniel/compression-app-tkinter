import zlib, base64

def compress(inputfile, outputfile):
    data = open(inputfile, 'r').read()

    data_bytes = bytes(data, 'utf-8')

    compressed = base64.b64encode(zlib.compress(data_bytes,9))
    decoded = compressed.decode('utf-8')
    file = open(outputfile, 'w')
    file.write(decoded)
    file.close()

def decompress(inputfile, outputfile):
    file = open(inputfile, 'r').read()
    encoded = file.encode('utf-8')
    decompressed = zlib.decompress(base64.b64decode(encoded))
    final = decompressed.decode('utf-8')
    
    file = open(outputfile, 'w')
    file.write(final)
    file.close()
#compress('demo.txt', 'ot.txt')
#decompress('ot.txt', 'dc1.txt')