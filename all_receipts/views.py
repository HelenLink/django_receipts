from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

# Create your views here.

eat_dict = {
    'lobio': 'Лобио - фасоль, перец',
    'olivie': 'Оливье - картошка, яйца',
    'borwch': 'Борщ - картошка, свекла'
}

eat_razdely = {
    'soups': ['borwch'],
    'vtoriey': ['lobio', 'картошка пюре'],
    'salad': ['olivie', 'vinegret']
}


def index(request):
    eats = list(eat_dict)
    context={
        'eats':eats,
        'eat_dict' : eat_dict,
    }
    return render(request, 'all_receipts/index.html', context=context)


def index2(request):
    eat_r = list(eat_razdely)
    li_elem = ''
    for elem in eat_r:
        redirect_path = reverse('type-name', args=[elem])
        li_elem += f'<li><a href={redirect_path}>{elem.title()}</a></li>'
    return HttpResponse(f'<ul>{li_elem}</ul>')

def get_info_about_receipts(request, sign: str):
    descrition = eat_dict.get(sign, None)
    data = {
        'descrition_receipts':descrition,
        'sign_receipts':sign,
        'eats':eat_dict,
                }
    return render(request, 'all_receipts/info_all_receipts.html', context=data)


def get_info_about_receipts_by_number(request, sign: int):
    eat = list(eat_dict)
    if sign > len(eat):
        return HttpResponseNotFound(f"Неправильный порядковый номер {sign}")
    name = eat[sign - 1]
    redirect_url = reverse("eat-name", args=(name,))
    return HttpResponseRedirect(redirect_url)

def get_info_about_type_bluda(request, signtype: str):
    descr = eat_razdely.get(signtype, None)
    if descr:
        elem = ''
        for sign in descr:
            redirect_path = reverse("eat-name", args=[sign])
            elem += f'<li><a href={redirect_path}>{sign.title()}</a></li>'
        return HttpResponse(f'<ul>{elem}</ul>')
    else:
        return HttpResponseNotFound(f"Нет рецепта {signtype}")
