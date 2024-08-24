from data_loader import load_mri
from plot_slices import plot_slices

def main():

    # Load MRI data
    mri_data = load_mri("/Users/takayukiono/Desktop/MyProject/neuro/Effects-of-a-seven-week-running-intervention-with-moderate-intensity-on-the-volume-of-the-hippocampus-and-depressive-symptoms-in-young-men-from-the-general-population/data/sub-119BPAF161001/ses-1/anat/sub-119BPAF161001_ses-1_acq-mprage_T1w.nii.gz")

    # Plot slices
    plot_slices(mri_data)

    return

if __name__ == "__main__":
    main()
