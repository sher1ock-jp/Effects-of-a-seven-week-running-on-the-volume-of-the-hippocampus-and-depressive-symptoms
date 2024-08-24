import nibabel as nib
import os
import pandas as pd

# sub_119BPAF161001_mri_path = "/Users/takayukiono/Desktop/MyProject/neuro/Effects-of-a-seven-week-running-intervention-with-moderate-intensity-on-the-volume-of-the-hippocampus-and-depressive-symptoms-in-young-men-from-the-general-population/data/sub-119BPAF161001/ses-1/anat/sub-119BPAF161001_ses-1_acq-mprage_T1w.nii.gz"

def load_mri(path):
    img = nib.load(path)
    img_data = img.get_fdata()
    return img_data

def load_behavioral_data(base_path):
    
    beh_data = []

    for subject in os.listdir(base_path):
        if subject.startswith('sub-119BPAF161001'):
            subject_path = os.path.join(base_path, subject)
            for session in os.listdir(subject_path):
                if session.startswith('ses-'):
                    session_path = os.path.join(subject_path, session, 'beh')
                    for file in os.listdir(session_path):
                        if file.endswith('.tsv'):
                            file_path = os.path.join(session_path, file)
                            df = pd.read_csv(file_path, sep='\t')
                            beh_data.append(df)
    return beh_data

