Simple Flask server which delivers QR codes for URLs (expects GET/POST parameter `url`).

QR-Codes are cached in folder  `codes`. In production you should deploy a proper clean-up method here ;)

Expected paramters:

* url: URL to "qr-encode"
* size (optional): Size (width & height) of resulting QR code image
* boxsize (optional): Size of single box of the QR code (when `size` is set as well, this is the size of each box *before* image gets resized)


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
