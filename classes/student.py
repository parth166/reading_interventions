class Student:
    def __init__(self, name, age, grade, school, country, prefers="anything"):
        """
            A student class that tracks reading habits and quirks of a student.
            This is useful for future analytics and expert diagnosis/intervention when needed.
        """
        self.name = name
        self.age = age
        self.grade = grade
        self.school = school
        self.country = country # country of the school
        self.prefers = prefers
        self.covered_vocab = {}
        self.difficult_to_speak = set()
        self.difficult_to_understand = set()
        self.easy_word_set = set()
        self.instructor_comments = []

        self.unique_identifier = name # simple hash for POC |||| can be replaced with better hash functions

    def get_hash_id(self):
        return self.unique_identifier
    