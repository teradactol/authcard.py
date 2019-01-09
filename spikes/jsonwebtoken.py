# [SOURCE https://github.com/mpdavis/python-jose/ ]
from jose import jwt
token = jwt.encode({'key': 'value'}, 'secret', algorithm='HS256')
print(token)
decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
print(decoded)