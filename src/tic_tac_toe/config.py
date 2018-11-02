import os

APP_DIR = os.path.dirname(os.path.realpath(__file__))

settings = {
    "template_path": os.path.join(APP_DIR, "templates"),
    "static_path": os.path.join(APP_DIR, "static")
}