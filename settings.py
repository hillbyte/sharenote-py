# API Key set in Share Note plugin settings
# set to something random like: head /dev/urandom | md5sum
SECRET_API_KEY = 'e28616cde774ed5199764d0b9b27768a'

# This API server's URL without a trailing slash
# Some examples might be:
#     SERVER_URL = 'https://notes.example.com'
#     SERVER_URL = 'http://123.123.123.123:8086'
#     SERVER_URL = 'http://something.local:8086'
SERVER_URL = 'http://lgg0gwcgw8gwg8cs8k4cccg0.152.67.167.99.sslip.io'

# Listen port
PORT = 8086

# File types allowed to be uploaded
# Copied from the Share Note API source code
ALLOWED_FILETYPES = [
    'html',
    'css',
    'jpg',
    'jpeg',
    'png',
    'webp',
    'svg',
    'gif',
    'webm',
    'ttf',
    'otf',
    'woff',
    'woff2'
]
