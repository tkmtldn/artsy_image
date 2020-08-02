import os
import numpy as np
from PIL import Image

def save_content(dirname, fname, length, width):
    images = []
    for y in range(width):
        row = []
        for x in range(length):
            row.append('{}_{}.jpg'.format(x, y))
        imgs = [Image.open(i) for i in row]
        imgs_comb = np.hstack([np.asarray(i) for i in imgs])
        imgs_comb = Image.fromarray(imgs_comb)
        imgs_comb.save('row_{}.jpg'.format(y))
        images.append('row_{}.jpg'.format(y))
        for filename in row:
            os.remove(filename)

    imgs = [Image.open(i) for i in images]
    imgs_comb = np.vstack([np.asarray(i) for i in imgs])
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save(fname)  # '{}.jpg'.format(time.time())

    for file in images:
        os.remove(file)

    print(f"File '{fname}' is ready.")