from pathlib import Path
from PIL import Image
from mmocr.apis import MMOCRInferencer
path_img = input("Enter path for images: ")
rec_path_model = input("Enter the path for recognition model weights: ")
rec_path_config = input("Enter the path for recognition model config file: ")
det_path_model = input("Enter the path for detection model weights: ")
det_path_config = input("Enter the path for detection model config file: ")
output_path = input("Enter path for output directory: ")
ocr = MMOCRInferencer(rec=rec_path_config, rec_weights=rec_path_model,
    det=det_path_config, det_weights=det_path_model)
for f in Path(path_img).glob('*.png'):
    img_path = str(f).replace("\\","/")
    ocr(img_path,out_dir=output_path,save_vis=True,save_pred=True)