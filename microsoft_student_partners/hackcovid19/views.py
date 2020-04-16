from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class Hackcovid19(View):
    template_name = "hackcovid19/index.html"
    from time import gmtime
    import datetime

    month_list = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    time_dict = {"gmt": {}, "now": {}}
    gmt = gmtime()
    now = datetime.datetime.now()
    time_dict["gmt"]["year"] = gmt[0]
    time_dict["gmt"]["month"] = month_list[int(gmt[1]) - 1]
    time_dict["gmt"]["day"] = gmt[2]
    time_dict["gmt"]["hour"] = gmt[3]
    time_dict["gmt"]["minute"] = gmt[4]
    time_dict["gmt"]["second"] = gmt[5]
    time_dict["now"]["year"] = now.year
    time_dict["now"]["month"] = month_list[int(now.month) - 1]
    time_dict["now"]["day"] = now.day
    time_dict["now"]["hour"] = now.hour
    time_dict["now"]["minute"] = now.minute
    time_dict["now"]["second"] = now.second
    print(now, gmt)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.time_dict)
