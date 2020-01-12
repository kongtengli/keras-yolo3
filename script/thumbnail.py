import os
from PIL import Image
imgs = os.listdir('cai341')
print(imgs)
count = 69
for file in imgs:
    # os.rename(i,'imgs/' + str(count) + '')
    if file == '.DS_Store': continue
    # count += 1

    img = Image.open("cai341/" + file)
    copy = img.copy()
    copy.thumbnail((1000, 583), Image.BICUBIC)
    width, height = copy.size
    n_im = Image.new("RGB", (1000, 583), "black")
    n_im.paste(copy, (int((1000 - width) / 2), int((583 - height) / 2)))
    # n_im.show()
    n_im.save("cai1000*583/" + str(count) + ".jpg")
    count += 1

