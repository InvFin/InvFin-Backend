from typing import Dict

DEFAULT_JSON_CHECKS_FILE = "src/escritos/term-checks.json"

EXTRA_DATA_DICT_KEY_OLD_URLS = "previous_urls"

DEFAULT_EXTRA_DATA_DICT: Dict = {
    EXTRA_DATA_DICT_KEY_OLD_URLS: [],
}

BASE_ESCRITO_PUBLISHED = 1
BASE_ESCRITO_DRAFT = 2
BASE_ESCRITO_SCHEDULED = 3
BASE_ESCRITO_NEED_REVISION = 4

BASE_ESCRITO_STATUS = (
    (BASE_ESCRITO_PUBLISHED, "Publicado"),
    (BASE_ESCRITO_DRAFT, "Borrador"),
    (BASE_ESCRITO_SCHEDULED, "Programado"),
    (BASE_ESCRITO_NEED_REVISION, "Necesita revisión"),
)

ESCRITO_STATUS_MAP = {
    BASE_ESCRITO_PUBLISHED: "Publicado",
    BASE_ESCRITO_DRAFT: "Borrador",
    BASE_ESCRITO_SCHEDULED: "Programado",
    BASE_ESCRITO_NEED_REVISION: "Necesita revisión",
}