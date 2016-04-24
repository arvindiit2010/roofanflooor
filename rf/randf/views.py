from rest_framework.views import APIView
from django.http import HttpResponse
from randf.serializers import MovieSerializer, UserSerializer
from randf.models import CustomUser
import traceback
import json

class User(APIView):

    def post(self, request,*args, **kwargs):
        try:
            #ipdb.set_trace()
            required_params = ['email', 'first_name', 'last_name', 'contact']
            if not all(p in self.request.DATA for p in required_params):
                response_msg = {'error': 'please check input params. %s are compulsory' % required_params }
                response = HttpResponse(json.dumps(response_msg))
                response.status_code = 405
                return response
            serializer = UserSerializer(data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(json.dumps(serializer.data))

        except Exception as e:
            response_msg = {'error': 'unable to server request. Get exception: %s' % traceback.format_exc()}
            response = HttpResponse(json.dumps(response_msg))
            response.status_code = 404
            return response

class MovieRating(APIView):

    def post(self, request,*args, **kwargs):
        try:
            #ipdb.set_trace()

            required_params = ['name', 'rating']
            if not all(p in self.request.DATA for p in required_params):
                response_msg = {'error': 'please check input params. movie name and rating are compulsory'}
                response = HttpResponse(json.dumps(response_msg))
                response.status_code = 405
                return response
            if 'contact' in request.DATA:
                res = CustomUser.objects.filter(contact=request.DATA['contact'], user_name=request.DATA['user_name'])
            elif 'email' in request.DATA:
                res = CustomUser.objects.filter(email=request.DATA['email'], user_name=request.DATA['user_name'])
            else:
                response_msg = {'error': 'please check input params. contact or email  and user_name are compulsory'}
                response = HttpResponse(json.dumps(response_msg))
                response.status_code = 405
                return response
            if res:
                serializer = MovieSerializer(data=request.DATA)
                if serializer.is_valid():
                    serializer.save()
                    return HttpResponse(json.dumps(serializer.data))
                else:
                    pass
            else:
                response_msg = {'error': 'Please check user name and contact/email'}
                response = HttpResponse(json.dumps(response_msg))
                response.status_code = 404
            return response
        except Exception as e:
            response_msg = {'error': 'unable to server request. Get exception: %s' % traceback.format_exc()}
            response = HttpResponse(json.dumps(response_msg))
            response.status_code = 404
            return response

    def get(self, request):

        try:
            #ipdb.set_trace()
            from randf.models import MovieRating
            if 'contact' in request.QUERY_PARAMS:
                usr = CustomUser.objects.filter(contact=request.QUERY_PARAMS['contact'], user_name=request.QUERY_PARAMS['user_name'])
            elif 'email' in request.QUERY_PARAMS:
                usr = CustomUser.objects.filter(email=request.QUERY_PARAMS['email'], user_name=request.QUERY_PARAMS['user_name'])
            else:
                response_msg = {'error': 'please check input params. contact or email  and user_name are compulsory'}
                response = HttpResponse(json.dumps(response_msg))
                response.status_code = 405
                return response

            res = MovieRating.objects.filter(name=request.QUERY_PARAMS['name'])
            total_count = len(res)
            if total_count == 0:
                response_msg = {'error': 'please check input movie name this name %s not present' % request.QUERY_PARAMS['name']}
                response = HttpResponse(json.dumps(response_msg))
                response.status_code = 404
                return response

            total = 0
            for rating in res:
                total += int(rating.rating)
            avg = total/float(total_count)
            if avg >= 5:
                hit = 'YES'
            else:
                hit = 'NO'

            response_msg = {'Success': hit, 'average_rating': round(avg, 2)}
            response = HttpResponse(json.dumps(response_msg))
            response.status_code = 200
            return response

        except Exception as e:
            response_msg = {'error': 'unable to server request. Get exception: %s' % e}
            response = HttpResponse(json.dumps(response_msg))
            response.status_code = 404
            return response

