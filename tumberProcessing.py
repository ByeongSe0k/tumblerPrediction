from glob import glob
from sklearn.model_selection import train_test_split

imgList = glob('/Users/byeongseok/Desktop/tumbler/darknet/build/darknet/x64/data/obj/*.jpg')

trainImgList, testImgList = train_test_split(imgList, test_size=0.1, random_state=42)

with open('/Users/byeongseok/Desktop/tumbler/darknet/build/darknet/x64/data/train.txt', 'w') as f:
    f.write('\n'.join(trainImgList)+'\n')
with open('/Users/byeongseok/Desktop/tumbler/darknet/build/darknet/x64/data/test.txt', 'w') as ff:
    ff.write('\n'.join(testImgList)+'\n')
