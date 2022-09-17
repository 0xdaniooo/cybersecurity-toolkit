from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('hex-to-ascii/', views.HexToAscii, name="hex-to-ascii"),
    path('ascii-to-hex/', views.AsciiToHex, name="ascii-to-hex"),
    path('hex-to-decimal/', views.HexToDecimal, name="hex-to-decimal"),
    path('decimal-to-hex/', views.DecimalToHex, name="decimal-to-hex"),
    path('base64-encode/', views.Base64Encode, name="base64-encode"),
    path('base64-decode/', views.Base64Decode, name="base64-decode"),
    path('ascii-table/', views.AsciiTable, name="ascii-table"),
    path('general-conversion/', views.GeneralConversion, name="general-conversion"),
    path('xor-calculator/', views.XorCalculator, name="xor-calculator"),
]