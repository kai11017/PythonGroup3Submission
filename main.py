
import zipfile

def data_loader(name_of_dataset):
    path_to_zip_file=name_of_dataset
    directory_to_extract_to=''
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)




    



print('----Welcome to Team - 3 Submission of Python Lab End Project')

choose=input('1. UCMerced_Land_Use Dataset \n 2. Medical-Waste-v4.0 \n 3. Ultrasound Fetus Dataset \nChoose from the following : (Enter choice 1 2 or 3) ')
name_of_dataset=input('Enter the name of the zipfile in which the respective dataset is stored : ')

data_loader(name_of_dataset)








