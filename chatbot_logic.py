import re
import random


class Rulebot:
    ### Potential Negative Responses 
    negative_responses = ("no", "nope", "Nah", "naw", "not a chance", "sorry")
    ### Exit conversation keywords
    exit_commands = ("Stop","stop","STOP","quit", "bye", "pause", "exit", "goodbye", "later", "stop")

    ### Random starter questions
    random_questions = (
        "What do you know about machine learning?",
        "Have you worked on any AI/ML projects before?",
        "Which programming language do you prefer for machine learning?",
        "What interests you the most about artificial intelligence?",
        "Do you have experience with neural networks?",
        "How do you think AI will impact the future?",
        "What is your favorite machine learning algorithm?",
        "Have you used any machine learning libraries like TensorFlow or Scikit-learn?",
        "What challenges have you faced when working with data?",
        "Do you know the difference between supervised and unsupervised learning?",
        "How familiar are you with deep learning?",
        "What industries do you think will benefit the most from AI?"
    )
    # Acknowledgments
    acknowledgments = ["ok","ohh okay", "aahaan", "hmm", "done", "got it", "understood", "okay", "sure", "right"]


    def __init__(self):
        self.alienbabble = {
            'career': r'.*(career|job|profession|occupation).*',
            'education': r'.*(education|qualification|school|study|certification|degree|diploma).*',
            'about_rachit': r'.*(about|who is|tell me about|info about).*rachit*',
            'project': r'.*\b(projects|project|portfolio|work)\b.*',
            'skill': r'.*\b(skills|skill|proficient|expertise|abilities)\b.*',
            'interest': r'.*\b(interests|interest|hobbies|passion|likes)\b.*',
            'goal': r'.*\b(goals|goal|aspirations|ambitions|objectives)\b.*',
            'contact': r'.*\b(contact|email|phone|social media|connect)\b.*',
            'location': r'.*\b(location|city|country|place|residence)\b.*',
            'experience': r'.*\b(experience|background|history|work history)\b.*',
            'achievement': r'.*\b(achievements|achievement|awards|recognition|accomplishments)\b.*',
            'future_plan': r'.*\b(future plans|plan|goals|aspirations|objectives|targets)\b.*',
            'wish_me': r'.*\b(hey|HEY|Hey|hi|HI|Hi|Hello|HELLO|hello|hii|Hii)\b.*',
            'exit_signs': r'.*\b(STOP|Stop|stop|quit|Quit|QUIT|PAUSE|Pause|pause|Bye|bye|BYE)\b.*',
            'negative_signs': r'.*\b(NO|NAAH|SORRY|NOT A CHANCE|no|No|Naah|naah|sorry|Sorry|not a chance)\b.*',
            'acknowledgment': r'.*\b(ok|OK|Ok|Ohh|Okay|OKAY|ohh|okay|aahaan|hmm|done|got it|understood|sure|right)\b.*',
            'haal': r'.*\b(kya haal chaal|kese ho|how are you|HOW ARE YOU|How are you|what about you)\b.*',

        }
        self.alienbabble_compiled = {key: re.compile(value, re.IGNORECASE) for key, value in self.alienbabble.items()}


    def greet(self):
        print("Hello! 👋 Welcome to our conversation!")
        print("I'm excited to chat with you!")
        self.name = input("What is your name?\n")
        print(f"Hi {self.name} 👋, Welcome to Rachit's Personal Assistant. I'm here to help you navigate through Rachit's portfolio, answer your questions, and provide insights into his projects and skills.")
        self.chat()


    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Thank you for chatting with Rachit's Personal Assistant! If you need any more assistance, feel free to come back anytime. Have a great day ahead!")
                return True
        return False


    def chat(self):
        while True:
            # Take user input and convert it to lowercase
            reply = input("How may I assist you further?\n").lower()
        
            # Check for exit commands
            if self.make_exit(reply):
                break
        
            # Check if the input matches any greeting triggers
            elif reply in self.acknowledgments:
                print("Oh, great!")
            else:
                response = self.match_reply(reply)
                print(response)



    def match_reply(self, reply):
        for key, value in self.alienbabble_compiled.items():
            if value.search(reply):
                if key == 'career':
                    return self.career()
                elif key == 'acknowledgment':
                    return self.acknowledgment()
                elif key == 'haal':
                    return self.haal()
                elif key == 'negative_signs':
                    return self.negative_signs()
                elif key == 'exit_signs':
                    return self.exit_signs()
                elif key == 'wish_me':
                    return self.wish_me()
                elif key == 'education':
                    return self.education()
                elif key == 'about_rachit':
                    return self.about_rachit()
                elif key == 'project':
                    return self.project()
                elif key == 'skill':
                    return self.skill()
                elif key == 'interest':
                    return self.interest()
                elif key == 'goal':
                    return self.goal()
                elif key == 'contact':
                    return self.contact()
                elif key == 'location':
                    return self.location()
                elif key == 'experience':
                    return self.experience()
                elif key == 'achievement':
                    return self.achievement()
                elif key == 'future_plan':
                    return self.future_plan()
                elif reply not in self.exit_commands:
                    response = self.match_reply(reply)
                    if "I dont understand" in response:  # Adjust this based on how you handle no matches
                        print(self.ask_random_question())
                    else:
                        print(response)
        return self.no_match_intent()

    def achievement(self):
        responses = (
            "I've consistently demonstrated academic excellence, securing top positions in all semesters of my BCA program at KJIT. My dedication and hard work have earned me recognition as one of the top performers in my class.",
            "I've received two certificates for outstanding academic performance and a medal for exceptional achievement. These accolades motivate me to continue striving for excellence. Additionally, I've completed certifications in programming languages, data science, and machine learning.",
            "My certifications include [list specific certifications, e.g., Python, Data Science, Machine Learning]. These certifications have enhanced my skills and knowledge, enabling me to tackle complex projects. My academic achievements and certifications have prepared me for a successful career in computer science and technology."
        )
        return random.choice(responses)
    
    def acknowledgment(self):
        responses = (
            "What do you know about machine learning?",
            "Have you worked on any AI/ML projects before?",
            "Which programming language do you prefer for machine learning?",
            "What interests you the most about artificial intelligence?",
            "Do you have experience with neural networks?",
            "How do you think AI will impact the future?",
            "What is your favorite machine learning algorithm?",
            "Have you used any machine learning libraries like TensorFlow or Scikit-learn?",
            "What challenges have you faced when working with data?",
            "Do you know the difference between supervised and unsupervised learning?",
            "How familiar are you with deep learning?",
            "What industries do you think will benefit the most from AI?"
            )
        return random.choice(responses)
    
    def haal(self):
        responses = (
            "I'm just a bot, but I'm here and ready to help you!",
            "I'm doing great, thanks for asking! How can I assist you today?",
            "I'm always ready to assist! How can I help you?",
            "I'm a bot, so no feelings, but I'm here to help you with anything!",
            "I don't have feelings, but I'm ready to make your day easier!",
            "I'm just code, but thanks for asking! How can I assist you today?",
            "I'm here to help you with whatever you need! How can I assist you?",
            "I'm just code, but let's get back to helping you!"
            )
        return random.choice(responses)

    def future_plan(self):
        responses = (
            "I envision myself as a leading AI/ML engineer, equipped with exceptional skills and expertise. My goal is to develop innovative solutions that transform industries and improve lives. I strive to master cutting-edge technologies, staying ahead of the curve. Excellence is my benchmark.",
            "In the next 5 years, I aim to become a renowned AI/ML expert, recognized for my contributions to the field. I will continuously update my skills, exploring advancements in deep learning, natural language processing, and computer vision. My objective is to create impactful projects that showcase my expertise.",
            "Ultimately, I aspire to lead AI/ML teams, driving revolutionary projects that redefine industry standards. I will foster collaboration, mentorship, and knowledge sharing. My vision is to establish myself as a thought leader, inspiring the next generation of AI/ML engineers. I am committed to lifelong learning, innovation, and excellence."
        )
        return random.choice(responses)
    
    def wish_me(self):
        responses = (
            "Hello 👋,Welcome to Rachit's Personal Assistant. I'm here to help you navigate through Rachit's portfolio, answer your questions, and provide insights into his projects and skills.",
            "Hello 👋,Welcome to Rachit's Personal Assistant. I'm here to help you navigate through Rachit's portfolio, answer your questions, and provide insights into his projects and skills."
        )
        return random.choice(responses)
    
    def negative_signs(self):
        responses = (
            "I see! Is there anything else I can help you with?",
            "No problem! Let me know if you have any other questions.",
            "That's okay! Feel free to ask if you need help with something else.",
            "Got it! Would you like to try something else?",
            "No worries! Maybe I can assist you with another topic?",
            "I understand. How about exploring something different?",
            "That's alright! If you're unsure, feel free to ask me anything!",
            "No worries! I'm here whenever you're ready."
        )
        return random.choice(responses)
    
    def exit_signs(self):
        responses = (
            "Thank you for chatting with Rachit's Personal Assistant! If you need any more assistance, feel free to come back anytime. Have a great day ahead!.",
            "Thank you for chatting with Rachit's Personal Assistant! If you need any more assistance, feel free to come back anytime. Have a great day ahead!."
        )
        return random.choice(responses)
    
    def experience(self):
        responses = (
            "As a student, I worked on various academic projects involving AI/ML, including image classification, natural language processing, and predictive modeling. These projects helped me develop a strong foundation in machine learning algorithms and deep learning techniques. I successfully implemented projects using Python, NumPy, Pandas, and Scikit-learn.",
            "I've developed personal projects leveraging AI/ML, such as chatbots, sentiment analysis tools, and recommendation systems. These projects allowed me to explore AI/ML applications in real-world scenarios, enhancing my problem-solving skills. I utilized libraries like NLTK, Matplotlib, and Seaborn to analyze and visualize data.",
            "Through internships and training programs, I gained hands-on experience with AI/ML tools and technologies. I learned to design, train, and deploy machine learning models using popular frameworks. I also explored AI/ML applications in computer vision, speech recognition, and natural language processing.",
            "I've conducted research on emerging AI/ML trends, including neural networks, transfer learning, and reinforcement learning. I've explored research papers and articles to stay updated on industry advancements. This knowledge enables me to contribute to innovative AI/ML projects and solutions."
        )
        return random.choice(responses)


    def education(self):
        responses = (
            "I'm currently pursuing Bachelor of Computer Applications (BCA) at KJIT, one of the renowned institutions in Gujarat. As a 3rd-year student, I've gained a solid foundation in computer science and programming.",
            "I completed my 12th standard from Saint Basil School, Vadodara, with a strong academic record. My schooling laid the groundwork for my interest in computer science and technology.",
            "Throughout my academic journey, I've developed proficiency in programming languages like Python, Java, and C++. I've also explored various frameworks and libraries, including NumPy, Pandas, and Scikit-learn.",
            "I've consistently achieved academic excellence, securing impressive grades in computer science and mathematics. My projects and assignments have showcased my problem-solving skills and innovative thinking."
            )
        return random.choice(responses)


    def interest(self):
        responses = (
            "I'm passionate about automation and AI's potential to simplify human life. AI can alleviate mundane tasks, freeing humans for creativity and innovation. My goal is to develop intelligent systems that enhance efficiency and quality of life. Transforming industries through automation drives me.",
            "I'm drawn to AI applications in robotic process automation, natural language processing, and computer vision. These technologies can revolutionize healthcare, finance, and education. I aim to create AI-powered tools that assist humans and make a tangible impact. Innovation through AI excites me.",
            "My focus is on designing AI systems that integrate seamlessly with human workflow, amplifying productivity and job satisfaction. Human-centered design ensures AI augments human capabilities. I explore human-computer interaction, AI ethics, and explainable AI to create harmonious human-machine collaboration. AI should empower humans."
        )
        return random.choice(responses)


    def goal(self):
        responses = (
            "My goal is to become a leading AI/ML engineer, developing innovative solutions that transform industries. I strive for excellence in deep learning, NLP, and computer vision. I aim to work with cutting-edge technologies, solving real-world problems. Impacting lives through AI drives me.",
            "In 5 years, I envision myself as a renowned AI expert, recognized for contributions to the field. I'll continuously update my skills, exploring advancements in AI and ML. My objective is to lead AI teams, driving revolutionary projects. Mentorship and knowledge sharing are key.",
            "Ultimately, I aspire to create AI systems that improve lives globally. I'll focus on healthcare, education, and sustainability. My legacy will be AI solutions that make a lasting difference. Inspiring future AI engineers to innovate and make an impact is my vision."
        )
        return random.choice(responses)

    def location(self):
        responses = (
            "I'm based in Vadodara, India.",
            "My location is Vadodara, Gujarat.",
            "I reside in the cultural city of Vadodara.",
            "You can find me in Vadodara, India.",
            "My current location is Vadodara."
        )
        return random.choice(responses)


    def contact(self):
        responses = (
            "You can reach me at rachitn46@gmail.com or +91 9586419028.",
            "Feel free to contact me through my website or social media channels.",
            "My contact information is available on my portfolio website.",
            "You can email me at rachitn46@gmail.com.",
            "Connect with me on LinkedIn for professional inquiries."
        )
        return random.choice(responses)
    def about_rachit(self):
        responses = (
            "I’m Rachit, a tech enthusiast from Vadodara, currently pursuing a career in AI/ML.",
            "Hi, I'm Rachit! I'm passionate about artificial intelligence and machine learning.",
            "I'm Rachit, a BCA student at KJIT College, with a focus on AI/ML.",
            "Hello! I'm Rachit, an aspiring AI/ML engineer with a love for coding.",
            "I'm Rachit, a curious learner exploring the world of AI/ML.",
            "Hi, I'm Rachit! I'm excited to share my knowledge and experience in AI/ML.",
            "I'm Rachit, a creative problem-solver with a passion for AI/ML innovation.",
            "Hello! I'm Rachit, a detail-oriented AI/ML enthusiast with a drive for excellence."
        )
        return random.choice(responses)


    def career(self):
        responses = (
            "I chose AI/ML because it combines my passion for problem-solving with cutting-edge technology.",
            "My career goal is to become a leading AI/ML researcher and developer.",
            "I'm pursuing a career in AI/ML to create innovative solutions for real-world problems.",
            "AI/ML fascinates me, and I want to contribute to its growth and development.",
            "I'm excited to apply my skills in AI/ML to drive positive change.",
            "My career aspiration is to work on AI/ML projects that impact people's lives.",
            "I'm drawn to AI/ML because of its potential to revolutionize industries.",
            "I want to use AI/ML to improve healthcare, education, and environmental sustainability."
        )
        return random.choice(responses)

    def skill(self):
        responses = (
            "As an AI/ML engineer, I possess a strong foundation in programming languages like Python and Java. I'm well-versed in machine learning libraries such as NumPy, Pandas, Matplotlib, Scikit-learn, and NLTK. My expertise extends to neural networks, enabling me to design and implement intelligent systems.",
            "I excel in data analysis, visualization, and modeling, leveraging tools like Seaborn and Matplotlib to uncover insights. My experience with machine learning algorithms allows me to develop predictive models that drive business value. I'm passionate about solving complex problems with data-driven solutions.",
            "As a collaborative AI/ML engineer, I thrive in team environments, communicating complex technical concepts effectively. My passion for innovation drives me to stay updated on industry trends and advancements. I'm committed to delivering scalable, efficient, and reliable AI/ML solutions that transform businesses and improve lives."
        )
        return random.choice(responses)

    def project(self):
        responses = (
                  "I'm currently working on a movie recommendation system using machine learning. This project leverages collaborative filtering and natural language processing to suggest personalized movie recommendations. Utilizing Python and Scikit-learn, I've achieved impressive accuracy.",
                  "I've designed and developed a personal website and portfolio, showcasing my skills and experiences. Built using HTML, CSS, and JavaScript, this platform highlights my projects and achievements. It serves as a comprehensive overview of my expertise.",
                  "I've created a conversational chatbot using natural language processing and machine learning. This chatbot understands user queries and responds accordingly. Integrated with my personal website, it enhances user interaction.",
                  "I'm eager to explore various projects, including image classification, sentiment analysis, and predictive modeling. I'm interested in applying machine learning to healthcare, finance, and education. Future projects will focus on solving real-world problems."
                  )
        return random.choice(responses)
    
    def ask_random_question(self):
        return random.choice(self.random_questions)

    def no_match_intent(self):
        responses = (
            "Please tell me more.",
            "Tell me more!",
            "Why do you say that?",
            "I see. Can you elaborate?",
            "Could you explain that in more detail?"
        )
        return random.choice(responses)


if __name__ == "__main__":
    Alienbot = Rulebot()
    Alienbot.greet()