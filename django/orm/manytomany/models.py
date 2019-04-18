from django.db import models

# Create your models here.

# 병원에 오는 사람들을 기록하는 시스템을 만드려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떠한 관계로 표현할 수 있을까?

class Doctor(models.Model):
    name = models.TextField()
    # patients = models.ManyToManyField(Patient, through='Reservation') #아래 doctors와 둘 중 하나만 적기!
    # patient1.doctor_set.all() 
    
class Patient(models.Model):
    name = models.TextField()
    # Reservation을 통해서 doctor와 patient의 N:N관계를 형성
    # (의사와 예약이 1:N, 환자와 예약이 1:M이므로 의사와 환자가 M:N)
    doctors = models.ManyToManyField(Doctor, related_name='patients')#, through='Reservation') 
    #doctor1.patient_set.all(): reservation을 통하지않고 바로 의사의 환자를 불러옴
    # patient_set을 patients로 이름을 지정해줌
    
# 중계자 역할
# class Reservation(models.Model):
#     # Doctor:Reservation = 1:N 관계
#     # Patient:Reservation = 1:N 관계
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    
    
# doctor1 = Doctor.objects.create(name='kim')
# doctor2 = Doctor.objects.create(name='kang')
# patient1 = Patient.objects.create(name='tom')
# patient2 = Patient.objects.create(name='jhon')

# Reservation.objects.create(doctor=doctor1, patient=patient2)
# Reservation.objects.create(doctor=doctor1, patient=patient1)
# Reservation.objects.create(doctor=doctor2, patient=patient1)

# doctor1.patients.add(patient2)
# >>> doctor1.patients.all()
# >>> patient2.doctors.all()
# doctor1.patients.remove(patient2) == patient2.doctors.remove(doctor1)