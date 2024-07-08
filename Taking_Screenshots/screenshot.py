import pyscreenshot as ImageGrab


def take_screenshot(file_name, bbox):
    img = ImageGrab.grab(bbox)
    img.save(file_name)

    img.show()

if __name__ == '__main__':
    file_name = input('Input file name: ')
    bbox = list(map(int, input('Input bounding box "x1 y1 x2 y2": ').split()))
    take_screenshot(file_name, bbox)
