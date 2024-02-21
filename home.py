import streamlit as st
from operations import *

def main():
    st.title("Questionnaire")

    # Define a list of questions
    questions = [
        "What is your name?"
        # "Where are you from?",
        # "What is your favorite color?",
        # "What is your favorite food?",
        # "What is your favorite hobby?",
    ]

    # Initialize session state dictionary if not already initialized
    if 'answers' not in st.session_state:
        st.session_state.answers = {}

    # Display each question and input field for answers
    for i, question in enumerate(questions, start=1):
        st.subheader(f"Question {i}: {question}")
        # Retrieve answer from session state or default to empty string
        answer = st.text_input(f"Your answer to question {i}", st.session_state.answers.get(f"answer_{i}", ""))
        st.session_state.answers[f"answer_{i}"] = answer  # Store answer in session state
        st.write("")  # Add a blank line for spacing

    # Add a submit button
    if st.button("Submit"):
        # Display submitted answers
        for i, question in enumerate(questions, start=1):
            answer = st.session_state.answers.get(f"answer_{i}", "")
            a, b, c, d, e, f, g = eval_ans(answer)
            st.write(f"Answer to question {i}: {a, b, c, d, e, f, g}")
        st.success("Answers submitted successfully!")

def eval_ans(answer):
    essay_text = answer
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
    phraseology2 = 0
    if(len(phraseology_scores2)>0):
        phraseology2 = sum(phraseology_scores2)/len(phraseology_scores2)
    # print("Phraseology Scores for Sections:")
    # for i, score in enumerate(phraseology_scores2, 1):
    #     print(f"Section {i}: {score2}")

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


    vocabulary_score = calculate_vocabulary_score(essay_text)
    print("Vocabulary score:", vocabulary_score)


    list_cohesion_score = []
    sentences = sent_tokenize(essay_text)
    for sentence in sentences:
        cohesion_score = calculate_cohesion_score(sentence)
        list_cohesion_score.append(cohesion_score)
        # print("Cohesion score for senten ce '{}': {}".format(sentence, cohesion_score))

    print("Average cohesion_score : ", sum(list_cohesion_score)/len(list_cohesion_score))


    score = conventions_score(essay_text)
    print("Conventions Score:", score)    

    return gram_count, lexical_diversity_score, phraseology2, phraseology, \
        calculate_vocabulary_score2(essay_text), vocabulary_score, cohesion_score

if __name__ == "__main__":
    main()
