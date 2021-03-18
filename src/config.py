import os


DATABASE_URL = "sqlite:///{path}".format(
    path=os.path.join(os.environ.get("HOME"), ".ml-helper.sqlite")
)
TEST_DATABASE_URL = "sqlite:///:memory:"

if os.environ.get("TEST_ENVIRONMENT"):
    DATABASE_URL = TEST_DATABASE_URL

SEABORN_THEME = "ticks"
SEABORN_PALETTE = "Set2"
