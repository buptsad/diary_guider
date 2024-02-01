from pathlib import Path
from uuid import uuid4

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(uuid4())
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/flaskdb'

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True