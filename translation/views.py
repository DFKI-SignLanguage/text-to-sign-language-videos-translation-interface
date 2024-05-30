from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Translation
from .translation_mapping import translation_mapping  # Import the translation_mapping
from .sentence_modification import modify_sentence_structure

@csrf_exempt
def translate_text(request):
    if request.method == 'POST':
        print('Received POST request')
        text = request.POST.get('text', '')
        source_language = request.POST.get('source_language', '')
        print('Text:', text)
        print('Source Language:', source_language)


        # Manually modify sentence structure if needed
        modified_text = modify_sentence_structure(text)
        print('Modified Text:', modified_text)

        # Split the modified text into words
        words = modified_text.split()

        # Translate each word and create a dictionary of word:video_url
        # translated_words = {}
        # for word in words:
        #     video_url = translation_mapping.get(word)
        #     if video_url is not None:
        #         translated_words[word] = video_url

        # Translate each word and create a list of tuples (word, video_url)
        translated_words = []
        for word in words:
           word = word.rstrip('.,!')  # Remove dot (.) or comma (,)
           video_url = translation_mapping.get(word)
           if video_url is not None:
               translated_words.append((word, video_url))

        print('Translated Wordss:', translated_words)  # Add this line for debugging

        # Save the translations in the database (optional)

        #This is for an expert, when they click on submit eval button
        #Translation.objects.create(source_text=text, translation=mariannmt)

        #For normal users
        try:
            translation_instance = Translation.objects.filter(source_text=text)[0]
            Translation.translation = translation_instance.translation
        except IndexError:
            pass


        return JsonResponse({'translated_words': translated_words})
        #return JsonResponse({'translated_words': {'melken': "4427585_1.mp4"}})
    else:
        return JsonResponse({'error': 'Invalid request method'})

