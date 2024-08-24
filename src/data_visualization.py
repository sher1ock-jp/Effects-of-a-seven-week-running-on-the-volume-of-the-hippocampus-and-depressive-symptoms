import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import seaborn as sns
import os

def read_cesd_file(beh_data):
    demo_df = pd.DataFrame({
        'participant_id': ['sub-119BPAF161001'],
        'vo2max_UKK1': [41.45],
        'vo2max_UKK2': [47.39],
        'BMI': [23.04],
        'age': [21],
        'sex': [2]
    })

    # CES-D is "Center for Epidemiologic Studies Depression Scale"
    cesd_data = []
    
    for df in beh_data:
        cesd_columns = [col for col in df.columns if col.startswith('CESD_')]
        df['total_score'] = df[cesd_columns].sum(axis=1)
        cesd_data.append(df)
        print(df[['participant_id', 'session_id', 'total_score']])
        print(f"Full total score: {df['total_score'].values[0]}")

    # if cesd_data:
    #     cesd_df = pd.concat(cesd_data, ignore_index=True)
    # else:
    #     print("No CES-D data found in the provided list.")
    #     cesd_df = pd.DataFrame()

    # # Merge demographic and CES-D data
    # full_df = pd.merge(demo_df, cesd_df, on='participant_id')

    # plt.figure(figsize=(10, 6))
    # plt.plot(full_df['session_id'], full_df['total_score'], marker='o')
    # plt.title('CES-D Scores Across Sessions')
    # plt.xlabel('Session')
    # plt.ylabel('CES-D Total Score')
    # plt.xticks(range(1, 5))
    # plt.grid(True)
    # plt.show()

    # # Correlate VO2 max improvement with change in CES-D score
    # cesd_change = full_df.loc[full_df['session_id'] == 4, 'total_score'].values[0] - full_df.loc[full_df['session_id'] == 1, 'total_score'].values[0]
    # print(f"Change in CES-D score: {cesd_change}")
    # print(f"VO2 max improvement: {full_df['vo2max_improvement'].values[0]}")

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


