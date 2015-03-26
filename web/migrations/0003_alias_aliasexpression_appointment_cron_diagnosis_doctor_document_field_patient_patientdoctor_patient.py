# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150320_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('aliassernum', models.IntegerField(serialize=False, primary_key=True, db_column='AliasSerNum')),
                ('aliasname', models.CharField(unique=True, max_length=100, db_column='AliasName')),
                ('aliastype', models.CharField(max_length=25, db_column='AliasType')),
                ('aliasupdate', models.IntegerField(db_column='AliasUpdate')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Alias',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Aliasexpression',
            fields=[
                ('aliasexpressionsernum', models.IntegerField(serialize=False, primary_key=True, db_column='AliasExpressionSerNum')),
                ('aliassernum', models.IntegerField(db_column='AliasSerNum')),
                ('expressionname', models.CharField(max_length=100, db_column='ExpressionName')),
            ],
            options={
                'db_table': 'AliasExpression',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointmentsernum', models.IntegerField(serialize=False, primary_key=True, db_column='AppointmentSerNum')),
                ('patientsernum', models.IntegerField(db_column='PatientSerNum')),
                ('appointmentid', models.IntegerField(null=True, db_column='AppointmentId', blank=True)),
                ('diagnosissernum', models.IntegerField(db_column='DiagnosisSerNum')),
                ('prioritysernum', models.IntegerField(db_column='PrioritySerNum')),
                ('aliassernum', models.IntegerField(null=True, db_column='AliasSerNum', blank=True)),
                ('aliasexpressionsernum', models.IntegerField(db_column='AliasExpressionSerNum')),
                ('status', models.CharField(max_length=50, db_column='Status', blank=True)),
                ('scheduledstarttime', models.DateTimeField(null=True, db_column='ScheduledStartTime', blank=True)),
                ('scheduledendtime', models.DateTimeField(null=True, db_column='ScheduledEndTime', blank=True)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Appointment',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cron',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile', models.IntegerField(db_column='Profile')),
                ('nextcron', models.DateField(db_column='NextCron')),
                ('repeatoption', models.CharField(max_length=25, db_column='RepeatOption')),
                ('repeattime', models.TimeField(db_column='RepeatTime')),
                ('lastcron', models.DateTimeField(db_column='LastCron')),
            ],
            options={
                'db_table': 'Cron',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosissernum', models.IntegerField(serialize=False, primary_key=True, db_column='DiagnosisSerNum')),
                ('patientsernum', models.IntegerField(db_column='PatientSerNum')),
                ('diagnosisid', models.CharField(max_length=25, db_column='DiagnosisId', blank=True)),
                ('diagnosiscreationdate', models.DateTimeField(null=True, db_column='DiagnosisCreationDate', blank=True)),
                ('diagnosiscode', models.CharField(max_length=25, db_column='DiagnosisCode', blank=True)),
                ('description', models.TextField(db_column='Description')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Diagnosis',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorsernum', models.IntegerField(serialize=False, primary_key=True, db_column='DoctorSerNum')),
                ('oncologistflag', models.IntegerField(db_column='OncologistFlag')),
            ],
            options={
                'db_table': 'Doctor',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('documentsernum', models.IntegerField(serialize=False, primary_key=True, db_column='DocumentSerNum')),
                ('patientsernum', models.IntegerField(db_column='PatientSerNum')),
                ('documentid', models.CharField(max_length=30, db_column='DocumentId')),
                ('diagnosissernum', models.IntegerField(db_column='DiagnosisSerNum')),
                ('prioritysernum', models.IntegerField(db_column='PrioritySerNum')),
                ('approvalstatus', models.CharField(max_length=11, db_column='ApprovalStatus')),
                ('approvedbysernum', models.IntegerField(null=True, db_column='ApprovedBySerNum', blank=True)),
                ('approvedtimestamp', models.DateTimeField(null=True, db_column='ApprovedTimeStamp', blank=True)),
                ('authoredbysernum', models.IntegerField(db_column='AuthoredBySerNum')),
                ('dateofservice', models.DateTimeField(db_column='DateOfService')),
                ('aliassernum', models.IntegerField(db_column='AliasSerNum')),
                ('aliasexpressionsernum', models.IntegerField(db_column='AliasExpressionSerNum')),
                ('printed', models.CharField(max_length=5, db_column='Printed', blank=True)),
                ('signedbysernum', models.IntegerField(null=True, db_column='SignedBySerNum', blank=True)),
                ('signedtimestamp', models.DateTimeField(null=True, db_column='SignedTimeStamp', blank=True)),
                ('supervisedbysernum', models.IntegerField(null=True, db_column='SupervisedBySerNum', blank=True)),
                ('createdbysernum', models.IntegerField(db_column='CreatedBySerNum')),
                ('createdtimestamp', models.DateTimeField(db_column='CreatedTimeStamp')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Document',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('fieldsernum', models.IntegerField(serialize=False, primary_key=True, db_column='FieldSerNum')),
                ('plansernum', models.IntegerField(db_column='PlanSerNum')),
                ('fieldid', models.IntegerField(db_column='FieldId')),
                ('fieldcreationdate', models.DateTimeField(db_column='FieldCreationDate')),
                ('gantryrtn', models.FloatField(db_column='GantryRtn')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Field',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientsernum', models.IntegerField(serialize=False, primary_key=True, db_column='PatientSerNum')),
                ('dateofbirth', models.TextField(db_column='DateOfBirth', blank=True)),
                ('sex', models.CharField(max_length=11, db_column='Sex', blank=True)),
                ('postalcode', models.CharField(max_length=25, db_column='PostalCode')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Patient',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patientdoctor',
            fields=[
                ('patientdoctorsernum', models.IntegerField(serialize=False, primary_key=True, db_column='PatientDoctorSerNum')),
                ('patientsernum', models.IntegerField(db_column='PatientSerNum')),
                ('doctorsernum', models.IntegerField(db_column='DoctorSerNum')),
                ('oncologistflag', models.IntegerField(db_column='OncologistFlag')),
                ('primaryflag', models.IntegerField(db_column='PrimaryFlag')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'PatientDoctor',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patientlocation',
            fields=[
                ('patientlocationsernum', models.IntegerField(serialize=False, primary_key=True, db_column='PatientLocationSerNum')),
                ('appointmentsernum', models.IntegerField(db_column='AppointmentSerNum')),
                ('patientlocationid', models.IntegerField(db_column='PatientLocationId')),
                ('resourceser', models.IntegerField(db_column='ResourceSer')),
                ('revcount', models.IntegerField(db_column='RevCount')),
                ('checkedinflag', models.IntegerField(db_column='CheckedInFlag')),
                ('arrivaldatetime', models.DateTimeField(db_column='ArrivalDateTime')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'PatientLocation',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patientlocationmh',
            fields=[
                ('patientlocationmhsernum', models.IntegerField(serialize=False, primary_key=True, db_column='PatientLocationMHSerNum')),
                ('appointmentsernum', models.IntegerField(db_column='AppointmentSerNum')),
                ('patientlocationid', models.IntegerField(db_column='PatientLocationId')),
                ('resourceser', models.IntegerField(db_column='ResourceSer')),
                ('revcount', models.IntegerField(db_column='RevCount')),
                ('checkedinflag', models.IntegerField(db_column='CheckedInFlag')),
                ('arrivaldatetime', models.DateTimeField(db_column='ArrivalDateTime')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'PatientLocationMH',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plansernum', models.IntegerField(serialize=False, primary_key=True, db_column='PlanSerNum')),
                ('patientsernum', models.IntegerField(db_column='PatientSerNum')),
                ('planid', models.IntegerField(db_column='PlanId')),
                ('diagnosissernum', models.IntegerField(db_column='DiagnosisSerNum')),
                ('prioritysernum', models.IntegerField(db_column='PrioritySerNum')),
                ('aliassernum', models.IntegerField(db_column='AliasSerNum')),
                ('aliasexpressionsernum', models.IntegerField(db_column='AliasExpressionSerNum')),
                ('plancreationdate', models.DateTimeField(db_column='PlanCreationDate')),
                ('status', models.CharField(max_length=100, db_column='Status')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Plan',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('prioritysernum', models.IntegerField(serialize=False, primary_key=True, db_column='PrioritySerNum')),
                ('patientsernum', models.IntegerField(db_column='PatientSerNum')),
                ('priorityid', models.CharField(max_length=25, db_column='PriorityId', blank=True)),
                ('prioritydatetime', models.DateTimeField(null=True, db_column='PriorityDateTime', blank=True)),
                ('prioritycode', models.CharField(max_length=25, db_column='PriorityCode', blank=True)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Priority',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staffsernum', models.IntegerField(serialize=False, primary_key=True, db_column='StaffSerNum')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Staff',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('studysernum', models.IntegerField(serialize=False, primary_key=True, db_column='StudySerNum')),
                ('usersernum', models.IntegerField(db_column='UserSerNum')),
                ('studyname', models.CharField(max_length=100, db_column='StudyName')),
                ('relativeplot', models.IntegerField(db_column='RelativePlot')),
                ('binwidth', models.IntegerField(db_column='BinWidth')),
                ('thresholdtype', models.CharField(max_length=100, db_column='ThresholdType')),
                ('thresholdpercent', models.IntegerField(null=True, db_column='ThresholdPercent', blank=True)),
                ('histdataseriestype', models.CharField(max_length=25, db_column='HistDataSeriesType')),
                ('histdatastartdate', models.DateField(db_column='HistDataStartDate')),
                ('histdataenddate', models.DateField(db_column='HistDataEndDate')),
                ('currdataseriestype', models.CharField(max_length=25, db_column='CurrDataSeriesType')),
                ('currdatastartdate', models.DateField(db_column='CurrDataStartDate')),
            ],
            options={
                'db_table': 'Study',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Studydiagnosisfilter',
            fields=[
                ('studydiagnosisfiltersernum', models.IntegerField(serialize=False, primary_key=True, db_column='StudyDiagnosisFilterSerNum')),
                ('studysernum', models.IntegerField(db_column='StudySerNum')),
                ('filtername', models.TextField(db_column='FilterName')),
            ],
            options={
                'db_table': 'StudyDiagnosisFilter',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Studypriorityfilter',
            fields=[
                ('studypriorityfiltersernum', models.IntegerField(serialize=False, primary_key=True, db_column='StudyPriorityFilterSerNum')),
                ('studysernum', models.IntegerField(db_column='StudySerNum')),
                ('filtername', models.CharField(max_length=1000, db_column='FilterName')),
            ],
            options={
                'db_table': 'StudyPriorityFilter',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Studythreshold',
            fields=[
                ('thresholdsernum', models.IntegerField(serialize=False, primary_key=True, db_column='ThresholdSerNum')),
                ('studysernum', models.IntegerField(db_column='StudySerNum')),
                ('minimum', models.IntegerField(db_column='Minimum')),
                ('maximum', models.IntegerField(db_column='Maximum')),
            ],
            options={
                'db_table': 'StudyThreshold',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('tasksernum', models.IntegerField(serialize=False, primary_key=True, db_column='TaskSerNum')),
                ('patientsernum', models.IntegerField(db_column='PatientSerNum')),
                ('taskid', models.IntegerField(null=True, db_column='TaskId', blank=True)),
                ('diagnosissernum', models.IntegerField(db_column='DiagnosisSerNum')),
                ('prioritysernum', models.IntegerField(db_column='PrioritySerNum')),
                ('aliassernum', models.IntegerField(db_column='AliasSerNum')),
                ('aliasexpressionsernum', models.IntegerField(db_column='AliasExpressionSerNum')),
                ('status', models.CharField(max_length=50, db_column='Status')),
                ('duedatetime', models.DateTimeField(null=True, db_column='DueDateTime', blank=True)),
                ('creationdate', models.DateTimeField(null=True, db_column='CreationDate', blank=True)),
                ('completiondate', models.DateTimeField(null=True, db_column='CompletionDate', blank=True)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'Task',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timedelaystudy',
            fields=[
                ('timedelaystudysernum', models.IntegerField(serialize=False, primary_key=True, db_column='TimeDelayStudySerNum')),
                ('studysernum', models.IntegerField(db_column='StudySerNum')),
                ('startaliassernum', models.IntegerField(db_column='StartAliasSerNum')),
                ('starttimestampname', models.CharField(max_length=100, db_column='StartTimeStampName')),
                ('startstatuses', models.CharField(max_length=100, db_column='StartStatuses', blank=True)),
                ('endaliassernum', models.IntegerField(db_column='EndAliasSerNum')),
                ('endtimestampname', models.CharField(max_length=100, db_column='EndTimeStampName')),
                ('endstatuses', models.CharField(max_length=100, db_column='EndStatuses')),
            ],
            options={
                'db_table': 'TimeDelayStudy',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Treatmentfieldhstry',
            fields=[
                ('treatmentfieldhstrysernum', models.IntegerField(serialize=False, primary_key=True, db_column='TreatmentFieldHstrySerNum')),
                ('plansernum', models.IntegerField(db_column='PlanSerNum')),
                ('treatmentfieldhstryid', models.IntegerField(db_column='TreatmentFieldHstryId')),
                ('treatmentdatetime', models.DateTimeField(db_column='TreatmentDateTime')),
                ('gantryrtn', models.FloatField(db_column='GantryRtn')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
            ],
            options={
                'db_table': 'TreatmentFieldHstry',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Treatmentparameterstudy',
            fields=[
                ('treatmentparameterstudysernum', models.IntegerField(serialize=False, primary_key=True, db_column='TreatmentParameterStudySerNum')),
                ('studysernum', models.IntegerField(db_column='StudySerNum')),
                ('aliassernum', models.IntegerField(db_column='AliasSerNum')),
                ('treatmentparameterfield', models.CharField(max_length=100, db_column='TreatmentParameterField')),
                ('treatmentparameterdisplayname', models.CharField(max_length=100, db_column='TreatmentParameterDisplayName')),
                ('treatmentparameterunits', models.CharField(max_length=100, db_column='TreatmentParameterUnits')),
                ('planstatus', models.CharField(max_length=100, db_column='PlanStatus')),
                ('polarplot', models.IntegerField(db_column='PolarPlot')),
            ],
            options={
                'db_table': 'TreatmentParameterStudy',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('usersernum', models.IntegerField(serialize=False, primary_key=True, db_column='UserSerNum')),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venuesernum', models.IntegerField(serialize=False, primary_key=True, db_column='VenueSerNum')),
                ('venuename', models.CharField(max_length=50, db_column='VenueName')),
                ('resourceser', models.IntegerField(db_column='ResourceSer')),
            ],
            options={
                'db_table': 'Venue',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
