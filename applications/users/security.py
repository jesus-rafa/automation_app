from applications.configuracion.models import Accesos, App


def get_access(request):

    perfil = []
    menu = []

    for group in request.user.groups.all():
        perfil.append(group.id)

    obj_access = Accesos.objects.filter(perfil__in=perfil)

    for page in obj_access:
        for url in page.urls.filter(is_active=True, is_visible=True).prefetch_related('get_urls').order_by('sort'):
            menu.append(url)

    app = App.objects.get(dominio = 'goevents.tech')

    return {
        'menu': menu,
        'app': app
    }
