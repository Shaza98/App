from django.http import HttpResponse

# Create your views here.
#import xlwt

# from django.http import HttpResponse
# from django.contrib.auth.models import User

# def export_users_xls(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="users.xls"'

#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('Users')

#     # Sheet header, first row
#     row_num = 0

#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True

#     columns = ['Name', 'Email', 'Phone', ]

#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)

#     # Sheet body, remaining rows
#     font_style = xlwt.XFStyle()

#     rows = User.objects.all().values_list('Name','Email','Phone')
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)

#     wb.save(response)
#     return response


def index(request):
    return HttpResponse("<h1> Go to http://127.0.0.1:8000/admin/First/person/add/ to insert a new person in the database ")