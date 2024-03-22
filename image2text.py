from transformers import pipeline

captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
txt = captioner("https://huggingface.co/datasets/Narsil/image_dummy/resolve/main/parrots.png")
## [{'generated_text': 'two birds are standing next to each other '}]

print(txt)