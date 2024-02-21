from operations import *
from data import essay_text_list

for essay_text in essay_text_list:

    gram_count = 0
    errors = find_grammar_errors(essay_text)
    print("Grammar errors found:")
    for error in errors:
        gram_count+=1
        # print("-", error)
    print("gram_count ", gram_count)


    lexical_diversity_score = calculate_lexical_diversity(essay_text)
    print("Lexical Diversity Score:", lexical_diversity_score)


    sections = get_sentences(essay_text)
    phraseology_scores2 = []
    for i in range(len(sections)-1):
        score2 = calculate_phraseology_score(sections[i], sections[i+1])
        phraseology_scores2.append(score2)

    # print("Phraseology Scores for Sections:")
    # for i, score in enumerate(phraseology_scores2, 1):
    #     print(f"Section {i}: {score2}")
    phraseology2 = 0
    if(len(phraseology_scores2)>0):
        phraseology2 = sum(phraseology_scores2)/len(phraseology_scores2)
    
    # print("Average : ", sum(phraseology_scores2)/len(phraseology_scores2))



    phraseology_scores = []
    for i in range(len(sections)-1):
        score = calculate_phrase_relation_score(sections[i], sections[i+1])
        phraseology_scores.append(score)
    phraseology = 0
    if(len(phraseology_scores2)>0):
        phraseology = sum(phraseology_scores)/len(phraseology_scores)
    # print("Phraseology Scores for Sections:")
    # for i, score in enumerate(phraseology_scores, 1):
    #     print(f"Section {i}: {score}")
    # print("Average Phraseology : ", sum(phraseology_scores)/len(phraseology_scores))



    print("Vocabulary Score:" , calculate_vocabulary_score2(essay_text))


    score = calculate_vocabulary_score(essay_text)
    print("Vocabulary score:", score)


    list_cohesion_score = []
    sentences = sent_tokenize(essay_text)
    for sentence in sentences:
        cohesion_score = calculate_cohesion_score(sentence)
        list_cohesion_score.append(cohesion_score)
        # print("Cohesion score for senten ce '{}': {}".format(sentence, cohesion_score))

    print("Average cohesion_score : ", sum(list_cohesion_score)/len(list_cohesion_score))


    score = conventions_score(essay_text)
    print("Conventions Score:", score)

    print("______________________________________________________________ ")