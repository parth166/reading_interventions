import json

class Intervention:
    def __init__(self, word, meaning, synonyms, antonyms, intervention_type):
        self.word = word
        self.meaning = meaning
        self.type = intervention_type, # (rhyming, story)
        self.pronunciation = None
        self.accent = None
        self.reference_image = None
        self.audio_file = None
        self.video_file = None
        self.story = ""
        
    def set_pronunciation_attributes(self, pronunciation, accent):
        self.pronunciation = pronunciation
        self.accent = accent

    def set_images(self, object_images, subword_images, video=None):
        self.images = {
            "object": object_images,
            "subword_images": subword_images
        }

    def set_rhyming_words(self, rhyming_words):
        self.rhyming_words = rhyming_words
    
    def set_story(self, short_story):
        self.story = short_story

    def set_meta_data(self, obj):
        """
            The metadata has the following keys: "audio_file", "video_file", "reference_image"  
            
            (these are optional keys, without these the values of the private class variables won't change)
        """
        self.audio_file = obj["audio_file"] if "audio_file" in obj else self.audio_file
        self.video_file = obj["video_file"] if "video_file" in obj else self.video_file
        self.reference_image = obj["reference_image"] if "reference_image" in obj else self.reference_image

    def to_json(self):
        return json.dumps(self.__dict__)

