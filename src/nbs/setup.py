import os, sys

PWD = os.getenv("PWD")
DJANGO_PROJECT = os.environ.get("DJANGO_PROJECT") or "scrape"
DJANGO_ROOT_DIR = os.environ.get("DJANGO_ROOT_DIR") or "src"
# if not PWD.endswith(f"/{DJANGO_ROOT_DIR}"):
#     # src is the django-root
#     PWD = os.path.join(PWD, DJANGO_ROOT_DIR)


PROJ_MISSING_MSG = """Set an enviroment variable:\n
`DJANGO_PROJECT=your_project_name`\n
or call:\n
`init_django(project_name=your_project_name)`
"""


def init_django(project_name=None):
    candidate_pwd = os.path.join(PWD, DJANGO_ROOT_DIR)
    if os.path.isdir(candidate_pwd):
        os.chdir(candidate_pwd)
    else:
        os.chdir(PWD)

    dj_project_name = project_name or DJANGO_PROJECT
    if dj_project_name is None:
        raise Exception(PROJ_MISSING_MSG)

    sys.path.insert(0, PWD)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{dj_project_name}.settings")
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    import django

    django.setup()
