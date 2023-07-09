import torch
from PIL import Image
from RealESRGAN import RealESRGAN


def io(path_name):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    try:
        model = RealESRGAN(device, scale=4)
        model.load_weights("weights/RealESRGAN_x4.pth", download=True)

        image = Image.open(path_name).convert("RGB")

        sr_image = model.predict(image)

        # sr_image.save(f'results/sr_image_{random.random(1:10001)}.png')
        res_name = "sr_image_" + path_name
        sr_image.save(res_name)

    except:
        return None
    return res_name
