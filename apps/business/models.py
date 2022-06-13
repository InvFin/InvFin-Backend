from django.db.models import (
    Model,
    CharField,
    SET_NULL,
    CASCADE,
    OneToOneField,
    ForeignKey,
    SlugField,
    DateTimeField,
    IntegerField,
    JSONField,
    FloatField,
    BooleanField
)
from django.urls import reverse
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField

from apps.general.bases import BaseComment
from apps.general.models import Currency
from apps.seo.models import Promotion
from .managers import ProductManager
from apps.business import constants

User = get_user_model()


class Customer(Model):
    user = OneToOneField(User, on_delete=SET_NULL, null=True)
    created_at = DateTimeField(auto_now_add=True)
    # stripe_id = CharField(max_length=500, null=True, blank=True, unique=True, db_index=True)
    stripe_id = CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'business_customers'

    def __str__(self):
        return self.user.username


class Product(Model):
    title = CharField(max_length=300)
    slug = SlugField(max_length=300, null=True, blank=True)
    stripe_id = CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = CharField(max_length=500, null=True, blank=True)
    video = CharField(max_length=500, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(null=True, blank=True)
    visits = IntegerField(default=0)
    is_active = BooleanField(default=True)
    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'business_products'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("business:product", kwargs={"slug": self.slug})
    

class ProductComplementary(Model):
    EXTRAS = dict(
   title="¿Qué incluye?",
   include=[
      {
         "icon":"<i class='fas fa-infinity'></i>",
         "text":"Acceso de por vida"
      },
      {
         "icon":"<i class='fas fa-file-archive'></i>",
         "text":"Actualizaciones constantes"
      },
      {
         "icon":"<i class='fas fa-book'></i>",
         "text":"Ebook de regalo"
      }
   ])

    product = ForeignKey(Product,
        on_delete=CASCADE,
        null=True,
        related_name = "complementary")
    image = CharField(max_length=500, null=True, blank=True)
    video = CharField(max_length=500, null=True, blank=True)
    title = CharField(max_length=300, blank=True)
    slug = SlugField(max_length=300, null=True, blank=True)
    price = FloatField(null=True, blank=True)
    payment_type = CharField(max_length=300, blank=True, choices=constants.PAYMENT_TYPE)
    stripe_id = CharField(max_length=500, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    is_active = BooleanField(default=True)
    currency = ForeignKey(Currency, on_delete=SET_NULL, null=True)
    subscription_period = CharField(max_length=300, blank=True, choices=constants.SUBSCRIPTION_PERIOD)
    subscription_interval = IntegerField(default=0, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(null=True, blank=True)
    extras = JSONField(default=EXTRAS)
    purchase_result = CharField(max_length=300, blank=True, choices=constants.PURCHASE_RESULT)
    product_result = CharField(max_length=300, blank=True, default='')

    class Meta:
        verbose_name = 'Product complementary'
        verbose_name_plural = 'Products complementary'
        db_table = 'business_products_complementary'

    def __str__(self):
        return self.product.title
    
    @property
    def final_price(self):
        return f'{self.price} {self.currency}'
    
    @property
    def subscription_type(self):
        period = 'Mensual'
        if constants.PERIOD_MONTHLY == self.subscription_period:
            if self.subscription_interval == 6:
                period = 'Bianual'
        if constants.PERIOD_YEARLY == self.subscription_period:
            period = 'Anual'
        return period
    
    @property
    def payment(self):
        payment = self.payment_type[1]
        if self.payment_type == constants.TYPE_SUBSCRIPTION:
            payment = f'{constants.PAYMENT_TYPE[0][1]} {self.subscription_type}'
        return payment
    
    @property
    def payment_link(self):
        return reverse('business:create_checkout', kwargs={"pk": self.pk})


class ProductSubscriber(Model):    
    product = ForeignKey(Product,
        on_delete=CASCADE,
        null=True,
        related_name = "subscribers")
    product_complementary = ForeignKey(ProductComplementary,
        on_delete=CASCADE,
        null=True,
        related_name = "complementary_subs")
    subscriber = ForeignKey(User,
        on_delete=CASCADE,
        null=True,
        related_name = "subscriptions")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(null=True, blank=True)
    is_active = BooleanField(default=True)

    class Meta:
        verbose_name = 'Product subscriber'
        verbose_name_plural = 'Products subscribers'
        db_table = 'business_products_subscribers'

    def __str__(self):
        return self.product.title


class ProductComment(BaseComment):
    rating = IntegerField(null=True, blank=True)
    content_related = ForeignKey(Product,
        on_delete=CASCADE,
        null=True,
        related_name = "comments_related")
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products comments'
        db_table = 'business_products_comments'
    
    def __str__(self):
        return self.content_related.title


class ProductDiscount(Model):
    product = ForeignKey(
        Product, 
        on_delete=SET_NULL, 
        null=True,
        blank=True
    )
    product_complementary = ForeignKey(
        ProductComplementary, 
        on_delete=SET_NULL, 
        null=True, 
        blank=True
    )
    promotion = ForeignKey(
        Promotion, 
        on_delete=SET_NULL, 
        null=True, 
        blank=True,
        related_name="promotion_discount"
    )
    start_date = DateTimeField(null=True, blank=True)
    end_date = DateTimeField(null=True, blank=True)
    discount = FloatField(null=True, blank=True)
    is_percentage = BooleanField(default=True)
    is_active = BooleanField(default=True)

    class Meta:
        verbose_name = 'Product discount'
        verbose_name_plural = 'Products discounts'
        db_table = 'business_products_discounts'
    
    def __str__(self):
        return self.product.title


class ProductComplementaryPaymentLink(Model):
    product_complementary = ForeignKey(ProductComplementary,
        on_delete=CASCADE,
        null=True,
        related_name = "payment_links")
    promotion = ForeignKey(
        Promotion, 
        on_delete=SET_NULL, 
        null=True, 
        blank=True,
        related_name="promotion_link_payment"
    )
    title = CharField(max_length=500, null=True, blank=True)
    link = CharField(max_length=500, null=True, blank=True)
    stripe_id = CharField(max_length=500, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(null=True, blank=True)
    for_website = BooleanField(default=False)

    class Meta:
        verbose_name = 'Product complementary payment link'
        verbose_name_plural = 'Products complementary payment link'
        db_table = 'business_products_complementary_payment_link'

    def __str__(self):
        return self.product_complementary.product.title


class TransactionHistorial(Model):
    product = ForeignKey(
        Product, 
        on_delete=SET_NULL, 
        null=True
    )
    product_complementary = ForeignKey(
        ProductComplementary, 
        on_delete=SET_NULL, 
        null=True, 
        blank=True
    )
    product_comment = ForeignKey(
        ProductComment, 
        on_delete=SET_NULL, 
        null=True, 
        blank=True
    )
    customer = ForeignKey(Customer, on_delete=SET_NULL, null=True)
    created_at = DateTimeField(auto_now_add=True)
    payment_method = CharField(max_length=300, blank=True, choices=constants.PAYMENT_METHOD)
    currency = ForeignKey(Currency, on_delete=SET_NULL, null=True, blank=True)
    discount = ForeignKey(ProductDiscount, on_delete=SET_NULL, null=True, blank=True)
    final_amount = FloatField(null=True, blank=True)
    stripe_response = JSONField(default=dict, null=True, blank=True)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        db_table = 'business_transactions'

    def __str__(self):
        return self.product.title


class StripeWebhookResponse(Model):
    product = ForeignKey(
        Product, 
        on_delete=SET_NULL, 
        null=True
    )
    product_complementary = ForeignKey(
        ProductComplementary, 
        on_delete=SET_NULL, 
        null=True, 
        blank=True
    )
    customer = ForeignKey(
        Customer, 
        on_delete=SET_NULL, 
        null=True, 
        blank=True
    )
    full_response = JSONField(default=dict)
    created_at = DateTimeField(auto_now_add=True)
    stripe_id = CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Stripe webhook response"
        verbose_name_plural = "Stripe webhook responses"
        db_table = 'business_stripe_webhook_responses'

    def __str__(self):
        return str(self.created_at)