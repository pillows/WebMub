import binascii
def filesig(f):
    signatures = {
        "webm":"1a45dfa3", #WebM File Signature
        "mkv":"1a45dfa3" #MKV File Signature. Note the similarities between mkv and webm. "1a45dfa3934282886d6174726f736b61" is the full signature.
        "gif":"47494638" #GIF File Signature
    }
    content = binascii.hexlify(f)
    
    if str(content[:8]) in signatures.values():
        return true
    else:
        return false
        