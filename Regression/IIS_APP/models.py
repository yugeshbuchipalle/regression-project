from django.db import models
class RegisterdUser(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phonenumber = models.CharField(blank=True,null=True,max_length=13)
    password = models.CharField(max_length=30)

class CreateTestsuite(models.Model):
    Testsuites = (
        ('s5reg', 's5reg'),
        ('paralletestsuite1', 'paralletestsuite1'),
        ('paralletestsuite2', 'paralletestsuite2'),
        ('paralletestsuite3', 'paralletestsuite3'),
        ('paralletestsuite4', 'paralletestsuite4'),
        ('paralletestsuite5', 'paralletestsuite5'),
        ('Fullregtestsuite', 'Fullregtestsuite'),
    )
    Envirionment = (
        ('FT1', 'FT1'),
        ('FT2', 'FT2'),
        ('FT3', 'FT3'),
        ('SIT', 'SIT'),
        ('UAT', 'UAT'),
    )
    jobname = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    Testsuite = models.CharField(max_length=100, choices=Testsuites, default='Fullregtestsuite')
    envirionment = models.CharField(max_length=100, choices=Envirionment, default='FT1')


class Result(models.Model):
    jobname = models.CharField(max_length=100)
    passed = models.CharField(max_length=100)
    failed = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    result_list = models.CharField(max_length=2000,null=True)
