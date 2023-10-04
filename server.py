# -*- coding: utf-8 -*-
from flask import abort
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import send_from_directory
from os import mkdir
from os import path
from PIL.Image import LANCZOS

import qrcode


def create_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/gen')
    def index():
        url = getURL()
        if url is False:
            return render_template(
                'index.html',
                title='Create QR-Codes',
            )
        boxSize = getIntegerParameter('boxsize', 10, 1, 100)
        size = getIntegerParameter('size', False, 10, 1000)

        codesFolderName = 'codes'
        initCodesFolder(codesFolderName)
        filename = generateFilename(codesFolderName, url, size, boxSize)

        if not path.exists(filename):
            img = generateQRCodeImage(url, size, boxSize)
            img.save(filename)

        return send_file(filename)

    def getURL():
        url = request.args.get('url', '')
        if len(url) == 0:
            return False
        return url

    def getIntegerParameter(key, default, min, max):
        abortMessage = 'Please specify a valid value for {0} (a number between {1} and {2})'.format(  # noqa: E501
            key, min, max)
        value = request.args.get(key, default)
        if value is default:
            return value
        try:
            value = int(value)
        except ValueError:
            abort(400, abortMessage)
        if value > max:
            abort(400, abortMessage)
        if value < min:
            abort(400, abortMessage)
        return value

    def initCodesFolder(folderName):
        if not path.exists(folderName):
            mkdir(folderName)

    def generateFilename(codesFolderName, url, size, boxSize):
        filename = normalizeFilename(url)
        sizeStr = 'auto'
        if size is not False:
            sizeStr = str(size)
        fullFilename = '{0}/{1}.{2}.{3}.png'.format(
            codesFolderName, filename, boxSize, sizeStr)
        return fullFilename

    def generateQRCodeImage(url, size, boxSize):
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=boxSize,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')

        if size is not False:
            img = img.resize((size, size), LANCZOS)

        return img

    def normalizeFilename(s):
        # https://gist.github.com/seanh/93666
        import string
        valid_chars = '-_.() %s%s' % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in s if c in valid_chars)
        filename = filename.replace(' ', '_')
        return filename

    @app.route('/static/<path:path>')
    def sendStaticResources(path):
        return send_from_directory('static', path)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
