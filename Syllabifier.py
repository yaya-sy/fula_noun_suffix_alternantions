class Syllabifier :
  """This class implements a syllabifier for fula language, using two \
  theories of syllables : Moraïc theory (Breedveld) and Syllabic theory (Paradis). I also \
  implements an option "flat" syllable structure 
  
  Atributes
  ---------
  - mode : str
    "moraic" = Moraïc Theory Syllables
    "syllabic" = Syllabic Theory Syllables
    "flat" : flat representation of syllables 
  
  Methodes :
  - __call__ :
    retourne le mot syllabifié
  """
  vowels = ["a", "e", "i", "o", "u"]

  def __init__(self, mode="flat") :
    self.mode = mode

  def prenasalize(self, word: str) :
    pass
  
  def isvowel(self, phoneme: str) -> bool :
    return (phoneme in Syllabifier.vowels)
  
  def islinked(self, phoneme: str, syllabified: list) -> bool :
    return (phoneme in (p for tup in syllabified for p in tup))
  
  def __call__(self, word: str) :
    syllables = {}
    syllabified = []
    peaks = []
    for idx, phoneme in enumerate(word) :
      if self.isvowel(phoneme) :
        peaks.append((idx))
    for peak in peaks :
      if peak - 1 in range(len(word)) and not self.isvowel(word[peak - 1]) :
        syllables[peak] = [[word[peak - 1]], [word[peak]]]
        syllabified.append(peak - 1)
    for peak in peaks :
      if peak + 1 in range(len(word)) and peak + 1 not in syllabified :
        syllables[peak].append([word[peak + 1]])
        syllabified.append(peak + 1)
    for syll in peaks :
      if syll not in syllables and self.isvowel(word[syll]):
        syllables[syll - 1].insert(len(syllables[syll - 1]) - 1, [word[syll]])
    print(syllables)