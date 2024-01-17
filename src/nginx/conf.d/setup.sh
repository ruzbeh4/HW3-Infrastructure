sudo apk add --update --no-cache python3
pip install python-decouple
pip install python-nginx
python3 setup.py
nginx -g 'daemon off';