from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),  # Se agrega el URL de polls
    path('admin/', admin.site.urls),  # include() te permite utilizar otro URL CONFIGS
]  # lo que hace es que mocha el URL desde lo especificado
# y lo manda al URL CONFIG especificado
