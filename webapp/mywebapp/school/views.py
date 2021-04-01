# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponseBadRequest
import json
from . import db
from . import models
# Create your views here.

class StudentView(APIView):

    def get(self, request, roll_no=None):
        msg = "Roll Number required"
        if roll_no:
            s = db.read_entry(int(roll_no))
            if s:
                return JsonResponse({"name": s.name,
                                     "age": s.age,
                                     "roll_no": s.student_id,
                                     "gender": s.gender})
            msg = "No record found"
        else:
            students = db.read_entry()
            if students:
                ret = {}
                for k, v in students.items():
                    ret[k] = {
                        "name": v.name,
                        "age": v.age,
                        "roll_no": v.student_id,
                        "gender": v.gender
                    }
                return JsonResponse(ret, safe=False)

        return JsonResponse(msg, safe=False, status=400)

    def post(self, request):
        body = json.loads(request.body)
        s = models.Student(name=body.get("name"),
                    age=body.get("age"),
                    gender=body.get("gender"))

        db.write_entry(s)
        return JsonResponse({"status": "Added Successfully", "roll_no": s.student_id})

    def put(self, request):
        body=json.loads(request.body)
        if not body.get("roll_no"):
           return JsonResponse({"error":"Please provide roll no"}, status=400)
        else:
            roll_no = body.get("roll_no")
            s = db.read_entry(roll_no)
            if s:
                s.name = body.get('name')
                s.age = body.get('age')
                s.gender = body.get('gender')
                db.write_entry(s)
                msg = "Updated success"
            else:
                msg = "Record Not found"
        return JsonResponse({"status": msg})

    def delete(self, request):
        body = json.loads(request.body)
        if not body.get("roll_no"):
            return JsonResponse({"error": "Please provide roll no"}, status=400)
        else:
            roll_no = body.get("roll_no")
            deleted = db.delete_entry(roll_no)
            if deleted:
                msg = "Deleted Successfully"
            else:
                msg = "Record Not found"
        return JsonResponse({"status": msg, "roll_no": roll_no})
