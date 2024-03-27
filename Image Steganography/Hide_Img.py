import PIL.Image
import io

img = PIL.Image.open('FatihEminKarahan-CV.png')
byte_arr = io.BytesIO()
img.save(byte_arr, 'PNG')

with open('Üni_Logo.png', 'ab') as f:
    f.write(byte_arr.getvalue())
