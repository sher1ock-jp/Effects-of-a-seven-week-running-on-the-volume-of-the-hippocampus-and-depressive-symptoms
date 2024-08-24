import nibabel as nib

# sub_119BPAF161001_mri_path = "/Users/takayukiono/Desktop/MyProject/neuro/Effects-of-a-seven-week-running-intervention-with-moderate-intensity-on-the-volume-of-the-hippocampus-and-depressive-symptoms-in-young-men-from-the-general-population/data/sub-119BPAF161001/ses-1/anat/sub-119BPAF161001_ses-1_acq-mprage_T1w.nii.gz"

def load_mri(path):
    img = nib.load(path)
    img_data = img.get_fdata()
    return img_data

