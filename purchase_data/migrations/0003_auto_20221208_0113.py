# Generated by Django 3.2.16 on 2022-12-07 16:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_data', '0002_auto_20221207_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('食品', '食品'), ('飲料', '飲料'), ('家電', '家電・カメラ'), ('PC・スマホ・通信', 'PC・スマホ・通信'), ('日用雑貨・キッチン用品', '日用雑貨・キッチン用品'), ('コスメ・健康・医薬品', 'コスメ・健康・医薬品'), ('インテリア・寝具', 'インテリア・寝具'), ('服飾・ファッション', '服飾・ファッション'), ('スポーツ', 'スポーツ'), ('本・電子書籍・音楽', '本・電子書籍・音楽'), ('キッズ・ベビー・玩具', 'キッズ・ベビー・玩具'), ('ゲーム・ホビー・楽器', 'ゲーム・ホビー・楽器'), ('車・バイク', '車・バイク'), ('ペット・花・DIY', 'ペット・花・DIY'), ('サービス・リフォーム', 'サービス・リフォーム'), ('その他', 'その他')], max_length=100, verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='purchasedata',
            name='age',
            field=models.CharField(choices=[('〜19歳', '〜19歳'), ('20代', '20代'), ('30代', '30代'), ('40代', '40代'), ('50代', '50代'), ('60代', '60代'), ('70代', '70代'), ('80代〜', '80代〜'), ('不明・無回答', '不明・無回答')], max_length=20, verbose_name='年齢'),
        ),
        migrations.AlterField(
            model_name='purchasedata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 7, 16, 13, 30, 236857, tzinfo=utc), verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='purchasedata',
            name='gender',
            field=models.CharField(choices=[('女性', '女性'), ('男性', '男性'), ('その他・無回答', 'その他・無回答')], max_length=20, verbose_name='性別'),
        ),
    ]
