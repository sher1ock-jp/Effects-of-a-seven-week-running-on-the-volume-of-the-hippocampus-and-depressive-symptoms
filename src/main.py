from data_loader import load_mri, load_behavioral_data
from data_visualization import plot_slices, read_cesd_file

def main():

    # Load MRI data
    # mri_data = load_mri("/Users/takayukiono/Desktop/MyProject/neuro/Effects-of-a-seven-week-running-intervention-with-moderate-intensity-on-the-volume-of-the-hippocampus-and-depressive-symptoms-in-young-men-from-the-general-population/data/sub-119BPAF161001/ses-1/anat/sub-119BPAF161001_ses-1_acq-mprage_T1w.nii.gz")
    beh_data = load_behavioral_data("./data")
    print(beh_data)

    # Read CESD file
    read_cesd_file(beh_data)

    # Plot slices
    # plot_slices(mri_data)

    return

if __name__ == "__main__":
    main()
