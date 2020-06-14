from restapi.models import RuleTrueFalse, RuleMultipleChoice
from rest_framework import viewsets
from restapi.serializers import RuleTrueFalseSerializer, RuleMultipleChoiceSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import base64
import threading
import cv2
import numpy as np


class RuleTrueFalseViewSet(viewsets.ModelViewSet):
    queryset = RuleTrueFalse.objects.all()
    serializer_class = RuleTrueFalseSerializer


class RuleMultipleChoiceViewSet(viewsets.ModelViewSet):
    queryset = RuleMultipleChoice.objects.all()
    serializer_class = RuleMultipleChoiceSerializer


@csrf_exempt
def SignRecognitionHandler(request):

    mapName = {
        "haar_turnRight": "道路遵循方向(僅准右轉)",
        "haar_forbidRotate": "禁止迴轉"
    }

    def detect(img, haar, result):

        detector = cv2.CascadeClassifier("{base_path}/classifiers/{haar}.xml".format(
            base_path=os.path.abspath(os.path.dirname(__file__)), haar=haar))
        signs = detector.detectMultiScale(img,
                                          scaleFactor=1.1,
                                          minNeighbors=2,
                                          minSize=(30, 30))
        if len(signs) > 0:
            for (x, y, w, h) in signs:
                cv2.rectangle(img,
                              (x, y), (x+w, y+h),
                              (0, 0, 255), 2)
            
            retval, buffer = cv2.imencode('.jpg', img)
            pic_str = base64.b64encode(buffer)
            pic_str = pic_str.decode()
        else:
            pic_str = None
            print('nothing')

        result.append({"name": mapName[haar], "img": pic_str})

    if request.method == "POST":
        data = request.FILES.get('signImg').read()

        img = np.asarray(bytearray(data), dtype="uint8")
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        
        result = []
        threads = []

        for classifier in mapName.keys():
            threads.append(threading.Thread(target=detect, args=(img.copy(), classifier, result)))
        
        for i in range(len(threads)):
            threads[i].start()

        for i in range(len(threads)):
            threads[i].join()

    return JsonResponse(result, safe=False)
