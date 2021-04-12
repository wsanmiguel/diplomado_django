class Appointment():

    def __init__(self, id, doctor, patient, date_, time_, description=""):
        self.id = id
        self.doctor = doctor
        self.patient = patient
        self.date_ = date_
        self.time_ = time_
        self.description = description

    def setNote(self, description):
        self.description = description

    def __str__(self):
        return '''
        Doctor: {} - {} 
        Paciente: {} - {}
        Fecha: {}
        Hora: {} '''.format(self.doctor.id, self.doctor.full_name(), self.patient.id, self.patient.full_name(), self.date_, self.time_) 

    def __gt__(self, appointment):
        return self.doctor.id > appointment.doctor.id and self.date_ > appointment.date and self.time_ > appointment.time_

    def get_attend(self):
        return not self.description == ""
