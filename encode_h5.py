import base64, sys

filePath = sys.argv[1]
fileName = sys.argv[2]

with open(filePath, 'rb') as f:
    byteArray = f.read()

enc_byteArray = base64.b64encode(byteArray)

with open(fileName + '.py', 'w') as f:
    f.write('#cython: language_level=3\n')
    f.write('enc_model = ' + str(enc_byteArray))
    f.close()
