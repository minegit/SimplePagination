'''
Created on 20-Jan-2016

@author: minion
'''


from .models import Country
from django.http import HttpResponse
import json
def get(request):
    """
    get all the country paginated at page_id and count< optional> default value of count is 10.
    """
    try:
        invalid_data = []
        if request.method == 'GET':
            if 'page_id' in request.GET:
                page_id = int(request.GET['page_id']) - 1
                if page_id < 0:
                    invalid_data.append('page_id')
            else:
                return_data = dict({'status':201 , 'message' : "Parameter not present : page_id"})
                return HttpResponse(json.dumps(return_data), content_type='application/json')
            if 'count' in request.GET:
                count = int(request.GET['count'])
                if count < 0:
                    invalid_data.append('count')
            else:
                count = 10
        elif request.method == 'POST':
            if 'page_id' in request.POST:
                page_id = int(request.POST['page_id']) - 1
                if page_id < 0:
                    invalid_data.append('page_id')
            else:
                return_data = dict({'status':201 , 'message' : "Parameter not present : page_id"})
                return HttpResponse(json.dumps(return_data), content_type='application/json')
            if 'count' in request.POST:
                count = int(request.POST['count'])
                if count < 0:
                    invalid_data.append('count')
            else:
                count = 10
        else:
            return_data = dict({'status':201 , 'message' : "Invalid request protocol"})
            return HttpResponse(json.dumps(return_data), content_type='application/json')
        
        if len(invalid_data) > 0:
            return_data = dict({'status':201 , 'message' :  ",".join(invalid_data) + " have invalid data"})
            return HttpResponse(json.dumps(return_data), content_type='application/json')
        
        offset = page_id * count
        data = Country.objects.filter().order_by('name')[offset:offset + count]
        return_val = []
        for x in data:
            return_val.append(x.name)
        print(return_val)
        return_data = dict({'status':200 , 'message' : return_val})
    except Exception, e:
        print(e)
        return_data = dict({'status':201 , 'message' : "Some error occurred"})
    return HttpResponse(json.dumps(return_data), content_type='application/json')
