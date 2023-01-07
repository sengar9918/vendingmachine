from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Department,Doctors_details,Patient_details
from django.http import JsonResponse
from datetime import timedelta,datetime
from datetime import datetime,timezone
import pprint

# Create your views here.
#dashboard
def home(request):
    d=Patient_details.objects.all()
    start=datetime.now(timezone.utc)
    data=[]
    for i in d:
        var={}
        var['patient_name']=i.patient_name
        var['token']=i.token
        var['start_time']=i.start_time
        var['end_time']=i.end_time
        if i.start_time < start < i.end_time:
            var['status']='Active'
        else:
            var['status']='InActive' 
        data.append(var)
    return render(request,"dash.html",{'data':data})

# for manage department
def manage_department(request):
    if request.method=="POST":
        dep_name=request.POST['dep_name']
        dep_id=dep_name[0:1].upper()
        Department.objects.create(department_name=dep_name,dep_id=dep_id)
    data=Department.objects.all()
    return render(request,"add_property.html",{'data':data})

# for manage doctor
def manage_doctor(request):
 
    if request.method=="POST":
        doctor_name=request.POST['doctor_name']
        doctor_id=doctor_name[0:2].upper()
        dep_id=request.POST['dep_id']
        id_dep=Department.objects.get(id=dep_id)
        token=id_dep.dep_id +"-"+ doctor_id 
        Doctors_details.objects.create(department=dep_id,doctor_name=doctor_name,doctor_id=doctor_id,dep_doc_id=token)
    data1=Department.objects.all()
    data=[]

    doctor_det=Doctors_details.objects.all()
    for i in doctor_det:
        var={}
        var['doctor_name']=i.doctor_name
        dep=i.department
        name=Department.objects.get(id=dep)

        var['department']=name.department_name
        data.append(var)
    
    return render(request,"add_doctor.html",{'data':data,'data1':data1})

# for manage patient
def manage_patient(request):
    if request.method=="POST":
        patient_name=request.POST['patient_name']
        dep_id=request.POST['dep_id']
        doctor_id=request.POST['doctor_id']
        doc=Doctors_details.objects.get(id=doctor_id,department=dep_id)
        token=doc.dep_doc_id+"-"+str(1)
        start=datetime.now(timezone.utc)
        start1=datetime.now(timezone.utc)
       
        end = datetime.now(timezone.utc) + timedelta(minutes=10)
        
        all_token=Patient_details.objects.filter(token__icontains=doc.dep_doc_id).values()
       
       
        if all_token :
            d=Patient_details.objects.values_list('start_time','end_time' )
            data12=Patient_details.objects.filter(token__icontains=doc.dep_doc_id,start_time__lte=start,end_time__gte=start)
            if data12:
            
                tok=[i.token.split('-')[-1]  for i in data12]
                num=int(max(tok))+1
                token1=doc.dep_doc_id+"-"+str(num)
               
                Patient_details.objects.create(doctor_id=doctor_id,department_id=dep_id,patient_name=patient_name,token=token1,start_time=start,end_time=end)
                return redirect('home')
            else:
                Patient_details.objects.create(doctor_id=doctor_id,department_id=dep_id,patient_name=patient_name,token=token,start_time=start,end_time=end)     
                return redirect('home')
        else: 
            Patient_details.objects.create(doctor_id=doctor_id,department_id=dep_id,patient_name=patient_name,token=token,start_time=start,end_time=end)
            return redirect('home')
    
    data1=Department.objects.all()
    return render(request,"add_patient.html",{'data1':data1})

# for dropdown value get in patient page
def get_property(request):
    if request.method=="POST":
        r=[]       
        id=request.POST['id']
        data=Doctors_details.objects.filter(department=id)
        for l in data:
            val={}
            val['id']=l.id
            val['doctor_name']=l.doctor_name
            
            r.append(val)
        

        return JsonResponse({'all':r })

# for reset 
def reset(request):
    today = datetime.today()
    Patient_details.objects.all().delete()
    return redirect('home')
    

