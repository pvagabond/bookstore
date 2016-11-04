from django.conf.urls import url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.store, name='index'),
    url('^book/(\d+)', views.book_details, name='book_details'),
    url('^add/(\d+)', views.add_to_cart, name='add_to_cart'),
    url('^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url('^cart/', views.cart, name='cart'),
]
