from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
import pymongo
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method=='POST':
        user=request.POST.get('unm')
        pwd=request.POST.get('pwd')
        user=authenticate(username=user, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            client=pymongo.MongoClient('mongodb://localhost:27017')
            db=client['placement']
            col=db['student']
            td=col.count_documents({})
            tp=col.count_documents({"choice":"Placements"})
            th=col.count_documents({"choice":"Higher Studies"})
            te=col.count_documents({"choice":"Entrepreneurship (Deferred Placements)"})
            content={'td':td, 'tp':tp, 'th':th, 'te':te}
            return render (request,"base.html", content)
        
        else:
            messages.add_message(request, messages.INFO, "Wrong username or password")
            return render (request, 'index.html')
    else:
        return render (request, 'index.html')

def home(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        if request.method=="POST":
            search=request.POST.get('rno')
            search=int(search)
            client=pymongo.MongoClient('mongodb://localhost:27017')
            db=client['placement']
            col=db['student']
            getinfo=col.find({"rollno":search})
            print(getinfo)
            td=col.count_documents({})
            tp=col.count_documents({"choice":"Placements"})
            th=col.count_documents({"choice":"Higher Studies"})
            te=col.count_documents({"choice":"Entrepreneurship (Deferred Placements)"})
            to=col.count_documents({"choice":"Other Career options"})
            tetotal=te+to
            viewinfo={'getinfo':getinfo,'td':td, 'tp':tp, 'th':th, 'te':tetotal}
            return render (request, 'base.html',viewinfo) 
        else:
            client=pymongo.MongoClient('mongodb://localhost:27017')
            db=client['placement']
            col=db['student']
            td=col.count_documents({})
            tp=col.count_documents({"choice":"Placements"})
            th=col.count_documents({"choice":"Higher Studies"})
            te=col.count_documents({"choice":"Entrepreneurship (Deferred Placements)"})
            to=col.count_documents({"choice":"Other Career options"})
            tetotal=te+to
            viewinfo={'td':td, 'tp':tp, 'th':th, 'te':tetotal}
            return render (request, 'base.html',viewinfo) 


def placements(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        client=pymongo.MongoClient('mongodb://localhost:27017')
        db=client['placement']
        col=db['student']
        getinfo=col.find({"choice":"Placements"})
        ch="Placements"
        viewinfo={"getinfo":getinfo,"ch":ch}
        print(viewinfo)
        return render(request,'details.html', viewinfo)

def higherstudies(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        client=pymongo.MongoClient('mongodb://localhost:27017')
        db=client['placement']
        col=db['student']
        getinfo=col.find({"choice":"Higher Studies"})
        ch="Higher Studies"
        viewinfo={"getinfo":getinfo, "ch":ch}
        print(viewinfo)
        return render(request,'details.html', viewinfo)

def entre(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        client=pymongo.MongoClient('mongodb://localhost:27017')
        db=client['placement']
        col=db['student']
        getinfo=col.find({"$or":[{"choice":"Entrepreneurship (Deferred Placements)"},{"choice":"Other Career options"}]})
        # info=col.find({"choice":"Other Career options"})
        ch="Entrepreneurship (Deferred Placements)/Other Career Options"
        viewinfo={"getinfo":getinfo,"ch":ch,}
        print(viewinfo)
        return render(request,'totalstuds.html', viewinfo)

def totalstuds(request):
    if request.user.is_anonymous:
        return redirect('/')
    else:
        client=pymongo.MongoClient('mongodb://localhost:27017')
        db=client['placement']
        col=db['student']
        getinfo=col.find({})
        ch="Total Students"
        viewinfo={"getinfo":getinfo,"ch":ch}
        print(viewinfo)
        return render(request,'totalstuds.html', viewinfo)

def logoutuser(request):
    logout(request)
    return redirect ('/')