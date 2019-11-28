
ruid = request.args.get('ruid', '')
if len(ruid) > 0:
    url = 'https://www.uni-koblenz-landau.de/resolveuid/{0}'.format(ruid)
