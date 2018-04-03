def make_readable(seconds):
    hr = str(seconds / 3600)
    mn = str((seconds % 3600)/60)
    sc = str(((seconds % 3600)%60))
    if len(hr) == 1:
        hr = '0' + hr
    if len(mn) == 1:
        mn = '0' + mn
    if len(sc) == 1:
        sc = '0' + sc
    return hr + ':' + mn + ':' + sc