

# from stats.models import my_data
from opportunity.models import Opportunity


from accounts.models import Account, Tags
from common.utils import STAGES, SOURCES, CURRENCY_CODES
from contacts.models import Contact
from opportunity.models import Opportunity



from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, View
from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView






User = get_user_model()

class statsData(APIView):

    def get(self, request, format=None):
        model = Opportunity

        querytest = model.objects.values_list()
#####   PIE CHART DATA
        dataPie = model.objects.order_by('id').values_list()
        labelsPie = model.objects.order_by().values_list('stage', flat=True).distinct()
        amountSums=[]
        for i in labelsPie:
            temp = []
            temp = model.objects.order_by().values_list('amount', flat=True).filter(stage=i)
            sum = 0
            for j in temp:
                sum = sum + j
            amountSums.append(sum)

#####   LINE CHART DATA
        labelsLost = model.objects.values_list('name', flat=True).filter(stage="CLOSED LOST")
        labelsWon = model.objects.values_list('name', flat=True).filter(stage="CLOSED WON")
        amountsLost = model.objects.values_list('amount', flat=True).filter(stage="CLOSED LOST")
        amountsWon = model.objects.values_list('amount', flat=True).filter(stage="CLOSED WON")

        dataStage = []
        for x in STAGES:
            dataStage.append(x[0])

        data = {
            "dataStage": dataStage,
            "querytest": querytest,
            "labelsPie": labelsPie,
            "labelsSums": labelsPie,
            "amountsPie": amountSums,
            "amountSums": amountSums,
            "labelsLost": labelsLost,
            "labelsWon": labelsWon,
            "amountsLost": amountsLost,
            "amountsWon": amountsWon,
            "dataPie": dataPie,
        }
        return Response(data)


class ChartData(TemplateView):
    context_object_name = "opportunity_list"
    model = Opportunity
    template_name = 'charts.html'


    def get_queryset(self):
        queryset = self.model.objects.all().prefetch_related(
            "contacts", "account")
        if self.request.user.role != "ADMIN" and not \
                self.request.user.is_superuser:
            queryset = queryset.filter(
                Q(assigned_to__in=[self.request.user]) |
                Q(created_by=self.request.user.id))

        request_post = self.request.POST
        if request_post:
            if request_post.get('name'):
                queryset = queryset.filter(
                    name__icontains=request_post.get('name'))
            if request_post.get('stage'):
                queryset = queryset.filter(stage=request_post.get('stage'))
            if request_post.get('lead_source'):
                queryset = queryset.filter(
                    lead_source=request_post.get('lead_source'))
            if request_post.get('account'):
                queryset = queryset.filter(
                    account_id=request_post.get('account'))
            if request_post.get('contacts'):
                queryset = queryset.filter(
                    contacts=request_post.get('contacts'))

        return queryset


    def get_context_data(self, **kwargs):
        context = super(ChartData, self).get_context_data(**kwargs)
        context["opportunity_list"] = self.get_queryset()
        context["accounts"] = Account.objects.filter(status="open")
        context["contacts"] = Contact.objects.all()
        context["stages"] = STAGES
        context["sources"] = SOURCES
        context["per_page"] = self.request.POST.get('per_page')

        search = False
        if (
                self.request.POST.get('name') or self.request.POST.get('stage') or
                self.request.POST.get('lead_source') or
                self.request.POST.get('account') or
                self.request.POST.get('contacts')
        ):
            search = True

        context["search"] = search
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)







