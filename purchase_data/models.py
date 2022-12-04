from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Item(models.Model):
    class Meta:
        db_table    = "item"


    CATEGORY_CHOICES = (
        ('1', '食品'),
        ('2', '飲料'),
        ('3', '家電・カメラ'),
        ('4', 'PC・スマホ・通信'),
        ('5', '日用雑貨・キッチン用品'),
        ('6', 'コスメ・健康・医薬品'),
        ('7', 'インテリア・寝具'),
        ('8', '服飾・ファッション'),
        ('9', 'スポーツ'),
        ('10', '本・電子書籍・音楽'),
        ('11', 'キッズ・ベビー・玩具'),
        ('12', 'ゲーム・ホビー・楽器'),
        ('13', '車・バイク'),
        ('14', 'ペット・花・DIY'),
        ('15', 'サービス・リフォーム'),
        ('16', 'その他'),
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
        ('1', '女性'),
        ('2', '男性'),
        ('3', 'その他・無回答'),
    )

    AGE_CHOICES = (
        ('1', '〜19歳'),
        ('2', '20代'),
        ('3', '30代'),
        ('4', '40代'),
        ('5', '50代'),
        ('6', '60代'),
        ('7', '70代'),
        ('8', '80代〜'),
        ('9', '不明・無回答'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(verbose_name='購買日時', default=timezone.now())
    place = models.CharField(verbose_name='商品受け渡し場所', max_length=40)
    gender = models.CharField(verbose_name='性別', choices=GENDER_CHOICES, max_length=2)
    age = models.CharField(verbose_name='年齢', choices=AGE_CHOICES, max_length=2)
    item = models.ManyToManyField(Item, verbose_name="購入商品", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now())
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)