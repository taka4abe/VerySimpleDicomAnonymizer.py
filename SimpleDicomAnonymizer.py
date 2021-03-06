# this code works at
#   ./Patient/Study/Series/DICOMimages
#
# this code anonymizes Dicom files (PatientName) with "" (empty str).
#
# this code depends on os and pydicom==1.2.1 libralies.

import os
import pydicom as dicom

total = 0

cwd = os.getcwd()
root, cwd_name = cwd.rsplit("/", 1)

for Patient in os.listdir('.'):
    for Study in os.listdir(Patient):
        for Series in os.listdir(Patient + '/' + Study):
            total += 1
            try:
                path = "../Anonymized_" + cwd_name + "/" + Patient + '/' +\
                       Study + '/' + Series
                os.makedirs(path)
                print("os.makedirs:", path)
            except:
                print('failed to prepare anonymized dir "../Anonymized"')
                pass

print("A total of", total, "dirs.")
n = 0

for Patient in os.listdir('.'):
    for Study in os.listdir(Patient):
        for Series in os.listdir(Patient + '/' + Study):
            n += 1
            print("Anonymizing: " +  Patient + '/' + Study + ", " + str(n) + "/" + str(total))
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
                    ds.save_as("../Anonymized_" + cwd_name + "/" + path)
                except:
                    print('failed to save dicom file')
                    pass

print('done!')
