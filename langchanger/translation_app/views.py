import math
import random
import statistics

from django.shortcuts import get_list_or_404
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from registration_app.permissions import *
from .serializers import *

STATISTIC_DAY_RANGE = 30


def get_data_sample():
    return [random.randrange(x, x + STATISTIC_DAY_RANGE) for x in
            range(STATISTIC_DAY_RANGE)]


def paginator(request, queryset):
    page_size = int(request.GET.get('page_size', 6))
    current_page = int(request.GET.get('current_page', 1))

    first_item = (current_page - 1) * page_size
    last_item = current_page * page_size

    queryset_part = queryset[first_item:last_item]

    return queryset_part


class GenreListView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]


class LanguageListView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.AllowAny]


class MainPageView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        last_origins = Origin.objects.all()
        serializer = AllOriginSerializer(last_origins, many=True)

        content = {'data': serializer.data}

        return Response(content)


class AllOriginView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    filter_name_set = {
        'genre': 'genre__in',
        'age': 'age_limit__in',
        'language': 'origin_language__in',
    }

    def get(self, request):
        raw_filter = request.GET.get('filters', {})
        order_by = request.GET.get('order', 'relevance')

        complete_filter = {}
        for key, data in raw_filter.items():
            if key in self.filter_name_set:
                filter_key = self.filter_name_set[key]
                complete_filter[filter_key] = data

        queryset = Origin.objects.filter(**complete_filter)

        if order_by == 'relevance':
            queryset = queryset.order_by('id')

        response_queryset = paginator(request, queryset)

        serializer = AllOriginSerializer(response_queryset, many=True)
        content = {'data': serializer.data}

        return Response(content)


class OneOriginView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('origin', -1))

        origin = get_object_or_404(Origin, pk=pk)

        serializer_origin = OneOriginSerializer(origin)

        content = {'data': {
            'origin': serializer_origin.data,
        }}

        return Response(content)


class ReadOriginView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        pk = int(request.GET.get('origin', -1))

        origin = get_object_or_404(Origin, pk=pk)
        serializer = ReadOriginSerializer(origin)

        content = {'data': serializer.data}

        return Response(content)


class SearchOriginView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        search_sentence = request.GET.get('sentence')

        queryset_by_title = Origin.objects.filter(
            title__icontains=search_sentence)
        queryset_by_author = Origin.objects.filter(
            author__icontains=search_sentence)
        queryset_by_description = Origin.objects.filter(
            description__icontains=search_sentence)

        queryset_by_description = queryset_by_description.difference(
            queryset_by_author, queryset_by_title)
        queryset_by_author = queryset_by_author.difference(queryset_by_title)

        serializer_title = AllOriginSerializer(queryset_by_title, many=True)
        serializer_author = AllOriginSerializer(queryset_by_author, many=True)
        serializer_description = AllOriginSerializer(queryset_by_description,
                                                     many=True)

        content = {
            'origin_by_title': serializer_title.data,
            'origin_by_author': serializer_author.data,
            'origin_by_description': serializer_description.data,
        }

        return Response(content, status=200)


