import base64

h5_name = 'lstmModel'

with open('h5/' + h5_name + '.h5', 'rb') as f:
    byteArray = f.read()

enc_byteArray = base64.b64encode(byteArray)

with open(h5_name + '.py', 'w') as f:
    f.write('#cython: language_level=3\n')
    f.write('enc_model = ' + str(enc_byteArray))
    f.close()

import subprocess
process = subprocess.Popen('python setup.py ' + h5_name + ' build_ext --inplace', shell=True, stdout=subprocess.PIPE)
process.wait()
if process.returncode == 0:
    print('build pyd success.')
else:
    print('something wrong')


process = subprocess.Popen('rm ' + h5_name + '.py', shell=True, stdout=subprocess.PIPE)
process.wait()
if process.returncode == 0:
    print('delete ' + h5_name + '.py sucess.')
else:
    print('something wrong')

process = subprocess.Popen('rm ' + h5_name + '.c', shell=True, stdout=subprocess.PIPE)
process.wait()
if process.returncode == 0:
    print('delete ' + h5_name + '.c sucess.')
else:
    print('something wrong')


process = subprocess.Popen('mv ' + h5_name + '.cp36-win_amd64.pyd ' + h5_name + '.pyd', shell=True, stdout=subprocess.PIPE)
process.wait()
if process.returncode == 0:
    print('rename ' + h5_name + '.pyd sucess.')
else:
    print('something wrong')


process = subprocess.Popen('mv ' + h5_name + '.pyd web_taipower/py', shell=True, stdout=subprocess.PIPE)
process.wait()
if process.returncode == 0:
    print('move to web_taipower sucess.')
else:
    print('something wrong')