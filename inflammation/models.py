"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains

inflammation data for a single patient taken over a number of days

and each column represents a single day across all patients.
"""


import numpy as np
class Observation:
    def __init__(self, day, value):
        self.day = day 
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

# class Doctor(Person):
    
#     def __init__(self, name):
#         super().__init__(name)
#         self.patients = []

#     @property
#     def patient_names(self):
#         return [p.name for p in self.patients]    

#     def add_patient(self, new_patient):
#         if new_patient not in self.patients:
#             self.patients.append(new_patient)

class Patient(Person):

    def __init__(self, name, observations=None):
        super().__init__(name)
        self.observations = []
        if observations is not None:
            self.observations = observations

    @property
    def last_observation(self):
        return self.observations[-1]

    def add_observations(self, value, day=None):
        '''
        Args:
            value(_type_): _description
            day (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description

        '''
        if day is None:
            if self.observations:
                day = self.observations[-1].day+ 1

            else:
                day = 0

        new_observation = Observation(day, value)
        self.observations.append(new_observation)
        return new_observation


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array."""
    return np.min(data, axis=0)

<<<<<<< HEAD
def patient_normalise(data):
    ''''Normalise patient data from 2D array of inflammation data'''
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    maxes = np.nanmax(data, axis=1)
    normalised = data/maxes[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised
=======

def patient_normalise(data):
    '''Normalise patient data from 2D array of inflammation data'''
    maxes = np.max(data, axis = 0)
    return data / maxes[:, np.newaxis]
>>>>>>> 4dd85b5d82ff12a4a1465683fa2477e72b83243c
