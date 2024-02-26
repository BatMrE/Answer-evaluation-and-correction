import streamlit as st
import os
from src.model import *
from src.operations import *

@st.cache_resource
def get_default_answers(question):
    return {"answer": ""}

def main():
    st.title("Geography Questions")

    # Define the question
    question = "Importance of Biodiversity in ecosystem"

    # Initialize session state dictionary if not already initialized
    if 'answers' not in st.session_state:
        st.session_state.answers = get_default_answers(question)

    if 'show_improve_button' not in st.session_state:
        st.session_state.show_improve_button = False

    if 'auto_improve' not in st.session_state:
        st.session_state.auto_improve = False

    # Display the question and input field for the answer
    st.subheader(f"Question: {question}")
    # Retrieve answer from session state or default to empty string
    answer = st.text_area("Your answer", st.session_state.answers.get("answer", ""))
    st.session_state.answers["answer"] = answer  # Store answer in session state

    # Add a submit button
    if st.button("Submit"):
        # Display the submitted answer
        answer = st.session_state.answers.get("answer", "")
        gram_count, lexical_diversity_score, phraseology_score, phraseology_score2, vocab_score, avg_cohesion_score, convention_score = eval_ans(answer)
        data = {
            "Gram Count": [gram_count],
            "Lexical Diversity Score": [lexical_diversity_score],
            "Phraseology Score": [phraseology_score],
            "Phraseology Score 2": [phraseology_score2],
            "Vocabulary Score": [vocab_score],
            "Average Cohesion Score": [avg_cohesion_score],
            "Convention Score": [convention_score]
        }
        st.table(data)
        st.success("Answer submitted successfully!")
        st.session_state.show_improve_button = True
        st.session_state.gram_count = gram_count
        st.session_state.lexical_diversity_score = lexical_diversity_score
        st.session_state.phraseology_score = phraseology_score
        st.session_state.phraseology_score2 = phraseology_score2
        st.session_state.vocab_score = vocab_score
        st.session_state.avg_cohesion_score = avg_cohesion_score
        st.session_state.convention_score = convention_score

        if(gram_count > 0 or lexical_diversity_score < 0.5 or phraseology_score < 0.01 or phraseology_score2 < 0.02 or vocab_score < 80 or avg_cohesion_score < 5 or convention_score < 0.02 ):
            st.session_state.auto_improve = True

    # if st.session_state.show_improve_button:
    if st.session_state.show_improve_button or st.session_state.auto_improve:
        if st.button("Improve answer") or st.session_state.auto_improve:
            gram_count = st.session_state.gram_count
            lexical_diversity_score = st.session_state.lexical_diversity_score
            phraseology_score = st.session_state.phraseology_score
            phraseology_score2 = st.session_state.phraseology_score2
            vocab_score = st.session_state.vocab_score
            avg_cohesion_score = st.session_state.avg_cohesion_score
            convention_score = st.session_state.convention_score
            gen_model(gram_count, lexical_diversity_score, phraseology_score, phraseology_score2, vocab_score, avg_cohesion_score, convention_score, question, answer)
            st.session_state.show_improve_button = False

def eval_ans(essay_text):
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
    print("phraseology score matrix:", phraseology)

    phraseology_scores2 = [calculate_phraseology_score(sections[i], sections[i+1]) for i in range(len(sections)-1)]
    phraseology2 = sum(phraseology_scores2) / len(phraseology_scores2) if phraseology_scores2 else 0
    print("phraseology score:", phraseology2)

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

    return gram_count, lexical_diversity_score, phraseology, phraseology2, \
        vocab_score, avg_cohesion_score, convention_score


def gen_model(gram_count, lexical_diversity_score, phraseology, phraseology2, vocab_score, avg_cohesion_score, convention_score, question, answer):

    pdf_file_path = os.path.join(os.getcwd(), "data", "human-geography.pdf")
    docs = load_and_split_pdf(pdf_file_path)

    # Initialize Chroma vectorstore
    vectorstore = initialize_chroma_vectorstore(docs)

    # Initialize RAG chain
    rag_chain = initialize_rag_chain(vectorstore)
    # Example usage of the RAG chain
    output = rag_chain.invoke(f"Enhance the answer and refine its grammar for the question: '{question}' with the provided answer: '{answer}'")
    st.info(output)

    gram_count, lexical_diversity_score, phraseology_score, phraseology_score2, vocab_score, avg_cohesion_score, convention_score = eval_ans(output)
    data = {
        "Gram Count": [gram_count],
        "Lexical Diversity Score": [lexical_diversity_score],
        "Phraseology Score": [phraseology_score],
        "Phraseology Score 2": [phraseology_score2],
        "Vocabulary Score": [vocab_score],
        "Average Cohesion Score": [avg_cohesion_score],
        "Convention Score": [convention_score]
    }
    st.table(data)

if __name__ == "__main__":
    main()
