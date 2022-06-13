from django.http import JsonResponse
from django.shortcuts import render
import openpyxl
from django.db.models import Sum, Q
from main.models import Book, COURSE_CHOICES
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    context = {
        "be_book_count":Book.objects.filter(course="BE").aggregate(Sum('count')),
        "mba_book_count":Book.objects.filter(course="MBA").aggregate(Sum('count')),
        "mca_book_count":Book.objects.filter(course="MCA").aggregate(Sum('count')),
        "mtech_book_count":Book.objects.filter(course="MTech").aggregate(Sum('count')),
        "total_books_count":Book.objects.aggregate(Sum('count')),
        "courses":COURSE_CHOICES
    }
    if request.method == "POST":
        query = request.POST.get("search")
        results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(department__icontains=query) ).order_by("title")
        context["results"] = results
        context["search_result"] = True
    return render(request, "main/index.html", context)


def book_detail(request, id):
    context = {
        "book":Book.objects.get(id=id)
    }
    return render(request, "main/book_detail.html", context)


@csrf_exempt
def get_departments(request):
    departments = Book.objects.filter(course = 'BE').distinct().values_list("department", flat=True)
    return JsonResponse({'departments':list(departments)})

def upload(request):
    context = dict()
    if request.method == "POST":
        file = request.FILES.get("excel")
        wb = openpyxl.load_workbook(file, read_only=True)
        sheet = wb.active
        fields = [field.name for field in Book._meta.fields]
        fields.remove("id")
        for row in sheet.iter_rows(min_row=2):
            row_value = [x.value for x in row]
            nary = dict(zip(fields, row_value))
            Book.objects.get_or_create(**nary)
        context["uploaded"] = True
    context["row_count"] = Book.objects.count() 
    return render(request, "main/upload.html", context)
