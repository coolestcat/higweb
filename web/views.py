from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from firebase_token_generator import create_token
from django.contrib.auth import authenticate, login
from django.utils import timezone
import MySQLdb
import pandas as pd
import numpy.random as nr
import numpy
from random import randint
from datetime import datetime
from datetime import timedelta

current_time = datetime(2014, 8, 6, 12, 00, 00) # for patient 3, should be between Ready for MD Contour and Prescription Doc Fast Track
stages = ['Ct-Sim', 'READY FOR CONTOUR', 'READY FOR MD CONTOUR', 'Prescription Document (Fast Track)',
        'READY FOR DOSE CALCULATION', 'READY FOR PHYSICS QA', 'READY FOR TREATMENT']

def match(st, string_array):
    for i in range(len(string_array)):
        if st == string_array[i]:
            return i

    return -1

def getStage(id):
    st = "default"
    mysql_cn = MySQLdb.connect(host='localhost', port=3306,user='alvin', passwd='', db='hig')
    query = """
    SELECT a.AliasName, t.PatientSerNum, t.CreationDate, t.CompletionDate, t.Status
    FROM Task t INNER JOIN Patient p ON p.PatientSerNum = t.PatientSerNum 
        INNER JOIN Alias a ON a.AliasSerNum = t.AliasSerNum 
    WHERE p.PatientSerNum=%s
    UNION ALL 
    SELECT a.AliasName, ap.PatientserNum, ap.ScheduledStartTime, ap.ScheduledEndTime, ap.Status
    FROM Appointment ap INNER JOIN Patient p ON ap.PatientSerNum = p.PatientSerNum
        INNER JOIN Alias a ON a.AliasSerNum = ap.AliasSerNum
    WHERE p.PatientSerNum=%s
    UNION ALL 
    SELECT a.AliasName, p.PatientSerNum, p.PlanCreationDate, p.PlanCreationDate, p.Status
    FROM Plan p INNER JOIN Patient pa ON p.PatientSerNum = pa.PatientSerNum
        INNER JOIN Alias a ON a.AliasSerNum = p.AliasSerNum
    WHERE pa.PatientSerNum=%s
    UNION ALL
    SELECT DISTINCT a.AliasName, p.PatientSerNum, t.TreatmentDateTime, p.PlanCreationDate, p.Status 
    FROM TreatmentFieldHstry t INNER JOIN Plan p ON t.PlanSerNum = p.PlanSerNum
    INNER JOIN Alias a ON a.AliasSerNum = p.AliasSerNum
    INNER JOIN Patient pat ON pat.PatientSerNum = p.PatientSerNum
    WHERE pat.PatientSerNum=%s
    UNION ALL
    SELECT a.AliasName, d.PatientSerNum, d.ApprovedTimeStamp, d.DateOfService, d.ApprovalStatus
    FROM Document d INNER JOIN Patient p ON d.PatientSerNum = p.PatientSerNum
        INNER JOIN Alias a on d.AliasSerNum = a.AliasSerNum
    WHERE p.PatientSerNum=%s
    ORDER BY PatientSerNum, CreationDate""" % (id,id,id,id,id)

    df = pd.read_sql(query, con=mysql_cn)  
    i = 0
    time = datetime(1970, 7, 30, 12, 00, 00)
    bad_time = datetime(1970, 1, 1, 00, 00, 00)

    events = []

    # set current time to be random time between the first and last entry of the patient (for testing only)
    
    k = 0
    t_start = datetime.strptime(str(df.iloc[k,2]),"%Y-%m-%d %H:%M:%S")
    while (t_start == bad_time):
        k += 1
        t_start = datetime.strptime(str(df.iloc[k,2]),"%Y-%m-%d %H:%M:%S")

    t_end = datetime.strptime(str(df.iloc[len(df)-1,2]),"%Y-%m-%d %H:%M:%S")

    current_time = t_start + timedelta(seconds=randint(0, int((t_end - t_start).total_seconds())))

    print str(t_start)
    print str(t_end)
    print str(current_time)

    while (i<len(df)):
        time = datetime.strptime(str(df.iloc[i,2]),"%Y-%m-%d %H:%M:%S")
        if (time < current_time):
            events.append(str(df.iloc[i,0]))
        else:
            break
        i += 1

    for k in range(len(events)):
        this_str = events[len(events)-(k+1)]
        mat = match(this_str, stages)
        if mat!=-1:
            return stages[mat]
        else:
            continue

    print 'loaded dataframe. records:', len(df)
    mysql_cn.close()
    return st

# Create your views here.
def index(request):
    theUser = 3
    template = loader.get_template('web/index.html')
    context = RequestContext(request, {
        'theUser': theUser,
        # 'error_message' : 'Login Failed'
    })
    return HttpResponse(template.render(context))

def login(request):
	# this_user = request.GET['uname']
	# this_password = request.GET['pword']

	# error_str = "Invalid - %s, %s" % (this_user, this_password)
	# return render(request, 'web/index.html', {
    #   'error_message': error_str,
    # })
    this_user = request.GET['userid']
    ID = int(this_user)

    try:
        thisid = int(ID)
        st = getStage(thisid)

    except ValueError:
        raise Http404()

    html = "<html><body>This is the page for patient %s.\n This is the current stage %s</body></html>" % (thisid, st)
    return HttpResponse(html)

def create(request):
    return render(request, 'web/create_index.html', {
    })

def created(request):
	this_user = request.GET['uname']
	this_password = request.GET['pword']

	# auth_payload = {"uid": this_user, "pass": this_password}
	# token = create_token("VSzXP3WjD5XeQbBUtdjMxEWvUHU6yqyduBxjciM8", auth_payload)

	return render(request, 'web/create_index.html', {
            'error_message': 'Successfully Created User'
    })

def note(request):
    return render(request, 'web/note.html', {
    })







