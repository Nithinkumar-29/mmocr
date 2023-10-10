from pathlib import Path
from PIL import Image
from mmocr.apis import MMOCRInferencer
path_img = input("Enter path for images: ")
path_model = input("Enter the path for model weights: ")
path_config = input("Enter the path for model config file: ")
ocr = MMOCRInferencer(det=path_config, det_weights=path_model)
output_path = input("Enter path for output directory: ")
for f in Path(path_img).glob('*.png'):
    img_path = str(f).replace("\\","/")
    ocr(img_path,out_dir=output_path,save_vis=True,save_pred=True)