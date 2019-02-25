import base64, platform, subprocess, os, sys

filePath = sys.argv[1]
fileName = sys.argv[2]


with open(filePath, 'rb') as f:
    byteArray = f.read()

enc_byteArray = base64.b64encode(byteArray)

with open(fileName + '.py', 'w') as f:
    f.write('#cython: language_level=3\n')
    if fileName  == 'features':
        f.write('enc_features = ' + str(enc_byteArray))
    elif fileName == 'num_previous':
        f.write('enc_num_previous = ' + str(enc_byteArray))
    else:
        f.write('enc_model = ' + str(enc_byteArray))
            
    f.close()
