import requests
from celery import shared_task
from django.conf import settings
from .models import GeneratedImage

@shared_task
def generate_image(prompt):
    api_key = settings.STABILITY_API_KEY
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7.0,  
        "width": 1024,    
        "height": 1024     
    }

    try:
        response = requests.post(
            'https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image',
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            response_data = response.json()
            image_url = response_data.get('image_url')  
            if image_url:
                GeneratedImage.objects.create(prompt=prompt, image_url=image_url)
                return image_url
            else:
                print("Image URL not found in response.")
                return None
        else:
            print(f"Failed to generate image: {response.status_code} {response.text}")
            return None

    except Exception as e:
        print(f"Error generating image for prompt '{prompt}': {e}")
        return None
