from django import template

register = template.Library()

@register.filter(name="reverse_int")
def reverse_int(num):
    int_revers = int(str(num)[::-1])
    return int_revers

register.filter(name='iran_format')
def iran_format(phone, delimiter="-"):
    if len(phone) != 11 or not phone.isdigit() or not phone.startswith("09"):
        return phone

    return f"{phone[:4]}{delimiter}{phone[4:7]}{delimiter}{phone[7:]}"

@register.filter(name="revers_str")
def reverse_str(value):
    return value[::-1]