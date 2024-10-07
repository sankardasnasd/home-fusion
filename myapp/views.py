import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    if 'submit' in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        a=Login.objects.filter(username=username,password=password)
        if a.exists():
            b = Login.objects.get(username=username, password=password)
            request.session['lid']=b.id
            if b.type=='admin':
                return HttpResponse('''<script>alert("Login successfully ");window.location='/adminhome'</script>''')
            elif b.type == 'owner':
                return HttpResponse('''<script>alert("Login successfully ");window.location='/owner_home'</script>''')
            elif b.type == 'user':

                return HttpResponse('''<script>alert("Login successfully ");window.location='/user_home'</script>''')
            else:
                return HttpResponse('''<script>alert("Invalid ");window.location='/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid ");window.location='/'</script>''')
    return  render(request,'loginindex.html')

def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')


def admin_change_password(request):

    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    if 'submit' in request.POST:
        old=request.POST['old']
        new=request.POST['new']
        confirm=request.POST['confirm']

        a=Login.objects.filter(password=old,id=request.session['lid'])
        if a.exists():
            if new == confirm:
                Login.objects.filter(id=request.session['lid']).update(password=confirm)
                return HttpResponse(
                    '''<script>alert('Successfully changed');window.location='/'</script>''')
            else:
                return HttpResponse(
                    '''<script>alert('Password Mismatch');window.location='/admin_change_password'</script>''')

        else:
            return HttpResponse(
                '''<script>alert('Password Mismatch');window.location='/admin_change_password'</script>''')
    return render(request,'admin/admin_change_password.html')



