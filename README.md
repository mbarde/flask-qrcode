Simple Flask server which delivers QR-Codes for URLs (expects GET/POST parameter `url`).

QR-Codes are cached in folder  `codes`.


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
