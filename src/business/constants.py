TYPE_SUBSCRIPTION = "subscription"
TYPE_ONE_TIME = "payment"

PAYMENT_TYPE = ((TYPE_SUBSCRIPTION, "Subscripción"), (TYPE_ONE_TIME, "Un pago"))

PERIOD_DAYLY = "day"
PERIOD_WEEKLY = "week"
PERIOD_MONTHLY = "month"
PERIOD_YEARLY = "year"

SUBSCRIPTION_PERIOD = (
    (PERIOD_DAYLY, "Daily"),
    (PERIOD_WEEKLY, "Weekly"),
    (PERIOD_MONTHLY, "Montly"),
    (PERIOD_YEARLY, "Yearly"),
)

PAYMENT_PAYPAL = "credits"
PAYMENT_WIRE = "wire"
PAYMENT_CREDITS = "paypal"
PAYMENT_OTHER = "other"
PAYMENT_CARD = "card"

PAYMENT_METHOD = (
    (PAYMENT_PAYPAL, "Credits"),
    (PAYMENT_WIRE, "Wire"),
    (PAYMENT_CREDITS, "Paypal"),
    (PAYMENT_OTHER, "Others"),
    (PAYMENT_CARD, "Card"),
)

INVALID_CARD = 4000000000000002
VALID_CARD = 4242424242424242

ADD_CREDITS = "add_credits"
SHARE_EXCEL = "share_excel"
ILIMITED_CREDITS = "ilimited_credits"
RANDOM_PRIZE = "random_prize"
RANDOM_CREDITS = "random_credits"

PURCHASE_RESULT = (
    (ADD_CREDITS, ADD_CREDITS),
    (SHARE_EXCEL, SHARE_EXCEL),
    (ILIMITED_CREDITS, ILIMITED_CREDITS),
    (RANDOM_PRIZE, RANDOM_PRIZE),
    (RANDOM_CREDITS, RANDOM_CREDITS),
)