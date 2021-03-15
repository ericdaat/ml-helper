import os

if os.environ.get("TEST_ENVIRONMENT") == "True":
    DATABASE_URL = "sqlite:///:memory:"
else:
    DATABASE_URL = "sqlite:///{path}".format(
        path=os.path.join(os.environ.get("HOME"), ".ml-helper.sqlite")
    )
