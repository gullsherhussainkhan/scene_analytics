from scene_analytics.corelib.scene_anonymization.blur_regions import BlurRegion
from cv2 import imread as cv2_imread


class Anonymizer:
    
    def __init__(self,):
        
        self.blur_algo = BlurRegion()
    
    def anonymize_image(self,input_image_path,dimensions_list,algorithm,blocks):
        input_image = cv2_imread(input_image_path)

        (h, w) = input_image.shape[:2]

        original_image = input_image.copy()

        for dim in dimensions_list:        
            input_region = self.blur_algo.extract_region(input_image,dim[0],dim[1],dim[2],dim[3])
            
            if (algorithm=='gaussian'):
                processed_region = self.blur_algo.gaussian_blur(input_region,blocks)

            original_image[dim[0]:dim[1], dim[2]:dim[3]] = processed_region

        return original_image
        