import PIL.Image
import io

with open('Uni_Logo.png', 'rb') as f:
    content = f.read()
    offset = content.index(b'6082')

    f.seek(offset + 2)

    new_img = PIL.Image.open(io.BytesIO(f.read()))
    new_img.save("new_img.png")