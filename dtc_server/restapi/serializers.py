from restapi.models import RuleTrueFalse, RuleMultipleChoice
from rest_framework import serializers


class RuleTrueFalseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RuleTrueFalse
        fields = ['quizId', 'quiz', 'ansIndex']


class RuleMultipleChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RuleMultipleChoice
        fields = ['quizId', 'quiz', 'option1', 'option2', 'option3', 'ansIndex']