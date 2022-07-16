# Generated by Django 3.2.14 on 2022-07-16 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0011_company_checkings'),
        ('seo', '0010_alter_promotion_web_location'),
        ('business', '0003_auto_20220620_1809'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('preguntas_respuestas', '0006_auto_20220603_1924'),
        ('escritos', '0007_auto_20220603_1924'),
        ('public_blog', '0006_auto_20220603_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisiteurTermRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escritos.term')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seo.visiteur')),
            ],
            options={
                'verbose_name': 'Term recommended for visiteur',
                'db_table': 'recsys_terms_recommended_visiteurs',
            },
        ),
        migrations.CreateModel(
            name='VisiteurQuestionRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='preguntas_respuestas.question')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seo.visiteur')),
            ],
            options={
                'verbose_name': 'Question recommended for visiteur',
                'db_table': 'recsys_questions_recommended_visiteurs',
            },
        ),
        migrations.CreateModel(
            name='VisiteurPublicBlogRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='public_blog.publicblog')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seo.visiteur')),
            ],
            options={
                'verbose_name': 'PublicBlog recommended for visiteur',
                'db_table': 'recsys_public_blogs_recommended_visiteurs',
            },
        ),
        migrations.CreateModel(
            name='VisiteurPromotionRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seo.promotion')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seo.visiteur')),
            ],
            options={
                'verbose_name': 'Term recommended for visiteur',
                'db_table': 'recsys_promotion_recommended_visiteurs',
            },
        ),
        migrations.CreateModel(
            name='VisiteurProductComplementaryRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.productcomplementary')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seo.visiteur')),
            ],
            options={
                'verbose_name': 'Term recommended for visiteur',
                'db_table': 'recsys_product_complementary_recommended_visiteurs',
            },
        ),
        migrations.CreateModel(
            name='VisiteurCompanyRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresas.company')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seo.visiteur')),
            ],
            options={
                'verbose_name': 'Company recommended for visiteur',
                'db_table': 'recsys_companies_recommended_visiteurs',
            },
        ),
        migrations.CreateModel(
            name='UserTermRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escritos.term')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Term recommended for user',
                'db_table': 'recsys_terms_recommended_users',
            },
        ),
        migrations.CreateModel(
            name='UserQuestionRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='preguntas_respuestas.question')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Question recommended for user',
                'db_table': 'recsys_questions_recommended_users',
            },
        ),
        migrations.CreateModel(
            name='UserPublicBlogRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='public_blog.publicblog')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PublicBlog recommended for user',
                'db_table': 'recsys_public_blogs_recommended_users',
            },
        ),
        migrations.CreateModel(
            name='UserPromotionRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seo.promotion')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Term recommended for user',
                'db_table': 'recsys_promotion_recommended_users',
            },
        ),
        migrations.CreateModel(
            name='UserProductComplementaryRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.productcomplementary')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Term recommended for user',
                'db_table': 'recsys_product_complementary_recommended_users',
            },
        ),
        migrations.CreateModel(
            name='UserCompanyRecommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('side', 'Side'), ('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom'), ('in_between', 'In between')], default='side', max_length=150)),
                ('location', models.CharField(choices=[('all-web', 'Toda la web'), ('web-inicio', 'Web Inicio'), ('screener-inicio', 'Screener Inicio'), ('screener-market', 'Screener Market'), ('screener-company', 'Screener Company'), ('cartera-inicio', 'Cartera Inicio'), ('cartera-financials', 'Cartera Financials'), ('cartera-balance', 'Cartera Balance'), ('private-profile', 'Private Profile'), ('public-profile', 'Public Profile'), ('question-inicio', 'Question Inicio'), ('question-details', 'Question Details'), ('term-inicio', 'Term Inicio'), ('term-details', 'Term Details'), ('blog-inicio', 'Blog Inicio'), ('blog-details', 'Blog Details')], default='all-web', max_length=150)),
                ('kind', models.CharField(choices=[('pop_up', 'Pop up'), ('banner', 'Big Banner'), ('lista', 'List'), ('solo', 'Solo')], default='solo', max_length=150)),
                ('clicked', models.BooleanField(default=False)),
                ('recommendation_personalized', models.BooleanField(default=False)),
                ('recommendation_explained', models.JSONField(default=dict)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('model_recommended', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresas.company')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company recommended for user',
                'db_table': 'recsys_companies_recommended_users',
            },
        ),
    ]
