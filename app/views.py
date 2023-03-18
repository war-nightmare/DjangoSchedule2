from django.shortcuts import render, redirect, HttpResponse
from app import models
from calendar import weekday
import time
import datetime


# Create your views here.
def index(request):
    class_monday = models.Monday.objects.all().order_by("classstart")
    class_tuesday = models.Tuesday.objects.all().order_by("classstart")
    class_wednesday = models.Wednesday.objects.all().order_by("classstart")
    class_thursday = models.Thursday.objects.all().order_by("classstart")
    class_friday = models.Friday.objects.all().order_by("classstart")
    return render(request, "index.html", {'class_monday':class_monday, 'class_tuesday':class_tuesday, 'class_wednesday':class_wednesday, 'class_thursday':class_thursday, 'class_friday':class_friday})

def delete(request):
    nid = request.GET.get('nid')[:-1]
    date = request.GET.get('nid')[-1:]
    if date == '1':
        models.Monday.objects.filter(id=nid).delete()
    elif date == '2':
        models.Tuesday.objects.filter(id=nid).delete()
    elif date == '3':
        models.Wednesday.objects.filter(id=nid).delete()
    elif date == '4':
        models.Thursday.objects.filter(id=nid).delete()
    elif date == '5':
        models.Friday.objects.filter(id=nid).delete()
    return redirect("../")

def add(request):
    if request.method == 'GET':
        return render(request, "add.html")

    else:
        classdate = request.POST.get("classdate")
        classname = request.POST.get("classname")
        classstart = int(request.POST.get("classstart").replace(":",""))
        classend = int(request.POST.get("classend").replace(":",""))
        if classdate == "礼拜一":
            models.Monday.objects.create(classname=classname, classstart=classstart, classend=classend)
        elif classdate == "礼拜二":
            models.Tuesday.objects.create(classname=classname, classstart=classstart, classend=classend)
        elif classdate == "礼拜三":
            models.Wednesday.objects.create(classname=classname, classstart=classstart, classend=classend)
        elif classdate == "礼拜四":
            models.Thursday.objects.create(classname=classname, classstart=classstart, classend=classend)
        elif classdate == "礼拜五":
            models.Friday.objects.create(classname=classname, classstart=classstart, classend=classend)
        return redirect("../")

def edit(request):
    nid = request.GET.get('nid')[:-1]
    date = request.GET.get('nid')[-1:]
    if request.method == 'GET':
        monday = ""
        tuesday = ""
        wednesday = ""
        thursday = ""
        friday = ""
        if date == '1':
            row_object = models.Monday.objects.filter(id=nid).first()
            monday = 'selected'
        elif date == '2':
            row_object = models.Tuesday.objects.filter(id=nid).first()
            tuesday = 'selected'
        elif date == '3':
            row_object = models.Wednesday.objects.filter(id=nid).first()
            wednesday  = 'selected'
        elif date == '4':
            row_object = models.Thursday.objects.filter(id=nid).first()
            thursday = 'selected'
        elif date == '5':
            row_object = models.Friday.objects.filter(id=nid).first()
            friday  = 'selected'
        return render(request, "edit.html", {"row_object":row_object,"monday":monday,"tuesday":tuesday,"wednesday":wednesday,"thursday":thursday,"friday":friday})

    else:
        classname = request.POST.get("classname")
        classstart = int(request.POST.get("classstart").replace(":",""))
        classend = int(request.POST.get("classend").replace(":",""))
        if date == '1':
            models.Monday.objects.filter(id=nid).update(classname=classname, classstart=classstart, classend=classend)
        elif date == '2':
            models.Tuesday.objects.filter(id=nid).update(classname=classname, classstart=classstart, classend=classend)
        elif date == '3':
            models.Wednesday.objects.filter(id=nid).update(classname=classname, classstart=classstart, classend=classend)
        elif date == '4':
            models.Thursday.objects.filter(id=nid).update(classname=classname, classstart=classstart, classend=classend)
        elif date == '5':
            models.Friday.objects.filter(id=nid).update(classname=classname, classstart=classstart, classend=classend)

        return redirect("../")

