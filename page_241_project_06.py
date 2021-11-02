"""
Author: Ngô Văn Chiến
Date: 17/10/2021
 Problem: Define a second version of the grayscale function that uses the allegedly crude
method of simply averaging each RGB value. Test the function by comparing its
results with those of the other version discussed in this chapter.
Solution:

    ....
"""
def grayscale1(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

def grayscale2(image):
    average = (r + g + b) // 3
    image.setPixel(x, y, (average,average,average))
def main():
            filename = input("smokey.gif ")
            image = Image(filename)
            grayscale2(image)
            image.draw()

if __name__ == "__main__":
    main()