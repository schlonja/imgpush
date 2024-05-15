import os

IMAGES_DIR = "/images/"
CACHE_DIR = "/cache/"
OUTPUT_TYPE = "png"
MAX_UPLOADS_PER_DAY = 1000
MAX_UPLOADS_PER_HOUR = 100
MAX_UPLOADS_PER_MINUTE = 20
ALLOWED_ORIGINS = ["*"]
NAME_STRATEGY = "randomstr"
MAX_TMP_FILE_AGE = 5 * 60
RESIZE_TIMEOUT = 5
NUDE_FILTER_MAX_THRESHOLD = None
SHOW_UPLOAD_FORM = True
TOKEN_REQUIRED = True
BEARER_TOKEN = "6AHSJ56BG1rPK711K4zK0O1WMxUUU0LcKDlfEZr5lOzF3ReTBfscfSlSDEy8Be2K"
USER_AGENT = "Chrome/51.0.2704.103"

VALID_SIZES = []

MAX_SIZE_MB = 16

for variable in [item for item in globals() if not item.startswith("__")]:
    NULL = "NULL"
    env_var = os.getenv(variable, NULL).strip()
    if env_var is not NULL:
        try:
            env_var = eval(env_var)
        except Exception:
            pass
    globals()[variable] = env_var if env_var is not NULL else globals()[variable]
