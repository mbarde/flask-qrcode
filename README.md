# QR-Code generator with web UI

This is a QR-generator service you can host on your own machine.

Basically its a [Flask server](https://www.palletsprojects.com/p/flask/) wrapped around this [QR code image generator](https://pypi.org/project/qrcode/) providing an easy-to-use web UI (and an API) to generate QR-codes.

*Hint: QR-Codes are cached in folder  `codes`. In production you should deploy a proper clean-up mechanism here ;)*

## Frontend

![Screenshot_2023-10-24_09-08-15](https://github.com/mbarde/flask-qrcode/assets/4497578/4ed4fbda-831f-4a6c-8fc9-d674b3c5d603)

## API

Example: `http://localhost:5000?url=https://mbarde.de&boxsize=50`

Expected parameters:

* `url`: URL to "qr-encode"
* `size` (optional): Size (width & height) of resulting QR code image
* `boxsize` (optional): Size of single box of the QR code (when `size` is set as well, this is the size of each box *before* image gets resized)
* `fill` (optional): Hex code for fill color (without `#`)
* `back` (optional): Hex code for background color (without `#`)

## Setup & run

Within your [virtual environment](https://docs.python.org/3/tutorial/venv.html):
```
pip install -r requirements.txt
env FLASK_APP=server.py flask run --host=0.0.0.0
```

Access via http://localhost:5000/

## Serve with `waitress`

In production enviroments I suggest serving the application via [waitress](https://flask.palletsprojects.com/en/2.3.x/deploying/waitress/):

```
pip install waitress
waitress-serve --port=5000 --call "server:create_app"`
```
