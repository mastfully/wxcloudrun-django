from django.db import models, connection

from tenat.models import Tenat
from users.models import Users
# Create your models here.


class CCamp(models.Model):

    name = models.CharField(max_length=20,verbose_name='营期',blank=False)
    start = models.DateField(verbose_name="开始日期",blank=False)
    end = models.DateField(verbose_name='结束日期',blank=False)
    total_people = models.IntegerField(verbose_name='总人数')
    remainder = models.IntegerField(verbose_name='剩余人数')
    symbol = models.IntegerField(verbose_name='第几期', blank=False)
    price = models.IntegerField(verbose_name='价格', blank=False, default=5980)

    class Meta:

        db_table = "c_camp"


class Title(models.Model):

    year = models.CharField(max_length=10)
    vacation = models.CharField(max_length=10)

    class Meta:
        db_table = 'title'


class JCampTbName(models.Model):
    tb_name = models.CharField(max_length=20, unique=True)
    c_name = models.CharField(max_length=20)
    current = models.BooleanField()

    class Meta:
        db_table = 'jcamp_tb_name'


class CCampTbName(models.Model):
    tb_name = models.CharField(max_length=20, unique=True)
    c_name = models.CharField(max_length=20)
    current = models.BooleanField()

    class Meta:
        db_table = 'ccamp_tb_name'


class JCamp(models.Model):

    name = models.CharField(max_length=20,verbose_name='营期',blank=False)
    start = models.DateField(verbose_name="开始日期",blank=False)
    end = models.DateField(verbose_name='结束日期',blank=False)
    total_people = models.IntegerField(verbose_name='总人数')
    remainder = models.IntegerField(verbose_name='剩余人数')
    symbol = models.IntegerField(verbose_name='第几期',blank=False)
    price = models.IntegerField(verbose_name='价格', blank=False, default=4980)

    class Meta:
        db_table = "j_camp"


