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

    class Meta:

        db_table = "c_camp"


class JCamp(models.Model):

    name = models.CharField(max_length=20,verbose_name='营期',blank=False)
    start = models.DateField(verbose_name="开始日期",blank=False)
    end = models.DateField(verbose_name='结束日期',blank=False)
    total_people = models.IntegerField(verbose_name='总人数')
    remainder = models.IntegerField(verbose_name='剩余人数')
    symbol = models.IntegerField(verbose_name='第几期',blank=False)

    class Meta:

        db_table = "j_camp"


class BaseSignUpListModel():

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    symbol = models.IntegerField(verbose_name='第几期')
    name = models.CharField(max_length=20,verbose_name='姓名')
    age = models.CharField(max_length=10,verbose_name='年龄')
    bad = models.CharField(max_length=20,verbose_name='擅长科目')
    bad_reasonal = models.TextField(verbose_name='不擅长原因')
    biology_full = models.CharField(max_length=10,verbose_name='生物满分')
    biology_ideal_score = models.CharField(max_length=10,verbose_name='生物满分')
    biology_near_score = models.CharField(max_length=10,verbose_name='生物满分')
    birthday = models.CharField(max_length=10)
    chemistry_full = models.CharField(max_length=10,verbose_name='生物满分')
    chemistry_ideal_score = models.CharField(max_length=10,verbose_name='生物满分')
    chemistry_near_score = models.CharField(max_length=10,verbose_name='生物满分')
    chinese_full = models.CharField(max_length=10,verbose_name='生物满分')
    chinese_near_score = models.CharField(max_length=10,verbose_name='生物满分')
    chinses_ideal_score = models.CharField(max_length=10,verbose_name='生物满分')
    defect = models.TextField(verbose_name='自身缺陷')
    dream = models.TextField(verbose_name='理想目标')
    education_investment = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    emergency = models.CharField(max_length=20,verbose_name='紧急联系人')
    english_full = models.CharField(max_length=10,verbose_name='生物满分')
    english_ideal_score = models.CharField(max_length=10,verbose_name='生物满分')
    english_near_score = models.CharField(max_length=10,verbose_name='生物满分')
    father_educational_background = models.CharField(max_length=10)
    father_occupation = models.CharField(verbose_name='父亲职业',max_length=10)
    geography_full = models.CharField(max_length=10,verbose_name='生物满分')
    geography_ideal_score = models.CharField(max_length=10,verbose_name='生物满分')
    geography_near_score = models.CharField(max_length=10,verbose_name='地理最高分')
    good = models.CharField(max_length=10, verbose_name='擅长科目')
    good_reasonal = models.TextField(verbose_name='擅长原因')
    grade = models.CharField(max_length=10,verbose_name='年级')
    height = models.CharField(max_length=10, verbose_name='身高')
    history_full = models.CharField(max_length=10, verbose_name='身高')
    history_ideal_score = models.CharField(max_length=10, verbose_name='身高')
    history_near_score = models.CharField(max_length=10, verbose_name='身高')
    household_income = models.CharField(max_length=10, verbose_name='身高')
    ideal_heigh_school = models.CharField(max_length=20, verbose_name='身高', blank=True)
    ideal_university = models.CharField(max_length=20, verbose_name='身高', blank=True)
    interst = models.TextField(verbose_name='兴趣爱好')
    investment_in_children_education = models.CharField(max_length=20,verbose_name='教育投资')
    math_full = models.CharField(max_length=10, verbose_name='身高')
    math_ideal_score = models.CharField(max_length=10, verbose_name='身高')
    math_near_score = models.CharField(max_length=10, verbose_name='身高')
    methods_and_techniques = models.TextField(verbose_name='方法技巧')
    mother_educational_background = models.CharField(max_length=10, verbose_name='身高')
    mother_occupation = models.CharField(max_length=10, verbose_name='身高')
    personal_need = models.TextField()
    phone = models.CharField(max_length=11)
    physics_full = models.CharField(max_length=10, verbose_name='身高')
    physics_ideal_score = models.CharField(max_length=10, verbose_name='身高')
    physics_near_score = models.CharField(max_length=10, verbose_name='身高')
    politics_full = models.CharField(max_length=10, verbose_name='身高')
    politics_ideal_score = models.CharField(max_length=10, verbose_name='身高')
    politics_near_score = models.CharField(max_length=10, verbose_name='身高')
    race = models.CharField(max_length=10, verbose_name='身高')
    school = models.CharField(max_length=20, verbose_name='身高')
    speciality = models.CharField(max_length=20, verbose_name='身高')
    study_pro = models.CharField(max_length=20, verbose_name='身高')






class TenatCampPrice(models.Model):

    tenat_id = models.ForeignKey(Tenat,on_delete=models.CASCADE)
    c_camp = models.CharField(verbose_name='畅享营价格',max_length=10,null=True,blank=True)
    j_camp = models.CharField(verbose_name='畅享营价格',max_length=10,null=True,blank=True)

    class Meta:
        db_table = 'tenat_camp_price'