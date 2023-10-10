from pathlib import Path
from PIL import Image
from mmocr.apis import MMOCRInferencer
path_img = input("Enter path for images: ")
path_model = input("Enter the path for model weights: ")
path_config = input("Enter the path for model config file: ")
output_path = input("Enter path for output directory: ")
# ocr = MMOCRInferencer(rec='demo/mmocr/configs/textrecog/svtr/svtr-small_20e_st_mj.py', rec_weights='svtr-small_20e_st_mj-35d800d6.pth')
ocr = MMOCRInferencer(rec=path_config, rec_weights=path_model)
for f in Path(path_img).glob('*.png'):
    img_path = str(f).replace("\\","/")
    ocr(img_path,out_dir=output_path,save_vis=True,save_pred=True)