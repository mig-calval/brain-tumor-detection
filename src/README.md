# Exploration of RMI dataset, exploratory data analysis and partition of datasets

The original dataset is composed of 3064 mat files. 

Each mat file contains the RMI image, patient ID, tumor type (1 = meningioma, 2 = glioma and 3 = pituituary), the border of the tumor and a mask that surrounds it. 

In total, we have 3064 RMI images from 233 different patients and images can be of three views: lateral, superior or frontal. The number of images per type of tumor is unbalanced: 

| Tumor      | Count |
| ----------- | ----------- |
| Meningioma | 708 |
| Glioma | 1426 |
| Pituituary | 930 |

but we consider the unbalance of our data is not important enough to affect our predictions. 

### Train, validation and test sets

Train and test sets are splitted in a 80 % to 20 % relation. Also, train test is subdivided into train and validation sets in a 80 % to 20 % relation.

This is the count of tumor types in each set: 

| Tumor      | Train Count | Validation Count | Test Count |
| ----------- | ----------- | ----------- | ----------- |
| Meningioma | 451 | 113 | 142 |
| Glioma | 902 | 226 | 282 |
| Pituituary | 595 | 149 | 186 |
