import json

class Intervention:
    def __init__(self, word, student):
        self.word = word
        self.meaning = word.meaning
        self.type = student.prefers if student else "generic" # (rhyming, story)
        self.pronunciation = word.pronunciation_american if student and student.country == "USA" else word.pronunciation_american
        self.synonyms=word.synonyms
        self.antonyms=word.antonyms
        self.story = word.story
        self.rhyming_words = word.rhyming_words
        self.unique_id = word.get_word_hash() + (str(student.get_hash_id()) if student else "")

        self.reference_image = None
        self.audio_file = None
        self.video_file = None

    def set_images(self, object_images, subword_images, video=None):
        self.images = {
            "object": object_images,
            "subword_images": subword_images # images for objects when we break the word down into objects (Snowflake) ~ [Image of an snow + Image of a flake] 
        }

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