class BaseSignUpListModel(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    symbol = models.IntegerField(verbose_name='第几期')
    gender = models.CharField(max_length=10,verbose_name='性别')
    name = models.CharField(max_length=20,verbose_name='姓名')
    age = models.CharField(max_length=10,verbose_name='年龄')
    emergency = models.CharField(max_length=20, verbose_name='紧急联系人')
    grade = models.CharField(max_length=10, verbose_name='年级')
    height = models.CharField(max_length=10, verbose_name='身高')
    phone = models.CharField(max_length=11)
    id_card = models.CharField(max_length=20,verbose_name='身份证')
    race = models.CharField(max_length=10, verbose_name='民族')
    school = models.CharField(max_length=20, verbose_name='学校')
    bad = models.CharField(max_length=20,verbose_name='擅长科目', blank=True, null=True)
    bad_reasonal = models.TextField(verbose_name='不擅长原因', blank=True, null=True)
    biology_full = models.CharField(max_length=10,verbose_name='生物满分', blank=True, null=True)
    biology_ideal_score = models.CharField(max_length=10,verbose_name='生物理想满分', blank=True, null=True)
    biology_near_score = models.CharField(max_length=10,verbose_name='生物最近满分', blank=True, null=True)
    chemistry_full = models.CharField(max_length=10,verbose_name='化学满分', blank=True, null=True)
    chemistry_ideal_score = models.CharField(max_length=10,verbose_name='化学理想满分', blank=True, null=True)
    chemistry_near_score = models.CharField(max_length=10,verbose_name='化学最近满分', blank=True, null=True)
    chinese_full = models.CharField(max_length=10,verbose_name='语文满分', blank=True, null=True)
    chinese_near_score = models.CharField(max_length=10,verbose_name='语文理想满分', blank=True, null=True)
    chinses_ideal_score = models.CharField(max_length=10,verbose_name='语文最近满分', blank=True, null=True)
    defect = models.TextField(verbose_name='自身缺陷', blank=True, null=True)
    dream = models.TextField(verbose_name='理想目标', blank=True, null=True)
    education_investment = models.CharField(max_length=20, blank=True, null=True)
    english_full = models.CharField(max_length=10,verbose_name='英语满分', blank=True, null=True)
    english_ideal_score = models.CharField(max_length=10,verbose_name='英语理想满分', blank=True, null=True)
    english_near_score = models.CharField(max_length=10,verbose_name='英语最近满分', blank=True, null=True)
    father_educational_background = models.CharField(max_length=10, blank=True, null=True)
    father_occupation = models.CharField(verbose_name='父亲职业',max_length=10, blank=True, null=True)
    geography_full = models.CharField(max_length=10,verbose_name='地理满分', blank=True, null=True)
    geography_ideal_score = models.CharField(max_length=10,verbose_name='地理理想满分', blank=True, null=True)
    geography_near_score = models.CharField(max_length=10,verbose_name='地理最近分数', blank=True, null=True)
    good = models.CharField(max_length=10, verbose_name='擅长科目', blank=True, null=True)
    good_reasonal = models.TextField(verbose_name='擅长原因', blank=True, null=True)
    history_full = models.CharField(max_length=10, verbose_name='历史满分', blank=True, null=True)
    history_ideal_score = models.CharField(max_length=10, verbose_name='历史理想分数', blank=True, null=True)
    history_near_score = models.CharField(max_length=10, verbose_name='历史最近分数', blank=True, null=True)
    household_income = models.CharField(max_length=10, verbose_name='家庭收入', blank=True, null=True)
    ideal_heigh_school = models.CharField(max_length=20, verbose_name='理想高中', blank=True, null=True)
    ideal_university = models.CharField(max_length=20, verbose_name='理想大学', blank=True, null=True)
    interst = models.TextField(verbose_name='兴趣爱好', blank=True, null=True)
    investment_in_children_education = models.CharField(max_length=20,verbose_name='教育投资', blank=True, null=True)
    math_full = models.CharField(max_length=10, verbose_name='数学满分', blank=True, null=True)
    math_ideal_score = models.CharField(max_length=10, verbose_name='数学理想分数', blank=True, null=True)
    math_near_score = models.CharField(max_length=10, verbose_name='数学最近分数', blank=True, null=True)
    methods_and_techniques = models.TextField(verbose_name='方法技巧', blank=True, null=True)
    mother_educational_background = models.CharField(max_length=10, verbose_name='母亲学历', blank=True, null=True)
    mother_occupation = models.CharField(max_length=10, verbose_name='母亲职业', blank=True, null=True)
    personal_need = models.TextField(blank=True, null=True)
    physics_full = models.CharField(max_length=10, verbose_name='物理满分', blank=True, null=True)
    physics_ideal_score = models.CharField(max_length=10, verbose_name='物理理想分数', blank=True, null=True)
    physics_near_score = models.CharField(max_length=10, verbose_name='物理最近分数', blank=True, null=True)
    politics_full = models.CharField(max_length=10, verbose_name='政治满分', blank=True, null=True)
    politics_ideal_score = models.CharField(max_length=10, verbose_name='政治理想分数', blank=True, null=True)
    politics_near_score = models.CharField(max_length=10, verbose_name='政治最近分数', blank=True, null=True)
    speciality = models.CharField(max_length=20, verbose_name='特长', blank=True, null=True)
    study_pro = models.CharField(max_length=20, verbose_name='', blank=True, null=True)

    class Meta:
        abstract = True


class TenatCampPrice(models.Model):

    tenat_id = models.ForeignKey(Tenat, on_delete=models.CASCADE)
    c_camp = models.CharField(verbose_name='畅享营价格',max_length=10,null=True,blank=True)
    j_camp = models.CharField(verbose_name='畅享营价格',max_length=10,null=True,blank=True)

    class Meta:
        db_table = 'tenat_camp_price'