from django.views import generic
from django.conf import settings

from systempay import models


class TransactionListView(generic.ListView):
    model = models.SystemPayTransaction
    template_name = 'systempay/dashboard/transaction_list.html'
    context_object_name = 'transactions'


class TransactionDetailView(generic.DetailView):
    model = models.SystemPayTransaction
    template_name = 'systempay/dashboard/transaction_detail.html'
    context_object_name = 'txn'

    def get_context_data(self, **kwargs):
        ctx = super(TransactionDetailView, self).get_context_data(**kwargs)
        ctx['show_form_buttons'] = getattr(
            settings, 'PAYPAL_PAYFLOW_DASHBOARD_FORMS', False)
        return ctx
