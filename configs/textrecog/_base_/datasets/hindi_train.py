#config file for hindi dataset
hindi_textrecog_data_root = 'C:/Users/vanga/OneDrive/Desktop/temp/hindi/hindi/'

hindi_textrecog_train = dict(
    type='OCRDataset',
    data_root=hindi_textrecog_data_root,
    ann_file="C:/Users/vanga/OneDrive/Desktop/temp/hindi/hindi/new_train.json",
    test_mode=False,
    pipeline=None)

hindi_textrecog_test = dict(
    type='OCRDataset',
    data_root=hindi_textrecog_data_root,
    ann_file="C:/Users/vanga/OneDrive/Desktop/temp/hindi/hindi/new_test.json",
    test_mode=True,
    pipeline=None)