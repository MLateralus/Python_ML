from scipy import misc
import matplotlib.pyplot as plt

def loadImg(img_path):
    # i = Image.open(img_path)
    i = plt.imread(img_path)
    return i

if __name__ == '__main__':

    bait = loadImg("C:\Python27\Images\Taj.jpg")
    interpolations = ['nearest', 'bilinear', 'bicubic', 'gaussian', 'bessel', 'quadric']
    fig, ax = plt.subplots(nrows=3, ncols=3)

    for i in range(0,6):
        interpol = interpolations[i]
        plt.subplot(2,3,i+1)
        plt.imshow(bait, interpolation=interpol)
        plt.xlabel(interpolations[i])

    plt.show()
