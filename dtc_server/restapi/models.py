from django.db import models

# Create your models here.
class RuleTrueFalse(models.Model):
    quizId = models.IntegerField(default=0)
    quiz = models.TextField(default="")
    ansIndex = models.IntegerField(default=0)

    class Meta:
        db_table = "rule_true_false"

class RuleMultipleChoice(models.Model):
    quizId = models.IntegerField(default=0)
    quiz = models.TextField(default="")
    option1 = models.TextField(default="")
    option2 = models.TextField(default="")
    option3 = models.TextField(default="")
    ansIndex = models.IntegerField(default=0)
    
    class Meta:
        db_table = "rule_multiple_choice"