class OriginCommentStatistic(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):

        origins = Origin.objects.all()[:5]
        comment_statistics = []
        i = 0
        for origin in origins:
            statistics_base = {
                "origin_name": origin.title,
                "comment_amount": [],
                "day_list": list(range(STATISTIC_DAY_RANGE)),
                "quantiles": None,
                "mean": None,
                "variance": None,
                "stdev": None,
                "normalized_mean": None,
                "normalized_variance": None,
                "normalized_stdev": None,
                "coef_asymmetry": None,
                "coef_excess": None,
                "coef_cor": None,
                "equation": None
            }
            for j in range(STATISTIC_DAY_RANGE):
                from_date = origin.publication_date.date() + \
                            datetime.timedelta(days=j)
                to_date = origin.publication_date.date() + \
                          datetime.timedelta(days=j + 1)
                statistics_base['comment_amount'].append(
                    CommentOrigin.objects.filter(
                        Q(origin=origin) &
                        Q(post_date__gte=from_date) &
                        Q(post_date__lte=to_date)
                    ).count())

            statistics_base['quantiles'] = statistics.quantiles(
                statistics_base['comment_amount'])
            statistics_base['mean'] = statistics.fmean(
                statistics_base['comment_amount'])
            statistics_base['variance'] = statistics.variance(
                statistics_base['comment_amount'])
            statistics_base['stdev'] = statistics.stdev(
                statistics_base['comment_amount'])

            for j in range(STATISTIC_DAY_RANGE):
                if statistics_base['comment_amount'][j] < \
                        statistics_base['quantiles'][0] or \
                        statistics_base['comment_amount'][j] > \
                        statistics_base['quantiles'][2]:
                    statistics_base['day_list'][j] = -1
                    statistics_base['comment_amount'][j] = -1
            statistics_base['comment_amount'] = list(filter(
                lambda x: -1 != x,
                statistics_base['comment_amount']
            ))
            statistics_base['day_list'] = list(filter(
                lambda x: -1 != x,
                statistics_base['day_list']
            ))

            statistics_base['normalized_mean'] = statistics.fmean(
                statistics_base['comment_amount'])
            statistics_base['normalized_variance'] = statistics.variance(
                statistics_base['comment_amount'])
            statistics_base['normalized_stdev'] = statistics.stdev(
                statistics_base['comment_amount'])
            statistics_base['coef_asymmetry'] = sum(map(
                lambda x: (x - statistics_base['normalized_mean']) ** 3,
                statistics_base['comment_amount']
            )) / (len(statistics_base['comment_amount']) * statistics_base[
                'normalized_stdev'] ** 3)
            statistics_base['coef_excess'] = sum(map(
                lambda x: (x - statistics_base['normalized_mean']) ** 4,
                statistics_base['comment_amount']
            )) / (len(statistics_base['comment_amount']) * statistics_base[
                'normalized_stdev'] ** 4)

            mean_day = sum(statistics_base['day_list']) / len(
                statistics_base['day_list'])
            stdev_day = statistics.stdev(statistics_base['day_list'])
            covar = sum(map(lambda x, y: x * y, statistics_base['day_list'],
                            statistics_base['comment_amount'])) / len(
                statistics_base['day_list']) - mean_day * statistics_base[
                        'normalized_mean']
            statistics_base['coef_cor'] = covar / (
                    stdev_day * statistics_base['normalized_stdev'])
            k = round(
                math.sqrt(statistics_base['normalized_stdev'] / stdev_day), 4)
            b = round(statistics_base['normalized_mean'] - k * mean_day, 4)
            statistics_base["equation"] = "{k}*x - {b}".format(k=k, b=b)

            comment_statistics.append(statistics_base)

            i += 1

        content = {
            "data": comment_statistics
        }
        return Response(content)


class OriginCommentView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request):
        origin = int(request.GET.get('origin', -1))

        comments = get_list_or_404(CommentOrigin, origin=origin)
        serializer = OriginCommentSerializer(comments, many=True)

        content = {'data': serializer.data}

        return Response(content)


class CreateCommentOriginView(APIView):
    permission_classes = [permissions.IsAuthenticated, BlacklistPermission]

    renderer_classes = [JSONRenderer]

    def post(self, request):
        comment_serializer = MakeCommentOriginSerializer(data=request.data)

        if comment_serializer.is_valid():
            comment_serializer.save()

            return Response(status=200)
        return Response(comment_serializer.errors, status=400)


class ChangeCommentOriginView(APIView):
    permission_classes = [ModeratorPermission]

    renderer_classes = [JSONRenderer]

    def delete(self, request):
        comment_id = int(request.POST.get('comment', -1))

        comment = get_object_or_404(CommentOrigin, id=comment_id)

        comment.delete()

        return Response(status=200)