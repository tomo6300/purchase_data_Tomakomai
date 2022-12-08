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

    PLACE_CHOICES=(
        ('青葉町','青葉町'),
    ('明野新町','明野新町'),
    ('明野元町','明野元町'),
    ('あけぼの町','あけぼの町'),
    ('旭町','旭町'),
    ('有明町','有明町'),
    ('泉町','泉町'),
    ('一本松町','一本松町'),
    ('字糸井','字糸井'),
    ('入船町','入船町'),
    ('字植苗','字植苗'),
    ('有珠の沢町','有珠の沢町'),
    ('ウトナイ北','ウトナイ北'),
    ('ウトナイ南','ウトナイ南'),
    ('永福町','永福町'),
    ('王子町','王子町'),
    ('大町','大町'),
    ('音羽町','音羽町'),
    ('表町','表町'),
    ('柏木町','柏木町'),
    ('字柏原','字柏原'),
    ('春日町','春日町'),
    ('川沿町','川沿町'),
    ('木場町','木場町'),
    ('錦西町','錦西町'),
    ('啓北町','啓北町'),
    ('小糸井町','小糸井町'),
    ('光洋町','光洋町'),
    ('寿町','寿町'),
    ('幸町','幸町'),
    ('栄町','栄町'),
    ('桜木町','桜木町'),
    ('桜坂町','桜坂町'),
    ('三光町','三光町'),
    ('汐見町','汐見町'),
    ('字静川','字静川'),
    ('清水町','清水町'),
    ('しらかば町','しらかば町'),
    ('白金町','白金町'),
    ('新開町','新開町'),
    ('新富町','新富町'),
    ('新中野町','新中野町'),
    ('新明町','新明町'),
    ('末広町','末広町'),
    ('澄川町','澄川町'),
    ('住吉町','住吉町'),
    ('青雲町','青雲町'),
    ('大成町','大成町'),
    ('字高丘','字高丘'),
    ('高砂町','高砂町'),
    ('拓勇西町','拓勇西町'),
    ('拓勇東町','拓勇東町'),
    ('字樽前','字樽前'),
    ('東開町','東開町'),
    ('ときわ町','ときわ町'),
    ('豊川町','豊川町'),
    ('錦町','錦町'),
    ('字錦岡','字錦岡'),
    ('日新町','日新町'),
    ('字沼ノ端','字沼ノ端'),
    ('沼ノ端中央','沼ノ端中央'),
    ('のぞみ町','のぞみ町'),
    ('花園町','花園町'),
    ('浜町','浜町'),
    ('はまなす町','はまなす町'),
    ('晴海町','晴海町'),
    ('日の出町','日の出町'),
    ('日吉町','日吉町'),
    ('双葉町','双葉町'),
    ('船見町','船見町'),
    ('字弁天','字弁天'),
    ('北栄町','北栄町'),
    ('北星町','北星町'),
    ('北光町','北光町'),
    ('本町','本町'),
    ('本幸町','本幸町'),
    ('真砂町','真砂町'),
    ('松風町','松風町'),
    ('字丸山','字丸山'),
    ('字美沢','字美沢'),
    ('美園町','美園町'),
    ('緑町','緑町'),
    ('港町','港町'),
    ('美原町','美原町'),
    ('宮の森町','宮の森町'),
    ('見山町','見山町'),
    ('宮前町','宮前町'),
    ('明徳町','明徳町'),
    ('もえぎ町','もえぎ町'),
    ('元町','元町'),
    ('元中野町','元中野町'),
    ('矢代町','矢代町'),
    ('柳町','柳町'),
    ('山手町','山手町'),
    ('弥生町','弥生町'),
    ('字勇払','字勇払'),
    ('若草町','若草町'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #detail = models.CharField(max_length=200)
    date = models.DateTimeField(verbose_name='購買日時')
    #place = models.CharField(verbose_name='商品受け渡し場所', max_length=40)
    place = models.CharField(verbose_name='商品受け渡し場所', choices=PLACE_CHOICES,max_length=40)
    gender = models.CharField(verbose_name='性別', choices=GENDER_CHOICES, max_length=20)
    age = models.CharField(verbose_name='年齢', choices=AGE_CHOICES, max_length=20)
    item = models.ManyToManyField(Item, verbose_name="購入商品", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now())
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)

    def __str__(self):
        return self.place
