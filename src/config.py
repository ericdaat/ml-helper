import os


DATABASE_URL = "sqlite:///{path}".format(
    path=os.path.join(os.environ.get("HOME"), ".ml-helper.sqlite")
)
TEST_DATABASE_URL = "sqlite:///:memory:"

SEABORN_THEME = "ticks"
SEABORN_PALETTE = "Set2"