def adminhome(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    return render(request,'admin/adminindex.html')

def admin_add_owner(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    if 'submit' in request.POST:
        name=request.POST['name']
        place=request.POST['place']
        post=request.POST['post']
        district=request.POST['district']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        image=request.FILES['image']

        fs=FileSystemStorage()
        date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.jpg'
        fs.save(date,image)
        path=fs.url(date)

        a=Login()
        a.username=email
        a.password=password
        a.type='owner'
        a.save()

        o=Owner()
        o.LOGIN=a
        o.name=name
        o.place=place
        o.post=post
        o.district=district
        o.email=email
        o.phone=phone
        o.image=path
        o.save()
        return HttpResponse('''<script>alert(" successfully ");window.location='/adminhome'</script>''')


    return render(request,'admin/add_owner.html')



def admin_view_owner(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    a=Owner.objects.all()
    return render(request,'admin/view owner.html',{'data':a})


def delete_owner(request,id):
    a=Owner.objects.get(id=id)
    a.delete()
    a.LOGIN.delete()
    return HttpResponse('''<script>alert("Deleted successfully ");window.location='/adminhome'</script>''')

def admin_edit_owner(request,id):
    a=Owner.objects.get(id=id)
    return render(request,'admin/edi_owner.html',{'data':a})

def admin_edit_owner_post(request):
    id = request.POST['id']
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    district = request.POST['district']
    phone = request.POST['phone']

    o=Owner.objects.get(id=id)
    if 'image' in request.FILES:
        image = request.FILES['image']

        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        fs.save(date, image)
        path = fs.url(date)
        o.image=path
    o.name = name
    o.place = place
    o.post = post
    o.district = district
    o.phone = phone
    o.save()
    return HttpResponse('''<script>alert("Edited successfully ");window.location='/admin_view_owner'</script>''')





def admin_view_complaints(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    a=Complaints.objects.all()
    return render(request,'admin/view complaints.html',{'data':a})

def sendreply(request,id):
    a=Complaints.objects.get(id=id)
    return render(request,'admin/sendreply.html',{'data':a})

def sendreply_post(request):
    id=request.POST['id']
    reply=request.POST['reply']

    a=Complaints.objects.get(id=id)
    a.reply=reply
    a.save()
    return HttpResponse('''<script>alert("Replied ");window.location='/admin_view_complaints'</script>''')


def admin_view_property(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    var=Property.objects.all()
    return render(request,'admin/view property.html',{'data':var})



def approve_property(request,id):
    a=Property.objects.filter(id=id).update(status='approved')
    return HttpResponse('''<script>alert("Approved ");window.location='/admin_view_property'</script>''')


def reject_property(request,id):
    a=Property.objects.filter(id=id).update(status='rejected')
    return HttpResponse('''<script>alert("Rejected ");window.location='/admin_view_property'</script>''')


def owner_home(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    return render(request,'owner/ownerindex.html')


def add_property(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    if 'submit' in request.POST:
        name=request.POST['name']
        price=request.POST['price']
        type=request.POST['type']
        latitude=request.POST['latitude']
        longitude=request.POST['longitude']
        details=request.POST['details']

        image = request.FILES['image']

        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        fs.save(date, image)
        path = fs.url(date)

        a=Property()
        a.OWNER=Owner.objects.get(LOGIN_id=request.session['lid'])
        a.name=name
        a.price=price
        a.type=type
        a.latitude=latitude
        a.longitude=longitude
        a.details=details
        a.image=path
        a.status='pending'
        a.save()
        return HttpResponse('''<script>alert("Added ");window.location='/add_property'</script>''')

    return  render(request,'owner/addproperty.html')

def owner_view_propery(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    a=Property.objects.filter(OWNER__LOGIN_id=request.session['lid'])
    return  render(request,'owner/ownerview property.html',{'data':a})


def owner_viewprofile(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    a=Owner.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'owner/viewprofile.html',{'user':a})



def onwer_view_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    var=Booking.objects.filter(PROPERTY__OWNER__LOGIN_id=request.session['lid'])
    return render(request,'owner/view booking.html',{'data':var})


def approve_booking(request,id):
    a=Booking.objects.filter(id=id).update(status='Approved')
    return HttpResponse('''<script>alert("Approved ");window.location='/onwer_view_booking'</script>''')
def reject_booking(request,id):
    a=Booking.objects.filter(id=id).update(status='Rejected')
    return HttpResponse('''<script>alert("Rejected ");window.location='/onwer_view_booking'</script>''')


def onwer_view_property_rating(request,id):
    var=Rating.objects.filter(PROPERTY_id=id)
    return render(request,'owner/owner_view_property_rating.html',{'data':var})

def owner_update_property(request,id):
    a=Property.objects.get(id=id)
    return render(request,'owner/update_property_status.html',{'data':a})


def owner_update_property_post(request):
    id=request.POST['id']
    select=request.POST['select']

    a=Property.objects.get(id=id)
    a.status=select
    a.save()
    return HttpResponse('''<script>alert("Updated ");window.location='/owner_view_propery'</script>''')




def user_reg(request):
    if 'submit' in request.POST:
        name=request.POST['name']
        place=request.POST['place']
        gender=request.POST['gender']
        idproof=request.POST['idproof']
        post=request.POST['post']
        district=request.POST['district']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        image = request.FILES['image']

        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        fs.save(date, image)
        path = fs.url(date)

        l=Login()
        l.username=email
        l.password=confirm_password
        l.type='user'
        l.save()

        u=User()
        u.LOGIN=l
        u.image=path
        u.name=name
        u.email=email
        u.phone=phone
        u.place=place
        u.gender=gender
        u.idproof=idproof
        u.district=district
        u.post=post
        u.save()
        return HttpResponse('''<script>alert("Register Success ");window.location='/'</script>''')

    return render(request,'user/reg.html')



def user_home(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    a=Property.objects.all()
    return render(request,'user/userindex.html',{'data':a})
def user_view_profile(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    var=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/user view_profile.html',{'user':var})


def user_edit_profile(request):
    var=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/user_edit_profile.html',{'user':var})


def user_edit_profile_post(request):
    id=request.POST['id']
    name = request.POST['name']
    place = request.POST['place']
    gender = request.POST['gender']
    idproof = request.POST['idproof']
    post = request.POST['post']
    district = request.POST['district']
    email = request.POST['email']
    phone = request.POST['phone']

    u=User.objects.get(id=id)
    if 'image' in request.FILES:
        image = request.FILES['image']

        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        fs.save(date, image)
        path = fs.url(date)
        u.image = path
    u.name = name
    u.email = email
    u.phone = phone
    u.place = place
    u.gender = gender
    u.idproof = idproof
    u.district = district
    u.post = post
    u.save()
    return HttpResponse('''<script>alert("Update Success ");window.location='/user_viewprofile'</script>''')

def user_view_property(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    var=Property.objects.all()
    return render(request,'user/user view property.html',{'data':var})


def user_send_rating(request,id):
    var=Property.objects.get(id=id)
    return render(request,'user/send rating.html',{'data':var})


def user_send_rating_post(request):
    id=request.POST['id']
    rating=request.POST['star']
    review=request.POST['review']

    a=Rating()
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.date=datetime.datetime.now().today().date()
    a.PROPERTY=Property.objects.get(id=id)
    a.review=review
    a.rating=rating
    a.save()
    return HttpResponse('''<script>alert(" Sent ");window.location='/user_view_property'</script>''')


def user_book_property(request,id):
    var=Property.objects.get(id=id)
    user=User.objects.get(LOGIN_id=request.session['lid'])
    old = Booking.objects.filter(PROPERTY=var, USER=user).exists()

    if old:
        return HttpResponse(
            '''<script>alert("You have already booked this property.");window.location='/user_view_property'</script>''')

    a=Booking()
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.date=datetime.datetime.now().today().date()
    a.amount=var.price
    a.PROPERTY=Property.objects.get(id=var.id)

    a.status='booking pending'
    a.save()

    var.status='booking pending'
    var.save()
    return HttpResponse('''<script>alert("Booking Pending ");window.location='/user_view_property'</script>''')

def user_view_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    var=Booking.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'user/user view booking.html',{'data':var})

def sent_notification(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    if 'submit' in request.POST:
        notification=request.POST['notification']
        var=Notification()
        var.notification=notification
        var.date=datetime.datetime.now().today().date()
        var.save()
        return HttpResponse('''<script>alert("Added ");window.location='/sent_notification'</script>''')

    return render(request,'admin/sent notification.html')


def admin_view_notification(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    var=Notification.objects.all
    return render(request,'admin/view notification.html',{'data':var})

def user_view_notification(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    var = Notification.objects.all().order_by('-id')
    return render(request, 'user/user view notification.html', {'data': var})

def sent_complaint(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout success ");window.location='/'</script>''')

    var=Complaints.objects.filter(USER__LOGIN_id=request.session['lid'])
    if 'submit' in request.POST:
        complaint=request.POST['complaint']
        a=Complaints()
        a.USER=User.objects.get(LOGIN_id=request.session['lid'])
        a.date=datetime.datetime.now().today().date()
        a.reply='pending'
        a.complaints=complaint
        a.save()
        return HttpResponse('''<script>alert("Sent ");window.location='/sent_complaint'</script>''')
    return render(request,'user/sent complaint.html',{'data':var})


def owner_chat_to_user(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = Booking.objects.get(USER__LOGIN=cid)
    print(qry.USER.LOGIN_id,'login----------')

    return render(request, "owner/Chat.html", {'photo': qry.USER.image, 'name': qry.USER.name, 'toid': cid})


def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = Booking.objects.get(USER__LOGIN_id=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
    l = []
    print(qry.USER.name,'userssssssssss')

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

    return JsonResponse({'photo': qry.USER.image, "data": l, 'name': qry.USER.name, 'toid': request.session["userid"]})


def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})



def user_chat1(request,id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = Booking.objects.get(PROPERTY__OWNER__LOGIN=cid)
    print('owner -----------',qry.PROPERTY.OWNER.name)

    return render(request, "user/Chat.html", {'photo': qry.PROPERTY.OWNER.image, 'name': qry.PROPERTY.OWNER.name, 'toid': cid})


def userchat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = Booking.objects.get(PROPERTY__OWNER__LOGIN_id=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
    l = []
    print(qry.PROPERTY.OWNER.name,'OWNERSSSSS')

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

    return JsonResponse({'photo': qry.PROPERTY.OWNER.image, "data": l, 'name': qry.PROPERTY.OWNER.name, 'toid': request.session["userid"]})


def userchat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    print('login_id-----',lid,'toid---',toid,'messageee---',message)

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})



