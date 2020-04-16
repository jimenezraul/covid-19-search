import json
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from django.contrib import messages


def covid_search(request):
    covid_url = 'https://coronavirus-19-api.herokuapp.com/countries'
    r = requests.get(covid_url.format()).json()
    if request.method == 'GET':
        search = request.GET.get("search")
        if request.GET.get("search") == None:
            pass
        elif request.GET.get("search") == '':
            messages.warning(
                request, "Please Enter a Country...")
            return redirect('covid_search')
        else:
            country_search = [
                x for x in r if x['country'] == search.title()]
            if not country_search:
                try:
                    country_search = [
                        x for x in r if x['country'] == search.upper()]
                    search_result = {
                        'country': country_search[0]['country'],
                        'total_cases': country_search[0]['cases'],
                        'cases_today': country_search[0]['todayCases'],
                        'deaths': country_search[0]['deaths'],
                        'recovered': country_search[0]['recovered'],
                    }
                    context = {
                        'search_result': search_result,
                    }
                    return render(request, "covidapp/index.html", context)
                except:
                    messages.warning(
                        request, "Country Not Found in Database")
                    return redirect('covid_search')

            search_result = {
                'country': country_search[0]['country'],
                'total_cases': country_search[0]['cases'],
                'cases_today': country_search[0]['todayCases'],
                'deaths': country_search[0]['deaths'],
                'recovered': country_search[0]['recovered'],
            }
            context = {
                'search_result': search_result,
            }
            return render(request, "covidapp/index.html", context)

    context = {
        'country': r,
    }
    return render(request, "covidapp/index.html", context)
