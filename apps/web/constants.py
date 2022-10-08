CONTENT_FOR_PROMOTION = "promotion"
CONTENT_FOR_SUGGESTION = "suggestion"
CONTENT_FOR_ANNOUNCEMENT = "announcement"
CONTENT_FOR_WELCOME = "welcome"
CONTENT_FOR_ENGAGEMENT = "engagement"
CONTENT_FOR_ENGAGEMENT_USER_FIRST_CALL = f"{CONTENT_FOR_ENGAGEMENT}-user-first-call"
CONTENT_FOR_ENGAGEMENT_USER_NO_ACTIVE = f"{CONTENT_FOR_ENGAGEMENT}-user-no-active"
CONTENT_FOR_ENGAGEMENT_USER_LITTLE_ACTIVE = f"{CONTENT_FOR_ENGAGEMENT}-user-little-active"

LIST_CONTENT_ENGAGEMENT = (
    CONTENT_FOR_ENGAGEMENT,
    CONTENT_FOR_ENGAGEMENT_USER_FIRST_CALL,
    CONTENT_FOR_ENGAGEMENT_USER_NO_ACTIVE,
    CONTENT_FOR_ENGAGEMENT_USER_LITTLE_ACTIVE,
)
COMMENT_PURCHASED_PRODUCT = "Comenta tu úlitma compra"

CONTENT_PURPOSES = (
    (CONTENT_FOR_PROMOTION, "Promotion"),
    (CONTENT_FOR_SUGGESTION, "Suggestion"),
    (CONTENT_FOR_ANNOUNCEMENT, "Announcement"),
    (CONTENT_FOR_WELCOME, "Welcome"),
    (CONTENT_FOR_ENGAGEMENT, "Engagement"),
    (CONTENT_FOR_ENGAGEMENT_USER_NO_ACTIVE, "Engagement user no active"),
    (CONTENT_FOR_ENGAGEMENT_USER_LITTLE_ACTIVE, "Engagement user little active"),
    (CONTENT_FOR_ENGAGEMENT_USER_FIRST_CALL, "Engagement user first call"),
)

WHOM_TO_SEND_EMAIL_ALL = "all"
WHOM_TO_SEND_EMAIL_TYPE_RELATED = "type_related"
WHOM_TO_SEND_EMAIL_SELECTED = "selected"
WHOM_TO_SEND_EMAIL = (
    (WHOM_TO_SEND_EMAIL_ALL, "All"),
    (WHOM_TO_SEND_EMAIL_TYPE_RELATED, "Type related"),
    (WHOM_TO_SEND_EMAIL_SELECTED, "Selected"),
)
