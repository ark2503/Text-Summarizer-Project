import setuptools 

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = 'ark2503'
SRC_REPO = 'TextSummarizer'
AUTHOR_EMAIL = 'arjunrk2103@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for NLP App",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages = setuptools.find_packages(where = "src"),
    package_dir = {"": "src"}
)