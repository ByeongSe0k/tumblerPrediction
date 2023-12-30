from PIL import Image
import os

# image resize
# img = Image.open('/Users/byeongseok/Desktop/tumbler/nothing.jpg')
# imgResize = img.resize((416,416))

# print(imgResize.size)

# imgResize.save('/Users/byeongseok/Desktop/tumbler/nothingResized.jpg')
# print(os.path.isfile('/Users/byeongseok/Desktop/tumbler/nothingResized.jpg'))


#image rotate
img = Image.open('/Users/byeongseok/Desktop/tumbler/nothingResized.jpg')
img = img.rotate(-90)
img.save('/Users/byeongseok/Desktop/tumbler/nothingResizedRotated.jpg')
print(os.path.isfile('/Users/byeongseok/Desktop/tumbler/nonthingResizedRotated.jpg'))
