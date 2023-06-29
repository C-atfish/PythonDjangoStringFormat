import json
from .models import StringConversionTable
from .Wrapper import Wrapper
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


@csrf_exempt
def string_formatter(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            string_input = data["input"]
            line_limit = data["lineLength"]

            formatted_string = Wrapper.wrap(string_input, line_limit)
            record = StringConversionTable(input=data["input"], output=formatted_string,
                                           max_line_length=data["lineLength"])
            record.save()

            return JsonResponse({
                "output": formatted_string
            })
        except KeyError:
            return JsonResponse({"Error": 'You need to attach the fields lineLength and input.'})

    else:
        return JsonResponse({"error": "Method not supported"}, status=405)


@csrf_exempt
def get_all_results(request):
    if request.method == "GET":
        all_results = StringConversionTable.objects.all()
        all_results_json = serializers.serialize("json", all_results)
        return JsonResponse({"data": all_results_json}, safe=False)
    else:
        return JsonResponse({"error": "Method not supported"}, status=405)
