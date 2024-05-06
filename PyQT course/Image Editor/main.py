from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QComboBox, QHBoxLayout, \
    QVBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageFilter, ImageEnhance

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQT")
main_window.resize(900, 700)

btn_folder = QPushButton("Folder")
file_list = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpness")
gray = QPushButton("B/W")
saturation = QPushButton("Color")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")

filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpness")
filter_box.addItem("B/W")
filter_box.addItem("Color")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

picture_box = QLabel("Image will apear here!")

master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(gray)
col1.addWidget(saturation)
col1.addWidget(contrast)
col1.addWidget(blur)

col2.addWidget(picture_box)

master_layout.addLayout(col1, 20)
master_layout.addLayout(col2, 80)

main_window.setLayout(master_layout)

working_directory = ""


def filter(files, extensions):
    results = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                results.append(file)
    return results


def getWorkDirectory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory()
    extensions = [".jpg", ".jpeg", ".png", ".svg", ".JPG", ".JPEG"]
    filenames = filter(os.listdir(working_directory), extensions)
    file_list.clear()
    for file in filenames:
        file_list.addItem(file)


class Editor():
    def __init__(self):
        self.image = None
        self.original = None
        self.filename = None
        self.save_folder = "edits/"

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(working_directory, self.filename)
        self.image = Image.open(fullname)
        self.original = self.image.copy()

    def save_image(self):
        path = os.path.join(working_directory, self.save_folder)
        if not (os.path.exists(path)) or not (os.path.isdir(path)):
            os.mkdir(path)

        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def show_image(self, path):
        picture_box.hide()
        image = QPixmap(path)
        w, h = picture_box.width(), picture_box.height()
        image = image.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio)
        picture_box.setPixmap(image)
        picture_box.show()

    def transformImage(self, transformation):
        transformations = {
            "B/W": lambda image: image.convert("L"),
            "Color": lambda image: ImageEnhance.Color(self.image).enhance(1.2),
            "Left": lambda image: image.transpose(Image.ROTATE_90),
            "Right": lambda image: image.transpose(Image.ROTATE_270),
            "Mirror": lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
            "Sharpness": lambda image: image.filter(ImageFilter.SHARPEN),
            "Contrast": lambda image: ImageEnhance.Contrast(self.image).enhance(1.2),
            "Blur": lambda image: image.filter(ImageFilter.BLUR)
        }
        transform_function = transformations.get(transformation)
        if transform_function:
            self.image = transform_function(self.image)
            self.save_image()
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

    def apply_filter(self, filter_name):
        if filter_name == "Original":
            self.image = self.original.copy()
        else:
            mapping = {
                "B/W": lambda image: image.convert("L"),
                "Color": lambda  image: ImageEnhance.Color(self.image).enhance(1.2),
                "Left": lambda image: image.transpose(Image.ROTATE_90),
                "Right": lambda image: image.transpose(Image.ROTATE_270),
                "Mirror": lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpness": lambda image: image.filter(ImageFilter.SHARPEN),
                "Contrast": lambda image: ImageEnhance.Contrast(self.image).enhance(1.2),
                "Blur": lambda image: image.filter(ImageFilter.BLUR)
            }
            filter_function = mapping.get(filter_name)
            if filter_function:
                self.image = filter_function(self.image)
                self.save_image()
                image_path = os.path.join(working_directory, self.save_folder, self.filename)
                self.show_image(image_path)
            pass
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.filename)
        self.show_image(image_path)

def handle_filter():
    if file_list.currentRow() >= 0:
        select_filter = filter_box.currentText()
        main.apply_filter(select_filter)

def displayImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        main.load_image(filename)
        main.show_image(os.path.join(working_directory, main.filename))


main = Editor()

btn_folder.clicked.connect(getWorkDirectory)
file_list.currentRowChanged.connect(displayImage)
gray.clicked.connect(lambda: main.transformImage("B/W"))
btn_left.clicked.connect(lambda: main.transformImage("Left"))
btn_right.clicked.connect(lambda: main.transformImage("Right"))
mirror.clicked.connect(lambda: main.transformImage("Mirror"))
sharpness.clicked.connect(lambda: main.transformImage("Sharpness"))
saturation.clicked.connect(lambda: main.transformImage("Color"))
contrast.clicked.connect(lambda: main.transformImage("Contrast"))
blur.clicked.connect(lambda: main.transformImage("Blur"))
filter_box.currentTextChanged.connect(main.apply_filter)

main_window.show()
app.exec()
