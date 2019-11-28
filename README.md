# QR-Code generation server

Nothing magical here, just a [Flask server](https://www.palletsprojects.com/p/flask/) wrapped around a [QR code image generator](https://pypi.org/project/qrcode/) to generate QR codes images representing URLs.

QR-Codes are cached in folder  `codes`. In production you should deploy a proper clean-up mechanism here ;)

Expected parameters:

* `url`: URL to "qr-encode"
* `size` (optional): Size (width & height) of resulting QR code image
* `boxsize` (optional): Size of single box of the QR code (when `size` is set as well, this is the size of each box *before* image gets resized)


## Setup & run

Within your virtual environment:
```
pip install -r requirements.txt
env FLASK_APP=server.py flask run --host=0.0.0.0
```


## Serve with `waitress`

```
pip install waitress
waitress-serve --port=5000 --call "server:create_app"`
```
