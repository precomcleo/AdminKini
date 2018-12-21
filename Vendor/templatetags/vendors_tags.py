from django.template import Library

register = Library()

@register.filter
def deletable(vendor, user):
    return vendor.can_user_delete(user)