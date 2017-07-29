from scipy import misc
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from skimage.restoration import denoise_nl_means, denoise_tv_chambolle, estimate_sigma


class Image:

    def __init__(self, img_path, interpolations, deep):
        self.interpolations = interpolations
        self.image = plt.imread(img_path)
        self.how_deep = deep
        self.interpol_num = len(interpolations)

    def draw(self):
        fig, ax = plt.subplots(nrows=2, ncols=3)

        # Reference
        plt.subplot(2, 3, 1)
        plt.imshow(self.image, interpolation="None")
        plt.ylabel("Reference")

        if (self.how_deep != 0):
            for i in range(0, self.how_deep):
                self.imshow_interpols()
                self.nl_means()
                self.total_variations()
        else:
            self.imshow_interpols()
            self.nl_means()
            self.total_variations()

        plt.show()


    def imshow_interpols(self):
        for i in range(0, self.interpol_num):
            interpol = self.interpolations[i]
            plt.subplot(2, 3, i + 2)
            plt.imshow(self.image, interpolation=interpol)
            plt.ylabel(self.interpolations[i])
            self.__log__(i, interpol)

    def nl_means(self):
        self.__log__("Denoising nl means.....")
        plt.subplot(2, 3, 5)
        denoise = denoise_nl_means(self.image, 7, 9, 0.1, multichannel=True)
        plt.imshow(denoise)
        plt.ylabel("Non_local means")
        self.__log__("Denoising nl means done")

    def total_variations(self):
        self.__log__("Denoising total variations.....")
        plt.subplot(2, 3, 6)
        tv_denoised = denoise_tv_chambolle(self.image, weight=0.1, multichannel=True)
        plt.imshow(tv_denoised)
        plt.ylabel("Total Variation denoise")
        self.__log__("Denoising total variations done")

    def __log__(self, arg1, *args):
        value = args or ""
        print(arg1, value)

if __name__ == '__main__':

    newImage = Image("C:/lena_recon_3.jpg", ['nearest', 'bilinear', 'quadric'], 4)
    newImage.draw()

