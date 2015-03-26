from __future__ import unicode_literals

from tastypie.utils.timezone import now
from django.db import models


class Alias(models.Model):
    aliassernum = models.IntegerField(db_column='AliasSerNum', primary_key=True)  # Field name made lowercase.
    aliasname = models.CharField(db_column='AliasName', unique=True, max_length=100)  # Field name made lowercase.
    aliastype = models.CharField(db_column='AliasType', max_length=25)  # Field name made lowercase.
    aliasupdate = models.IntegerField(db_column='AliasUpdate')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alias'


class Aliasexpression(models.Model):
    aliasexpressionsernum = models.IntegerField(db_column='AliasExpressionSerNum', primary_key=True)  # Field name made lowercase.
    aliassernum = models.IntegerField(db_column='AliasSerNum')  # Field name made lowercase.
    expressionname = models.CharField(db_column='ExpressionName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AliasExpression'


class Appointment(models.Model):
    appointmentsernum = models.IntegerField(db_column='AppointmentSerNum', primary_key=True)  # Field name made lowercase.
    patientsernum = models.IntegerField(db_column='PatientSerNum')  # Field name made lowercase.
    appointmentid = models.IntegerField(db_column='AppointmentId', blank=True, null=True)  # Field name made lowercase.
    diagnosissernum = models.IntegerField(db_column='DiagnosisSerNum')  # Field name made lowercase.
    prioritysernum = models.IntegerField(db_column='PrioritySerNum')  # Field name made lowercase.
    aliassernum = models.IntegerField(db_column='AliasSerNum', blank=True, null=True)  # Field name made lowercase.
    aliasexpressionsernum = models.IntegerField(db_column='AliasExpressionSerNum')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True)  # Field name made lowercase.
    scheduledstarttime = models.DateTimeField(db_column='ScheduledStartTime', blank=True, null=True)  # Field name made lowercase.
    scheduledendtime = models.DateTimeField(db_column='ScheduledEndTime', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Appointment'


class Cron(models.Model):
    profile = models.IntegerField(db_column='Profile')  # Field name made lowercase.
    nextcron = models.DateField(db_column='NextCron')  # Field name made lowercase.
    repeatoption = models.CharField(db_column='RepeatOption', max_length=25)  # Field name made lowercase.
    repeattime = models.TimeField(db_column='RepeatTime')  # Field name made lowercase.
    lastcron = models.DateTimeField(db_column='LastCron')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cron'


class Diagnosis(models.Model):
    diagnosissernum = models.IntegerField(db_column='DiagnosisSerNum', primary_key=True)  # Field name made lowercase.
    patientsernum = models.IntegerField(db_column='PatientSerNum')  # Field name made lowercase.
    diagnosisid = models.CharField(db_column='DiagnosisId', max_length=25, blank=True)  # Field name made lowercase.
    diagnosiscreationdate = models.DateTimeField(db_column='DiagnosisCreationDate', blank=True, null=True)  # Field name made lowercase.
    diagnosiscode = models.CharField(db_column='DiagnosisCode', max_length=25, blank=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Diagnosis'


class Doctor(models.Model):
    doctorsernum = models.IntegerField(db_column='DoctorSerNum', primary_key=True)  # Field name made lowercase.
    oncologistflag = models.IntegerField(db_column='OncologistFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Doctor'


class Document(models.Model):
    documentsernum = models.IntegerField(db_column='DocumentSerNum', primary_key=True)  # Field name made lowercase.
    patientsernum = models.IntegerField(db_column='PatientSerNum')  # Field name made lowercase.
    documentid = models.CharField(db_column='DocumentId', max_length=30)  # Field name made lowercase.
    diagnosissernum = models.IntegerField(db_column='DiagnosisSerNum')  # Field name made lowercase.
    prioritysernum = models.IntegerField(db_column='PrioritySerNum')  # Field name made lowercase.
    approvalstatus = models.CharField(db_column='ApprovalStatus', max_length=11)  # Field name made lowercase.
    approvedbysernum = models.IntegerField(db_column='ApprovedBySerNum', blank=True, null=True)  # Field name made lowercase.
    approvedtimestamp = models.DateTimeField(db_column='ApprovedTimeStamp', blank=True, null=True)  # Field name made lowercase.
    authoredbysernum = models.IntegerField(db_column='AuthoredBySerNum')  # Field name made lowercase.
    dateofservice = models.DateTimeField(db_column='DateOfService')  # Field name made lowercase.
    aliassernum = models.IntegerField(db_column='AliasSerNum')  # Field name made lowercase.
    aliasexpressionsernum = models.IntegerField(db_column='AliasExpressionSerNum')  # Field name made lowercase.
    printed = models.CharField(db_column='Printed', max_length=5, blank=True)  # Field name made lowercase.
    signedbysernum = models.IntegerField(db_column='SignedBySerNum', blank=True, null=True)  # Field name made lowercase.
    signedtimestamp = models.DateTimeField(db_column='SignedTimeStamp', blank=True, null=True)  # Field name made lowercase.
    supervisedbysernum = models.IntegerField(db_column='SupervisedBySerNum', blank=True, null=True)  # Field name made lowercase.
    createdbysernum = models.IntegerField(db_column='CreatedBySerNum')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Document'


class Field(models.Model):
    fieldsernum = models.IntegerField(db_column='FieldSerNum', primary_key=True)  # Field name made lowercase.
    plansernum = models.IntegerField(db_column='PlanSerNum')  # Field name made lowercase.
    fieldid = models.IntegerField(db_column='FieldId')  # Field name made lowercase.
    fieldcreationdate = models.DateTimeField(db_column='FieldCreationDate')  # Field name made lowercase.
    gantryrtn = models.FloatField(db_column='GantryRtn')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Field'


class Patient(models.Model):
    patientsernum = models.IntegerField(db_column='PatientSerNum', primary_key=True)  # Field name made lowercase.
    dateofbirth = models.TextField(db_column='DateOfBirth', blank=True)  # Field name made lowercase. This field type is a guess.
    sex = models.CharField(db_column='Sex', max_length=11, blank=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=25)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patient'


class Patientdoctor(models.Model):
    patientdoctorsernum = models.IntegerField(db_column='PatientDoctorSerNum', primary_key=True)  # Field name made lowercase.
    patientsernum = models.IntegerField(db_column='PatientSerNum')  # Field name made lowercase.
    doctorsernum = models.IntegerField(db_column='DoctorSerNum')  # Field name made lowercase.
    oncologistflag = models.IntegerField(db_column='OncologistFlag')  # Field name made lowercase.
    primaryflag = models.IntegerField(db_column='PrimaryFlag')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PatientDoctor'


class Patientlocation(models.Model):
    patientlocationsernum = models.IntegerField(db_column='PatientLocationSerNum', primary_key=True)  # Field name made lowercase.
    appointmentsernum = models.IntegerField(db_column='AppointmentSerNum')  # Field name made lowercase.
    patientlocationid = models.IntegerField(db_column='PatientLocationId')  # Field name made lowercase.
    resourceser = models.IntegerField(db_column='ResourceSer')  # Field name made lowercase.
    revcount = models.IntegerField(db_column='RevCount')  # Field name made lowercase.
    checkedinflag = models.IntegerField(db_column='CheckedInFlag')  # Field name made lowercase.
    arrivaldatetime = models.DateTimeField(db_column='ArrivalDateTime')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PatientLocation'


class Patientlocationmh(models.Model):
    patientlocationmhsernum = models.IntegerField(db_column='PatientLocationMHSerNum', primary_key=True)  # Field name made lowercase.
    appointmentsernum = models.IntegerField(db_column='AppointmentSerNum')  # Field name made lowercase.
    patientlocationid = models.IntegerField(db_column='PatientLocationId')  # Field name made lowercase.
    resourceser = models.IntegerField(db_column='ResourceSer')  # Field name made lowercase.
    revcount = models.IntegerField(db_column='RevCount')  # Field name made lowercase.
    checkedinflag = models.IntegerField(db_column='CheckedInFlag')  # Field name made lowercase.
    arrivaldatetime = models.DateTimeField(db_column='ArrivalDateTime')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PatientLocationMH'


class Plan(models.Model):
    plansernum = models.IntegerField(db_column='PlanSerNum', primary_key=True)  # Field name made lowercase.
    patientsernum = models.IntegerField(db_column='PatientSerNum')  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId')  # Field name made lowercase.
    diagnosissernum = models.IntegerField(db_column='DiagnosisSerNum')  # Field name made lowercase.
    prioritysernum = models.IntegerField(db_column='PrioritySerNum')  # Field name made lowercase.
    aliassernum = models.IntegerField(db_column='AliasSerNum')  # Field name made lowercase.
    aliasexpressionsernum = models.IntegerField(db_column='AliasExpressionSerNum')  # Field name made lowercase.
    plancreationdate = models.DateTimeField(db_column='PlanCreationDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=100)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Plan'


class Priority(models.Model):
    prioritysernum = models.IntegerField(db_column='PrioritySerNum', primary_key=True)  # Field name made lowercase.
    patientsernum = models.IntegerField(db_column='PatientSerNum')  # Field name made lowercase.
    priorityid = models.CharField(db_column='PriorityId', max_length=25, blank=True)  # Field name made lowercase.
    prioritydatetime = models.DateTimeField(db_column='PriorityDateTime', blank=True, null=True)  # Field name made lowercase.
    prioritycode = models.CharField(db_column='PriorityCode', max_length=25, blank=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Priority'


class Staff(models.Model):
    staffsernum = models.IntegerField(db_column='StaffSerNum', primary_key=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staff'


class Study(models.Model):
    studysernum = models.IntegerField(db_column='StudySerNum', primary_key=True)  # Field name made lowercase.
    usersernum = models.IntegerField(db_column='UserSerNum')  # Field name made lowercase.
    studyname = models.CharField(db_column='StudyName', max_length=100)  # Field name made lowercase.
    relativeplot = models.IntegerField(db_column='RelativePlot')  # Field name made lowercase.
    binwidth = models.IntegerField(db_column='BinWidth')  # Field name made lowercase.
    thresholdtype = models.CharField(db_column='ThresholdType', max_length=100)  # Field name made lowercase.
    thresholdpercent = models.IntegerField(db_column='ThresholdPercent', blank=True, null=True)  # Field name made lowercase.
    histdataseriestype = models.CharField(db_column='HistDataSeriesType', max_length=25)  # Field name made lowercase.
    histdatastartdate = models.DateField(db_column='HistDataStartDate')  # Field name made lowercase.
    histdataenddate = models.DateField(db_column='HistDataEndDate')  # Field name made lowercase.
    currdataseriestype = models.CharField(db_column='CurrDataSeriesType', max_length=25)  # Field name made lowercase.
    currdatastartdate = models.DateField(db_column='CurrDataStartDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Study'


class Studydiagnosisfilter(models.Model):
    studydiagnosisfiltersernum = models.IntegerField(db_column='StudyDiagnosisFilterSerNum', primary_key=True)  # Field name made lowercase.
    studysernum = models.IntegerField(db_column='StudySerNum')  # Field name made lowercase.
    filtername = models.TextField(db_column='FilterName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudyDiagnosisFilter'


class Studypriorityfilter(models.Model):
    studypriorityfiltersernum = models.IntegerField(db_column='StudyPriorityFilterSerNum', primary_key=True)  # Field name made lowercase.
    studysernum = models.IntegerField(db_column='StudySerNum')  # Field name made lowercase.
    filtername = models.CharField(db_column='FilterName', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudyPriorityFilter'


class Studythreshold(models.Model):
    thresholdsernum = models.IntegerField(db_column='ThresholdSerNum', primary_key=True)  # Field name made lowercase.
    studysernum = models.IntegerField(db_column='StudySerNum')  # Field name made lowercase.
    minimum = models.IntegerField(db_column='Minimum')  # Field name made lowercase.
    maximum = models.IntegerField(db_column='Maximum')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudyThreshold'


class Task(models.Model):
    tasksernum = models.IntegerField(db_column='TaskSerNum', primary_key=True)  # Field name made lowercase.
    patientsernum = models.IntegerField(db_column='PatientSerNum')  # Field name made lowercase.
    taskid = models.IntegerField(db_column='TaskId', blank=True, null=True)  # Field name made lowercase.
    diagnosissernum = models.IntegerField(db_column='DiagnosisSerNum')  # Field name made lowercase.
    prioritysernum = models.IntegerField(db_column='PrioritySerNum')  # Field name made lowercase.
    aliassernum = models.IntegerField(db_column='AliasSerNum')  # Field name made lowercase.
    aliasexpressionsernum = models.IntegerField(db_column='AliasExpressionSerNum')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    duedatetime = models.DateTimeField(db_column='DueDateTime', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    completiondate = models.DateTimeField(db_column='CompletionDate', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Task'


class Timedelaystudy(models.Model):
    timedelaystudysernum = models.IntegerField(db_column='TimeDelayStudySerNum', primary_key=True)  # Field name made lowercase.
    studysernum = models.IntegerField(db_column='StudySerNum')  # Field name made lowercase.
    startaliassernum = models.IntegerField(db_column='StartAliasSerNum')  # Field name made lowercase.
    starttimestampname = models.CharField(db_column='StartTimeStampName', max_length=100)  # Field name made lowercase.
    startstatuses = models.CharField(db_column='StartStatuses', max_length=100, blank=True)  # Field name made lowercase.
    endaliassernum = models.IntegerField(db_column='EndAliasSerNum')  # Field name made lowercase.
    endtimestampname = models.CharField(db_column='EndTimeStampName', max_length=100)  # Field name made lowercase.
    endstatuses = models.CharField(db_column='EndStatuses', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeDelayStudy'


class Treatmentfieldhstry(models.Model):
    treatmentfieldhstrysernum = models.IntegerField(db_column='TreatmentFieldHstrySerNum', primary_key=True)  # Field name made lowercase.
    plansernum = models.IntegerField(db_column='PlanSerNum')  # Field name made lowercase.
    treatmentfieldhstryid = models.IntegerField(db_column='TreatmentFieldHstryId')  # Field name made lowercase.
    treatmentdatetime = models.DateTimeField(db_column='TreatmentDateTime')  # Field name made lowercase.
    gantryrtn = models.FloatField(db_column='GantryRtn')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TreatmentFieldHstry'


class Treatmentparameterstudy(models.Model):
    treatmentparameterstudysernum = models.IntegerField(db_column='TreatmentParameterStudySerNum', primary_key=True)  # Field name made lowercase.
    studysernum = models.IntegerField(db_column='StudySerNum')  # Field name made lowercase.
    aliassernum = models.IntegerField(db_column='AliasSerNum')  # Field name made lowercase.
    treatmentparameterfield = models.CharField(db_column='TreatmentParameterField', max_length=100)  # Field name made lowercase.
    treatmentparameterdisplayname = models.CharField(db_column='TreatmentParameterDisplayName', max_length=100)  # Field name made lowercase.
    treatmentparameterunits = models.CharField(db_column='TreatmentParameterUnits', max_length=100)  # Field name made lowercase.
    planstatus = models.CharField(db_column='PlanStatus', max_length=100)  # Field name made lowercase.
    polarplot = models.IntegerField(db_column='PolarPlot')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TreatmentParameterStudy'


class User(models.Model):
    usersernum = models.IntegerField(db_column='UserSerNum', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class Venue(models.Model):
    venuesernum = models.IntegerField(db_column='VenueSerNum', primary_key=True)  # Field name made lowercase.
    venuename = models.CharField(db_column='VenueName', max_length=50)  # Field name made lowercase.
    resourceser = models.IntegerField(db_column='ResourceSer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Venue'


class Entry(models.Model):
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title
