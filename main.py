from operations import *
from data import essay_text_list

def analyze_essay(essay_text):
    # Find grammar errors
    errors = find_grammar_errors(essay_text)
    gram_count = len(errors)
    print("Grammar errors found:", gram_count)

    # Calculate lexical diversity score
    lexical_diversity_score = calculate_lexical_diversity(essay_text)
    print("Lexical Diversity Score:", lexical_diversity_score)

    # Calculate phraseology scores
    sections = get_sentences(essay_text)
    phraseology_scores = [calculate_phrase_relation_score(sections[i], sections[i+1]) for i in range(len(sections)-1)]
    phraseology = sum(phraseology_scores) / len(phraseology_scores) if phraseology_scores else 0
    print("phraseology Score matrix:", phraseology)

    phraseology_scores2 = [calculate_phraseology_score(sections[i], sections[i+1]) for i in range(len(sections)-1)]
    phraseology2 = sum(phraseology_scores2) / len(phraseology_scores2) if phraseology_scores2 else 0
    print("phraseology Score:", phraseology2)

    # Calculate vocabulary score
    vocab_score = calculate_vocabulary_score2(essay_text)
    print("Vocabulary Score:", vocab_score)

    # Calculate cohesion score
    list_cohesion_score = [calculate_cohesion_score(sentence) for sentence in sent_tokenize(essay_text)]
    avg_cohesion_score = sum(list_cohesion_score) / len(list_cohesion_score)
    print("Average cohesion_score:", avg_cohesion_score)

    # Calculate conventions score
    convention_score = conventions_score(essay_text)
    print("Conventions Score:", convention_score)

    print("______________________________________________________________ ")

# Analyze each essay text
for essay_text in essay_text_list:
    analyze_essay(essay_text)
