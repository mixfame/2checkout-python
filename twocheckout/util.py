class Util:

    @classmethod
    def active(cls, sale):
        i = 0
        if 'recurring' in sale:
            invoice = sale
        else:
            invoice = sale.last_invoice()
        i = 0
        lineitems = dict()
        for lineitem_id in invoice.lineitems:
            if lineitem_id.billing.recurring_status == 'active':
                lineitems[i] = lineitem_id['lineitem_id']
                i += 1
        return lineitems