def show(request):
    class_monday = models.Monday.objects.all().order_by('classstart')
    class_tuesday = models.Tuesday.objects.all().order_by('classstart')
    class_wednesday = models.Wednesday.objects.all().order_by('classstart')
    class_thursday = models.Thursday.objects.all().order_by('classstart')
    class_friday = models.Friday.objects.all().order_by('classstart')

    dismonday = models.dismonday.objects.all()
    distuesday = models.distuesday.objects.all()
    diswednesday = models.diswednesday.objects.all()
    disthursday = models.disthursday.objects.all()
    disfriday = models.disfriday.objects.all()

    disclass_monday = []
    disclass_tuesday = []
    disclass_wednesday = []
    disclass_thursday = []
    disclass_friday = []

    for i in dismonday.values_list('theclass',flat=True):
        disclass_monday.append(i)
    for i in distuesday.values_list('theclass',flat=True):
        disclass_tuesday.append(i)
    for i in diswednesday.values_list('theclass',flat=True):
        disclass_wednesday.append(i)
    for i in disthursday.values_list('theclass',flat=True):
        disclass_thursday.append(i)
    for i in disfriday.values_list('theclass',flat=True):
        disclass_friday.append(i)

    ids_monday = []
    classstart_monday = []
    classend_monday = []
    classes_monday = []

    ids_tuesday = []
    classstart_tuesday = []
    classend_tuesday = []
    classes_tuesday = []

    ids_wednesday = []
    classstart_wednesday = []
    classend_wednesday = []
    classes_wednesday = []

    ids_thursday = []
    classstart_thursday = []
    classend_thursday = []
    classes_thursday = []

    ids_friday = []
    classstart_friday = []
    classend_friday = []
    classes_friday = []
    for i in class_monday.values_list(flat=True):
        ids_monday.append(i)
    for i in class_tuesday.values_list(flat=True):
        ids_tuesday.append(i)
    for i in class_wednesday.values_list(flat=True):
        ids_wednesday.append(i)
    for i in class_thursday.values_list(flat=True):
        ids_thursday.append(i)
    for i in class_friday.values_list(flat=True):
        ids_friday.append(i)
    
    a=0
    for i in ids_monday:
        classstart_monday.append(str(list(models.Monday.objects.filter(id=i).values_list('classstart', flat=True)))[1:-1])
        classend_monday.append(str(list(models.Monday.objects.filter(id=i).values_list('classend', flat=True)))[1:-1])
        classes_monday.append((str(list(models.Monday.objects.filter(id=i).values_list('classname', flat=True))))[2:-2])
        a+=1
    a=0
    for i in ids_tuesday:
        classstart_tuesday.append(str(list(models.Tuesday.objects.filter(id=i).values_list('classstart', flat=True)))[1:-1])
        classend_tuesday.append(str(list(models.Tuesday.objects.filter(id=i).values_list('classend', flat=True)))[1:-1])
        classes_tuesday.append((str(list(models.Tuesday.objects.filter(id=i).values_list('classname', flat=True))))[2:-2])
        a+=1
    a=0
    for i in ids_wednesday:
        classstart_wednesday.append(str(list(models.Wednesday.objects.filter(id=i).values_list('classstart', flat=True)))[1:-1])
        classend_wednesday.append(str(list(models.Wednesday.objects.filter(id=i).values_list('classend', flat=True)))[1:-1])
        classes_wednesday.append((str(list(models.Wednesday.objects.filter(id=i).values_list('classname', flat=True))))[2:-2])
        a+=1
    a=0
    for i in ids_thursday:
        classstart_thursday.append(str(list(models.Thursday.objects.filter(id=i).values_list('classstart', flat=True)))[1:-1])
        classend_thursday.append(str(list(models.Thursday.objects.filter(id=i).values_list('classend', flat=True)))[1:-1])
        classes_thursday.append((str(list(models.Thursday.objects.filter(id=i).values_list('classname', flat=True))))[2:-2])
        a+=1
    a=0
    for i in ids_friday:
        classstart_friday.append(str(list(models.Friday.objects.filter(id=i).values_list('classstart', flat=True)))[1:-1])
        classend_friday.append(str(list(models.Friday.objects.filter(id=i).values_list('classend', flat=True)))[1:-1])
        classes_friday.append((str(list(models.Friday.objects.filter(id=i).values_list('classname', flat=True))))[2:-2])
        a+=1

    for i in range(len(classstart_monday)):
        if len(classstart_monday[i]) == 3:
            classstart_monday[i] = "0" + classstart_monday[i]
    for i in range(len(classend_monday)):
        if len(classend_monday[i]) == 3:
            classend_monday[i] = "0" + classend_monday[i]

    for i in range(len(classstart_tuesday)):
        if len(classstart_tuesday[i]) == 3:
            classstart_tuesday[i] = "0" + classstart_tuesday[i]
    for i in range(len(classend_tuesday)):
        if len(classend_tuesday[i]) == 3:
            classend_tuesday[i] = "0" + classend_tuesday[i]

    for i in range(len(classstart_wednesday)):
        if len(classstart_wednesday[i]) == 3:
            classstart_wednesday[i] = "0" + classstart_wednesday[i]
    for i in range(len(classend_wednesday)):
        if len(classend_wednesday[i]) == 3:
            classend_wednesday[i] = "0" + classend_wednesday[i]

    for i in range(len(classstart_thursday)):
        if len(classstart_thursday[i]) == 3:
            classstart_thursday[i] = "0" + classstart_thursday[i]
    for i in range(len(classend_thursday)):
        if len(classend_thursday[i]) == 3:
            classend_thursday[i] = "0" + classend_thursday[i]

    for i in range(len(classstart_friday)):
        if len(classstart_friday[i]) == 3:
            classstart_friday[i] = "0" + classstart_friday[i]
    for i in range(len(classend_friday)):
        if len(classend_friday[i]) == 3:
            classend_friday[i] = "0" + classend_friday[i]

    curr_time = datetime.datetime.now()
    week_day = curr_time.isoweekday()

    def calculateclass():
        from calendar import weekday
        import time
        import datetime

        timestamp=datetime.datetime.strftime(curr_time,'%H%M')

        if week_day == 1:
            for i in range(len(classstart_monday)):
                if int(timestamp) < int(classstart_monday[0]):
                    d_hour = int((classstart_monday[0])[0:2]) - int(timestamp[0:2])
                    d_min = int((classstart_monday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_monday[0], d_hour, d_min)
                if int(timestamp) >= int(classend_monday[len(classend_monday)-1]):
                    d_hour = int((classstart_tuesday[0])[0:2]) - int(timestamp[0:2]) + 24
                    d_min = int((classstart_tuesday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_tuesday[0], d_hour, d_min)
                if int(timestamp) >= int(classstart_monday[i]) and int(timestamp) < int(classend_monday[i]):
                    d_hour = int((classend_monday[i])[0:2]) - int(timestamp[0:2])
                    d_min = int((classend_monday[i])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    if i == len(classstart_monday)-1:
                        d_hour = int((classend_tuesday[0])[0:2]) - int(timestamp[0:2]) + 24
                        d_min = int((classend_tuesday[0])[2:]) - int(timestamp[2:])
                        if d_min < 0:
                            d_hour-=1
                            d_min+=60
                        return (classes_monday[i], classes_tuesday[0], d_hour, d_min)
                    else:
                        return (classes_monday[i], classes_monday[i+1], d_hour, d_min)
        elif week_day == 2:
            for i in range(len(classstart_tuesday)):
                if int(timestamp) < int(classstart_tuesday[0]):
                    d_hour = int((classstart_tuesday[0])[0:2]) - int(timestamp[0:2])
                    d_min = int((classstart_tuesday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_tuesday[0], d_hour, d_min)
                if int(timestamp) >= int(classend_tuesday[len(classend_tuesday)-1]):
                    d_hour = int((classstart_wednesday[0])[0:2]) - int(timestamp[0:2]) + 24
                    d_min = int((classstart_wednesday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_wednesday[0], d_hour, d_min)
                if int(timestamp) >= int(classstart_tuesday[i]) and int(timestamp) < int(classend_tuesday[i]):
                    d_hour = int((classend_tuesday[i])[0:2]) - int(timestamp[0:2])
                    d_min = int((classend_tuesday[i])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    if i == len(classstart_tuesday)-1:
                        d_hour = int((classend_wednesday[0])[0:2]) - int(timestamp[0:2]) + 24
                        d_min = int((classend_wednesday[0])[2:]) - int(timestamp[2:])
                        if d_min < 0:
                            d_hour-=1
                            d_min+=60
                        return (classes_tuesday[i], classes_wednesday[0], d_hour, d_min)
                    else:
                        return (classes_tuesday[i], classes_tuesday[i+1], d_hour, d_min)
        elif week_day == 3:
            for i in range(len(classstart_wednesday)):
                if int(timestamp) < int(classstart_wednesday[0]):
                    d_hour = int((classstart_wednesday[0])[0:2]) - int(timestamp[0:2])
                    d_min = int((classstart_wednesday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_wednesday[0], d_hour, d_min)
                if int(timestamp) >= int(classend_wednesday[len(classend_wednesday)-1]):
                    d_hour = int((classstart_thursday[0])[0:2]) - int(timestamp[0:2]) + 24
                    d_min = int((classstart_thursday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_thursday[0], d_hour, d_min)
                if int(timestamp) >= int(classstart_wednesday[i]) and int(timestamp) < int(classend_wednesday[i]):
                    d_hour = int((classend_wednesday[i])[0:2]) - int(timestamp[0:2])
                    d_min = int((classend_wednesday[i])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    if i == len(classstart_wednesday)-1:
                        d_hour = int((classend_thursday[0])[0:2]) - int(timestamp[0:2]) + 24
                        d_min = int((classend_thursday[0])[2:]) - int(timestamp[2:])
                        if d_min < 0:
                            d_hour-=1
                            d_min+=60
                        return (classes_wednesday[i], classes_thursday[0], d_hour, d_min)
                    else:
                        return (classes_wednesday[i], classes_wednesday[i+1], d_hour, d_min)
        elif week_day == 4:
            for i in range(len(classstart_thursday)):
                if int(timestamp) < int(classstart_thursday[0]):
                    d_hour = int((classstart_thursday[0])[0:2]) - int(timestamp[0:2])
                    d_min = int((classstart_thursday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_thursday[0], d_hour, d_min)
                if int(timestamp) >= int(classend_thursday[len(classend_thursday)-1]):
                    d_hour = int((classstart_friday[0])[0:2]) - int(timestamp[0:2]) + 24
                    d_min = int((classstart_friday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_friday[0], d_hour, d_min)
                if int(timestamp) >= int(classstart_thursday[i]) and int(timestamp) < int(classend_thursday[i]):
                    d_hour = int((classend_thursday[i])[0:2]) - int(timestamp[0:2])
                    d_min = int((classend_thursday[i])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    if i == len(classstart_thursday)-1:
                        d_hour = int((classend_friday[0])[0:2]) - int(timestamp[0:2]) + 24
                        d_min = int((classend_friday[0])[2:]) - int(timestamp[2:])
                        if d_min < 0:
                            d_hour-=1
                            d_min+=60
                        return (classes_thursday[i], classes_friday[0], d_hour, d_min)
                    else:
                        return (classes_thursday[i], classes_thursday[i+1], d_hour, d_min)
        elif week_day == 5:
            for i in range(len(classstart_friday)):
                if int(timestamp) < int(classstart_friday[0]):
                    d_hour = int((classstart_friday[0])[0:2]) - int(timestamp[0:2])
                    d_min = int((classstart_friday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_friday[0], d_hour, d_min)
                if int(timestamp) >= int(classend_friday[len(classend_friday)-1]):
                    d_hour = int((classstart_monday[0])[0:2]) - int(timestamp[0:2]) + 72
                    d_min = int((classstart_monday[0])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    return ("没课", classes_monday[0], d_hour, d_min)
                if int(timestamp) >= int(classstart_friday[i]) and int(timestamp) < int(classend_friday[i]):
                    d_hour = int((classend_friday[i])[0:2]) - int(timestamp[0:2])
                    d_min = int((classend_friday[i])[2:]) - int(timestamp[2:])
                    if d_min < 0:
                        d_hour-=1
                        d_min+=60
                    if i == len(classstart_friday)-1:
                        d_hour = int((classend_monday[0])[0:2]) - int(timestamp[0:2]) + 72
                        d_min = int((classend_monday[0])[2:]) - int(timestamp[2:])
                        if d_min < 0:
                            d_hour-=1
                            d_min+=60
                        return (classes_friday[i], classes_monday[0], d_hour, d_min)
                    else:
                        return (classes_friday[i], classes_friday[i+1], d_hour, d_min)

        elif week_day == 6:
            d_hour = int((classend_monday[0])[0:2]) - int(timestamp[0:2]) + 48
            d_min = int((classend_monday[0])[2:]) - int(timestamp[2:])
            if d_min < 0:
                d_hour-=1
                d_min+=60
            return ("没课", classes_monday[0], d_hour, d_min)

        elif week_day == 7:
            d_hour = int((classend_monday[0])[0:2]) - int(timestamp[0:2]) + 24
            d_min = int((classend_monday[0])[2:]) - int(timestamp[2:])
            if d_min < 0:
                d_hour-=1
                d_min+=60
            return ("没课", classes_monday[0], d_hour, d_min)

    class_now = calculateclass()[0]
    class_next = calculateclass()[1]
    d_hour = calculateclass()[2]
    d_min = calculateclass()[3]

    time_tuple = time.localtime(time.time())
    weekday_lst = ["一","二","三","四","五","六","天"]
    weekday_display = weekday_lst[week_day-1]
    time_msg=("现在是{}年{}月{}日    礼拜{}    {}点{}分{}秒".format(time_tuple[0],time_tuple[1],time_tuple[2],weekday_display,time_tuple[3],time_tuple[4],time_tuple[5]))

    return render(request, "show.html", {'class_now':class_now, 'class_next':class_next, 'd_hour':d_hour, 'd_min':d_min, 'time_msg':time_msg, 'disclass_monday':disclass_monday, 'disclass_tuesday':disclass_tuesday, 'disclass_wednesday':disclass_wednesday, 'disclass_thursday':disclass_thursday, 'disclass_friday':disclass_friday})