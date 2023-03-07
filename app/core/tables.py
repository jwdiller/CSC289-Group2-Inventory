import django_tables2 as tables

class TopStocksTable(tables.Table):
    productName = tables.Column(verbose_name='Product Name')
    orderAmount = tables.Column(verbose_name='Order Amount')

    class Meta:
        attrs = {'class': 'table table-bordered table-striped'}
        # Change the table class as needed
        empty_text = 'No data available'
        # Display this message if there's no data
        orderable = False
