function createQRCode(event) {
    let url = document.getElementById('url').value;
    if (!url || url.length === 0) {
        document.getElementById('qrcode').src = '';
        document.getElementById('qrcode').style.display = 'none';
        document.getElementById('btn-download').style.display = 'none';
        event.preventDefault();
        return false;
    }

    if (url.endsWith('/')) url = url.slice(0, -1);    
    let src = '?url=' + url;

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

    const btnDownload = document.getElementById('btn-download');
    btnDownload.href = src;
    btnDownload.style.display = 'block';

    event.preventDefault();
    return false;
}