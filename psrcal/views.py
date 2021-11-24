from django.shortcuts import render
from .tradecal import cal_main, cal_month_main, cal_week_main
from .calmain import plreport_main, plreport_month_main, plreport_week_main


# Create your views here.
def psr_home(request):
    context = {}
    if request.method == "POST":
        symbol = request.POST["symbol"]
        timeFrame =request.POST["timeFrame"]
        fdate =request.POST["fdate"]
        tdate =request.POST["tdate"]
        fund = 1000
        if timeFrame == "day":
            data = cal_main(symbol, timeFrame, fdate, tdate)
            df = plreport_main(symbol, fdate, tdate, fund)
            context ={"data": data, "df": df}
        if timeFrame == "month":
            data = cal_month_main(symbol, timeFrame, fdate, tdate)
            df = plreport_month_main(symbol, fdate, tdate, fund)
            context ={"data": data, "df": df}
        if timeFrame == "week":
            data = cal_week_main(symbol, timeFrame, fdate, tdate)
            df = plreport_week_main(symbol, fdate, tdate, fund)
            context ={"data": data, "df": df}
    return render(request, "psrhome.html", context)