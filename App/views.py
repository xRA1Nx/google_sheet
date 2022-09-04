from django.db.models import Sum, Count, Max, Min, Avg
from django.views.generic import ListView
from .models import GoogleSheet
from qsstats import QuerySetStats


def time_series(queryset, date_field, interval, func=None):
    qsstats = QuerySetStats(queryset, date_field, func)
    return qsstats.time_series(*interval)


class SheetDataListView(ListView):
    model = GoogleSheet
    context_object_name = "sheet_data"
    template_name = "index.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        q = self.get_queryset()
        if q.exists():
            start = q.aggregate(start_date=Min('delivery_time')).get('start_date', 0)
            end = q.aggregate(end_date=Max('delivery_time')).get('end_date', 0)

            context['count'] = time_series(q, 'delivery_time', [start, end, 'weeks'])
            total = time_series(q, 'delivery_time', [start, end], func=Sum('usd_price', default=0))
            total = list(filter(lambda x: x[1] > 0, total))
            context['total'] = total

            usd_sum = q.aggregate(usd_sum=Sum('usd_price')).get('usd_sum', 0)
            context['usd_sum'] = usd_sum
        else:
            context['count'] = {}
            context['total'] = {}

        return context
