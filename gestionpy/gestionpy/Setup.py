import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

# On appelle la fonction setup
setup(
    name = "Products management",
    version = "1.0.2.2",
    description = "Manage all the products in your stock",
    author = "lionapi dev",
    author_email = "lionapi@dev.com",
    options = {
        "build_exe": {
            "includes": [],
            "excludes": ["tkinter"],
            "packages": ["os"],
            "include_files": ["product.ui", "auproduct.ui", "ma.ico", "ma.jpg", "splash.png"]
        },
        "bdist_msi": {

        }
    },
    executables = [
        Executable(
            script = "Products_pyqt5.py",
            copyright = "Copyright © 2019 Product management",
            icon = "ma.ico",
            base = base
        )
    ]
)

#https://stackoverflow.com/questions/2553886/how-can-i-bundle-other-files-when-using-cx-freeze
#https://buildmedia.readthedocs.org/media/pdf/cx-freeze/latest/cx-freeze.pdf
#A la racine du fichier *Products_pyqt5.py* ouvrir l'invite de commande et taper "python setup.py build" pour un build ou "python setup.py bdist_msi" pour un build et un executable
