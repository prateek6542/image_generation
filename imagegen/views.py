from django.shortcuts import render
from .tasks import generate_image

def generate_images_view(request):
    image_urls = []

    if request.method == "POST":
        prompt = request.POST.get('prompt', '')
        number_of_images = int(request.POST.get('number', 3))

        results = [generate_image.delay(prompt) for _ in range(number_of_images)]

        for result in results:
            try:
                image_url = result.get(timeout=60)
                if image_url:
                    image_urls.append(image_url)
                else:
                    image_urls.append("Error: Image generation failed")
            except Exception as e:
                print(f"Error: {e}")
                image_urls.append("Error occurred")

    return render(request, 'imagegen/generate_images.html', {'image_urls': image_urls})
