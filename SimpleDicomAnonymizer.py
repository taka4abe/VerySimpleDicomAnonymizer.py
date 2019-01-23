# this code works at
#   ./Patient/Study/Series/DICOMimages
#
# this code anonymizes Dicom files (PatientName) with "" (empty str).
#
# this code depends on os and pydicom==1.2.1 libralies.

import os
import pydicom as dicom

total = 0

for Patient in os.listdir('.'):
    for Study in os.listdir(Patient):
        for Series in os.listdir(Patient + '/' + Study):
            try:
                path = "../Anonymized/" + Patient + '/' +\
                       Study + '/' + Series
                os.makedirs(path)
                print("os.makedirs:", path)
                total += 1
            except:
                print('failed to prepare anonymized dir "../Anonymized"')
                pass

print("A total of", total, "dirs.")
n = 0

for Patient in os.listdir('.'):
    if Patient == 'Anonymized':
        pass
    else:
        for Study in os.listdir(Patient):
            for Series in os.listdir(Patient + '/' + Study):
                n += 1
                print("Anonymizing: " +  Patient + '/' + Study + ", " + n + "/" + total)
                for file_name in os.listdir(Patient + '/' + Study + '/' + Series):
                    path = Patient + '/' + Study + '/' + Series + '/' + file_name
                    #print(path)
                    try:
                        ds = dicom.dcmread(Patient + '/' + Study + '/' + Series +
                                             '/' + file_name)
                    except:
                        print('failed to read dicom file')
                        pass
                    try:
                        ds.PatientName = ""
                    except:
                        print('failed to anonymize')
                        pass
                    try:
                        ds.save_as("../Anonymized/" + path)
                    except:
                        print('failed to save dicom file')
                        pass

print('done!')
