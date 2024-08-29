from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.register,name="register"),
    path("home",views.home,name="home"),
    path("category/<category>/",views.category,name="category"),
    path("categoryTittle/<tittle>/",views.categoryTittle,name="categoryTittle"),
    path("product_details/<int:id>/",views.product_details,name="product_details"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    # path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("profile/",views.profile,name="profile"),
    path("userRegister/",views.userRegister,name="userRegister"),
    path("userLogin/",views.userLogin,name="userLogin"),
    path("userProfile/",views.userProfile,name="userProfile"),
    path("cPassword/",views.cPassword,name="cPassword"),
    path("editProfile/<Email>/",views.editProfile,name="editProfile"),
    path("updateProfile/<Email>/",views.updateProfile,name="updateProfile"),
    path("changePassword/<Email>/",views.changePassword,name="changePassword"),
    path("add_to_cart/",views.add_to_cart,name="add_to_cart"),
    path("show_cart/",views.show_cart,name="show_cart"),
    path("pluscart/",views.pluscart,name="pluscart"),
    path("minuscart/",views.minuscart,name="minuscart"),
    path("removecart/",views.removecart,name="removecart"),
    path("checkOut/",views.checkOut,name="checkOut"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)