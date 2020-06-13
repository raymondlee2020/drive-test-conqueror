from restapi.models import RuleTrueFalse, RuleMultipleChoice
from rest_framework import viewsets
from restapi.serializers import RuleTrueFalseSerializer, RuleMultipleChoiceSerializer


class RuleTrueFalseViewSet(viewsets.ModelViewSet):
    queryset = RuleTrueFalse.objects.all()
    serializer_class = RuleTrueFalseSerializer


class RuleMultipleChoiceViewSet(viewsets.ModelViewSet):
    queryset = RuleMultipleChoice.objects.all()
    serializer_class = RuleMultipleChoiceSerializer