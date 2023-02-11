from tkinter import FALSE
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,  logout
from django.contrib.auth import  login as log
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Q
from data.models import stresults
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver

def homepage(request):
    return render(request,'homepage.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('login')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('login')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('login')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('login')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please Login To Continue..")
        return render(request, 'homepage.html')
    return render(request, 'signup.html')

    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            request.session['username'] = username
            log(request,user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            
            return redirect('homepage')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('login')

    return render(request, "login.html") 


            

     
def signout(request):
    del request.session['username']
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('homepage')
   
def results(request):
    if request.session.has_key('username'):
       return render(request,'results.html')
    else:
        return redirect('/homepage')
            
    
@login_required(login_url='login')
def search(request):
    
    found_rst = None
    if ('rnum' in request.POST) and request.POST['rnum'].strip() and ('nme' in request.POST) and request.POST.get('nme',FALSE).strip()and ('dob' in request.POST) and request.POST['dob'].strip():
        
        found_rst = stresults.objects.filter(rnum__iexact=request.POST['rnum'],nme__iexact=request.POST.get('nme',FALSE),dob__iexact=request.POST['dob'])
        if found_rst:
            return render(request,'search.html',
            {  'found_rst': found_rst })
        
        else:
            messages.error(request,'No Result Found')
            return render(request,'results.html')
        
    

      # if request.method == 'POST':
    #     # rnum = request.POST['rnum']
          
        

        
    #     # res = stresults.objects.using('users').filter(rnum=request.POST['rnum']).exists
    #     # if res :    
    #     #     return render(request,'search.html',{'res': res} )
             
    #     # else:
    #     #     messages.error(request,'No Result Found')
    #     #     return render(request,'results.html') 
#      query = ''
#      found_rst = None
#      if ('q' in request.GET) and request.GET['q'].strip():
#         query_string = request.GET['q']
#         entry_query = get_query(query_string, ['field1', 'field2', 'field3'])
#         found_entries = Model.objects.filter(entry_query).order_by('-something')

#     return render('app/template-result.html',
#             { 'query_string': query_string, 'found_entries': found_entries },
#             context_instance=RequestContext(request)
#         )


        # r = request.GET.get('rnum',None)
        # n = request.GET.get('nme',None)
        # d = request.GET.get('dob',None)
        
        # res = stresults.objects.using('users').filter(Q(rnum__icontains=r) | Q(nme__icontains=n) | Q(dob__icontains=d))
        # if r and n and d in res:
        #     dt = stresults.objects.using('users').all()
         
        #     return render(request,'search.html',{dt:'dt'})
        

        # else: 
        #     messages.error(request,'no result found')
        #     return render(request, 'results.html')  
            
        
        
       

      
        
    
    # 

    # if request.method == "GET":

    #     query = request.GET.get('search')

    #     if query == '':

    #         query = 'None'

    #     results = stresults.objects.using('users').filter(Q(rnum__icontains=query) | Q(nme__icontains=query) | Q(dob__icontains=query)|Q(result__icontains=query))
    # {'query': query, 'results': results}
    

    

    
    
       
         
          



    
       
    
    
        

    return render(request,'results.html')    
 