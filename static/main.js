function createQRCode(event) {
    let url = document.getElementById('url').value;
    if (!url || url.length === 0) {
        document.getElementById('qrcode').src = '';
        document.getElementById('qrcode').style.display = 'none';
        event.preventDefault();
        return false;
    }

    if (url.endsWith('/')) url = url.slice(0, -1);    
    let src = '?url=' + url;

    let size = document.getElementById('size').value;
    if (size) {
        if (size < 10) size = 10;
        if (size > 1000) size = 1000;
        src += '&size=' + size;
    }

    let boxsize = document.getElementById('boxsize').value;
    if (boxsize) {
        if (boxsize < 1) boxsize = 1;
        if (boxsize > 100) boxsize = 100;
        src += '&boxsize=' + boxsize;
    }

    const clrfill = document.getElementById('clrfill').value;
    if (clrfill) src += '&fill=' + clrfill.slice(1);

    const clrback = document.getElementById('clrback').value;
    if (clrback) src += '&back=' + clrback.slice(1);

    document.getElementById('qrcode').src = src;
    document.getElementById('qrcode').style.display = 'block';

    event.preventDefault();
    return false;
}