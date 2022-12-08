from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Item(models.Model):
    class Meta:
        db_table    = "item"


    CATEGORY_CHOICES = (
        ('食品', '食品'),
        ('飲料', '飲料'),
        ('家電', '家電・カメラ'),
        ('PC・スマホ・通信', 'PC・スマホ・通信'),
        ('日用雑貨・キッチン用品', '日用雑貨・キッチン用品'),
        ('コスメ・健康・医薬品', 'コスメ・健康・医薬品'),
        ('インテリア・寝具', 'インテリア・寝具'),
        ('服飾・ファッション', '服飾・ファッション'),
        ('スポーツ', 'スポーツ'),
        ('本・電子書籍・音楽', '本・電子書籍・音楽'),
        ('キッズ・ベビー・玩具', 'キッズ・ベビー・玩具'),
        ('ゲーム・ホビー・楽器', 'ゲーム・ホビー・楽器'),
        ('車・バイク', '車・バイク'),
        ('ペット・花・DIY', 'ペット・花・DIY'),
        ('サービス・リフォーム', 'サービス・リフォーム'),
        ('その他', 'その他'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="品名",max_length=100)
    price = models.IntegerField(verbose_name="価格")
    category = models.CharField(verbose_name="カテゴリー",choices=CATEGORY_CHOICES,max_length=100)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)

    def __str__(self):
        return self.name

class PurchaseData(models.Model):

    GENDER_CHOICES = (
        ('女性', '女性'),
        ('男性', '男性'),
        ('その他・無回答', 'その他・無回答'),
    )

    AGE_CHOICES = (
        ('〜19歳', '〜19歳'),
        ('20代', '20代'),
        ('30代', '30代'),
        ('40代', '40代'),
        ('50代', '50代'),
        ('60代', '60代'),
        ('70代', '70代'),
        ('80代〜', '80代〜'),
        ('不明・無回答', '不明・無回答'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    detail = models.CharField(max_length=200)
    #cost = models.IntegerField(default=0)
    #category = models.CharField(max_length=10) 
    #
    date = models.DateTimeField(verbose_name='購買日時')
    place = models.CharField(verbose_name='商品受け渡し場所', max_length=40)
    gender = models.CharField(verbose_name='性別', choices=GENDER_CHOICES, max_length=20)
    age = models.CharField(verbose_name='年齢', choices=AGE_CHOICES, max_length=20)
    item = models.ManyToManyField(Item, verbose_name="購入商品", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now())
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)

    def __str__(self):
        return self.place
