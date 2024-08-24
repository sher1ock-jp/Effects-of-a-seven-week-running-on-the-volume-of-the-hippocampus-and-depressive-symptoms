import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_slices(data, num_slices=3, cmap='gray'):
    
    # why slice
        # Displaying at once: This would be like looking at the whole loaf from the outside. You can see the shape, but not the inside structure.
        # Slicing: This is like cutting a few slices from different parts of the loaf. Now you can see the internal structure clearly.
    
    fig, axes = plt.subplots(3, num_slices, figsize=(15, 15))

    # for i in range(num_slices):
    #     # Axial slices
    #     axial_slice = int(data.shape[2] * (i + 1) / (num_slices + 1))
    #     axes[0, i].imshow(np.rot90(data[:, :, axial_slice]), cmap=cmap)
    #     axes[0, i].set_title(f'Axial Slice {axial_slice}')
        
    #     # Sagittal slices
    #     sagittal_slice = int(data.shape[0] * (i + 1) / (num_slices + 1))
    #     axes[1, i].imshow(np.rot90(data[sagittal_slice, :, :]), cmap=cmap)
    #     axes[1, i].set_title(f'Sagittal Slice {sagittal_slice}')
        
    #     # Coronal slices
    #     coronal_slice = int(data.shape[1] * (i + 1) / (num_slices + 1))
    #     axes[2, i].imshow(np.rot90(data[:, coronal_slice, :]), cmap=cmap)
    #     axes[2, i].set_title(f'Coronal Slice {coronal_slice}')
    
    # for ax in axes.ravel():
    #     ax.axis('off')
    
    # plt.tight_layout()
    # plt.show()

    # Optional: You can also plot a single slice from each orientation
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(np.rot90(data[:, :, data.shape[2]//2]), cmap='gray')
    axes[0].set_title('Axial (Middle Slice)')
    axes[1].imshow(np.rot90(data[data.shape[0]//2, :, :]), cmap='gray')
    axes[1].set_title('Sagittal (Middle Slice)')
    axes[2].imshow(np.rot90(data[:, data.shape[1]//2, :]), cmap='gray')
    axes[2].set_title('Coronal (Middle Slice)')
    for ax in axes:
        ax.axis('off')
    plt.tight_layout()
    plt.show()


