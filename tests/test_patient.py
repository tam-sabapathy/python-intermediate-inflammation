"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Sheila Wheels'
    doc = Doctor(name=name)

    assert doc.name == name

def test_doctor_is_person():
    from inflammation.models import Doctor, Person

    doc = Doctor('Sheila Wheels')

    assert isinstance(doc, Person)


def test_patient_is_person():
    from inflammation.models import Patient, Person

    p = Patient('Alice')

    assert isinstance(p, Person)

def test_patients_added_correctly():
    
    from inflammation.models import Patient, Doctor
    doc = Doctor('Sheila Wheels')
    alice = Patient('Alice')
    doc.add_patient(alice)
    assert doc.patients is not None
    assert len(doc.patients) == 1


def test_no_duplicate_patients():
    
    from inflammation.models import Patient, Doctor
    doc = Doctor('Sheila Wheels')
    alice = Patient('Alice')
    doc.add_patient(alice)
    doc.add_patient(alice)
    assert len(doc.patients) == 1


