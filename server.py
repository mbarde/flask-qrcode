# -*- coding: utf-8 -*-
from flask import abort
from flask import Flask
from flask import request
from flask import send_file
from os import mkdir
from os import path


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        url = request.args.get('url', '')
        if len(url) == 0:
            abort(400)

        codesFolder = 'codes'
        if not path.exists(codesFolder):
            mkdir(codesFolder)

        filename = normalizeFilename(url)
        fullFilename = '{0}/{1}.png'.format(codesFolder, filename)
        if not path.exists(fullFilename):
            import qrcode
            img = qrcode.make(url)
            img.save(fullFilename)

        return send_file(fullFilename)

    def normalizeFilename(s):
        # https://gist.github.com/seanh/93666
        import string
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in s if c in valid_chars)
        filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
        return filename

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
