import streamlit as st

# Adding title
st.title('ASA CHATBOT')

st.write('Welcome to the chatbot! How can I assist you today?')

# Streamlit input and output
question = st.text_input('Ask a question:', key='unique_key')

if question:
    if question.lower() == 'hello':
        st.write('Hello! How can I help you?')
    elif question.lower() == 'what is your name?':
        st.write('I am ASA CHATBOT, your AI assistant. How can I help you today?')
    elif question.lower() == 'how are you doing today?':
        st.write("I'm doing well, thanks for asking!")
    elif question.lower() == 'how can you help me?':
        st.write("I'm an AI assistant, how can I assist you today?")
    elif question.lower() == 'what is 2 + 2?':
        st.write('2 + 2 is 4.')
    elif question.lower() == 'what color is the sky?':
        st.write('The sky is blue.')
    elif question.lower() == 'what is the capital of France?':
        st.write('The capital of France is Paris.')
    elif question.lower() == 'what is the largest mammal?':
        st.write('The largest mammal is the blue whale.')
    elif question.lower() == 'who wrote "To Kill a Mockingbird"?':
        st.write('Harper Lee wrote "To Kill a Mockingbird".')
    elif question.lower() == 'what is the boiling point of water?':
        st.write('The boiling point of water is 100°C or 212°F.')
    elif question.lower() == 'who is the president of the United States?':
        st.write('As of my knowledge cutoff date, Joe Biden is the president of the United States.')
    elif question.lower() == 'what is the speed of light?':
        st.write('The speed of light is approximately 299,792 kilometers per second.')
    elif question.lower() == 'what is the square root of 64?':
        st.write('The square root of 64 is 8.')
    elif question.lower() == 'who painted the Mona Lisa?':
        st.write('Leonardo da Vinci painted the Mona Lisa.')
    elif question.lower() == 'what is the smallest prime number?':
        st.write('The smallest prime number is 2.')
    elif question.lower() == 'what is the tallest mountain in the world?':
        st.write('The tallest mountain in the world is Mount Everest.')
    elif question.lower() == 'who discovered penicillin?':
        st.write('Alexander Fleming discovered penicillin.')
    elif question.lower() == 'what is the currency of Japan?':
        st.write('The currency of Japan is the yen.')
    elif question.lower() == 'what is the longest river in the world?':
        st.write('The longest river in the world is the Nile River.')
    elif question.lower() == 'what is the most spoken language in the world?':
        st.write('The most spoken language in the world is Mandarin Chinese.')
    elif question.lower() == 'what is the chemical symbol for water?':
        st.write('The chemical symbol for water is H2O.')
    elif question.lower() == 'who is known as the father of computers?':
        st.write('Charles Babbage is known as the father of computers.')
    elif question.lower() == 'what is the fastest land animal?':
        st.write('The fastest land animal is the cheetah.')
    elif question.lower() == 'who invented the telephone?':
        st.write('Alexander Graham Bell invented the telephone.')
    elif question.lower() == 'what is the hardest natural substance?':
        st.write('The hardest natural substance is diamond.')
    elif question.lower() == 'what is the tallest building in the world?':
        st.write('As of now, the tallest building in the world is the Burj Khalifa in Dubai.')
    elif question.lower() == 'who is the author of "Harry Potter"?':
        st.write('J.K. Rowling is the author of the "Harry Potter" series.')
    elif question.lower() == 'what is the capital of Italy?':
        st.write('The capital of Italy is Rome.')
    elif question.lower() == 'what is the main ingredient in guacamole?':
        st.write('The main ingredient in guacamole is avocado.')
    elif question.lower() == 'who was the first man to walk on the moon?':
        st.write('Neil Armstrong was the first man to walk on the moon.')
    elif question.lower() == 'what is the largest planet in our solar system?':
        st.write('The largest planet in our solar system is Jupiter.')
    elif question.lower() == 'what is the freezing point of water?':
        st.write('The freezing point of water is 0°C or 32°F.')
    elif question.lower() == 'what is the capital of Canada?':
        st.write('The capital of Canada is Ottawa.')
    elif question.lower() == 'who invented the light bulb?':
        st.write('Thomas Edison is often credited with inventing the light bulb.')
    elif question.lower() == 'what is the most popular sport in the world?':
        st.write('The most popular sport in the world is soccer (football).')
    elif question.lower() == 'what is the chemical symbol for gold?':
        st.write('The chemical symbol for gold is Au.')
    elif question.lower() == 'what is the name of the largest ocean on Earth?':
        st.write('The largest ocean on Earth is the Pacific Ocean.')
    elif question.lower() == 'who is the author of "Pride and Prejudice"?':
        st.write('Jane Austen is the author of "Pride and Prejudice".')
    elif question.lower() == 'what is the capital of Germany?':
        st.write('The capital of Germany is Berlin.')
    elif question.lower() == 'what is the main ingredient in hummus?':
        st.write('The main ingredient in hummus is chickpeas.')
    elif question.lower() == 'what is the tallest waterfall in the world?':
        st.write('The tallest waterfall in the world is Angel Falls in Venezuela.')
    elif question.lower() == 'who is the CEO of Tesla?':
        st.write('As of my knowledge cutoff date, Elon Musk is the CEO of Tesla.')
    elif question.lower() == 'what is the chemical symbol for oxygen?':
        st.write('The chemical symbol for oxygen is O.')
    elif question.lower() == 'what is the capital of Russia?':
        st.write('The capital of Russia is Moscow.')
    elif question.lower() == 'who wrote "Romeo and Juliet"?':
        st.write('William Shakespeare wrote "Romeo and Juliet".')
    elif question.lower() == 'what is the largest desert in the world?':
        st.write('The largest desert in the world is the Sahara Desert.')
    elif question.lower() == 'what is the capital of Australia?':
        st.write('The capital of Australia is Canberra.')
    elif question.lower() == 'who is known as the father of physics?':
        st.write('Albert Einstein is often referred to as the father of modern physics.')
    elif question.lower() == 'what is the chemical symbol for iron?':
        st.write('The chemical symbol for iron is Fe.')
    elif question.lower() == 'what is the capital of China?':
        st.write('The capital of China is Beijing.')
    elif question.lower() == 'who discovered gravity?':
        st.write('Sir Isaac Newton is credited with discovering gravity.')
    elif question.lower() == 'what is the largest island in the world?':
        st.write('The largest island in the world is Greenland.')
    elif question.lower() == 'what is the capital of Brazil?':
        st.write('The capital of Brazil is Brasília.')
    elif question.lower() == 'who is known as the king of pop?':
        st.write('Michael Jackson is known as the king of pop.')
    elif question.lower() == 'what is the chemical symbol for carbon?':
        st.write('The chemical symbol for carbon is C.')
    elif question.lower() == 'what is the capital of India?':
        st.write('The capital of India is New Delhi.')
    elif question.lower() == 'who wrote "The Great Gatsby"?':
        st.write('F. Scott Fitzgerald wrote "The Great Gatsby".')
    elif question.lower() == 'what is the capital of Egypt?':
        st.write('The capital of Egypt is Cairo.')
    elif question.lower() == 'what is the largest lake in the world?':
        st.write('The largest lake in the world by surface area is the Caspian Sea.')
    elif question.lower() == 'what is the chemical symbol for silver?':
        st.write('The chemical symbol for silver is Ag.')
    elif question.lower() == 'who wrote "Moby Dick"?':
        st.write('Herman Melville wrote "Moby Dick".')
    elif question.lower() == 'what is the capital of Spain?':
        st.write('The capital of Spain is Madrid.')
    elif question.lower() == 'what is the largest continent?':
        st.write('The largest continent is Asia.')
    elif question.lower() == 'who invented the airplane?':
        st.write('The Wright brothers, Orville and Wilbur Wright, are credited with inventing the airplane.')
    elif question.lower() == 'what is the chemical symbol for sodium?':
        st.write('The chemical symbol for sodium is Na.')
    elif question.lower() == 'who wrote "1984"?':
        st.write('George Orwell wrote "1984".')
    else:
        st.write('I am sorry, I Have Limited Data.')
