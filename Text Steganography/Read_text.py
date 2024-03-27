with open('Hide.png', 'rb') as f:
    text = f.read()
    offset = text.index(bytes.fromhex('FFD9'))
    f.seek(offset + 2)
    print(f.read())