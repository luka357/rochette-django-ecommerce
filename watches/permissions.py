from rest_framework.permissions import BasePermission, SAFE_METHODS


# ყველას შეუძლია ნახვა (GET), ცვლილება მხოლოდ ადმინს (is_staff)
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
