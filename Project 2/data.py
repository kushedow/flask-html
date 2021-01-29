goals = {"travel": "Для путешествий", "study": "Для учебы", "work": "Для работы", "relocate": "Для переезда"}

teachers = [

    {
        "id": 0,
        "name": "Morris Simmmons",
        "about": "Репетитор американского английского языка. Структурированная система обучения. Всем привет! Я "
                 "предпочитаю называть себя «тренером» английского языка. Мои занятия похожи на тренировки",
        "rating": 4.2,
        "picture": "https://i.pravatar.cc/300?img=20",
        "price": 900,
        "goals": ["travel", "relocate", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": True, "12:00": True, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "tue": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "wed": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "thu": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "fri": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": False},
        }
    },
    {
        "id": 1,
        "name": "Lee P",
        "about": "I am a native speaker and conversation tutor, providing private English conversation lessons using "
                 "something called Life Learning.This method allows students to take complete control of how and what "
                 "they learn. It is student-led learning focusing on interests, life goals, enjoyment and effective "
                 "learning for you, as an individual.Stop wasting time with textbooks, tests and unneccesary "
                 "pressure. Find a love for learning and speaking English with creativity and freedom. The lessons "
                 "are completely chosen by you to keep you motivated and driven to achieve your goals.",
        "rating": 4.8,
        "picture": "https://i.pravatar.cc/300?img=19",
        "price": 1200,
        "goals": ["relocate", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 2,
        "name": "Felix A",
        "about": "The English language has become the language of the world, thus, it is considered a world language. "
                 "Today English seems to evolve to a future global tongue, as its spreading on the Internet in recent "
                 "years shows (almost 80% of the worldwide web's pages are now written in English). scientific "
                 "researchers have found out that in fact many small languages have already vanished.But to teach it "
                 "in a satisfactory manner a good teacher of English is required.xA good teacher of English must "
                 "possess some qualities.Business, General and conversational English",
        "picture": "https://i.pravatar.cc/300?img=27",
        "rating": 4.7,
        "price": 1300,
        "goals": ["work"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "tue": {"8:00": True, "10:00": True, "12:00": True, "14:00": True, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": True, "10:00": True, "12:00": True, "14:00": True, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": True, "10:00": True, "12:00": True, "14:00": True, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": True, "10:00": True, "12:00": True, "14:00": True, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 3,
        "name": "Milan S",
        "about": "I have a wide range of interests, believe me, you will never be bored during our lesson. I worked "
                 "with lawyers, doctors, biologists and many others to help them improve their English in their "
                 "respective fields. Since I spent my whole life satisfying my curiosity, I acquired a huge "
                 "vocabulary that I can pass on to you.",
        "picture": "https://i.pravatar.cc/300?img=28",
        "rating": 4.9,
        "price": 1300,
        "goals": ["travel", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 4,
        "name": "Gulya S",
        "about": "Hello! My name is Gulya :) I am a native speaker of the Russian language and I am fluent in "
                 "English. I have been teaching online for 3 years now. I have an individual program, having studied "
                 "your requirements, I am preparing a special program. plan, and therefore deal) Books Cambridge, "
                 "Oxford, etc. I train and develop colloquial speech. We study words, stable combinations and put "
                 "them into practice. We speak and try to speak :) on different topics. We listen to audio lessons, "
                 "watch films with subtitles. We analyze everything on the shelves :) In parallel, of course, "
                 "we study the basics of grammar and the correct delivery of sentences :) All the materials are "
                 "provided by me. I promise you that you will talk from the first first lesson :)",
        "picture": "https://i.pravatar.cc/300?img=29",
        "rating": 4.3,
        "price": 900,
        "goals": ["travel"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 5,
        "name": "Yan M",
        "about": "Hello! My name is Yang and for more than five years I have been teaching English. I spent part of "
                 "this time in China, where I worked with students from 3 to 40 years old. I deal with both adults "
                 "and children. But for all ages, I try to make my classes fun and interactive. Teaching English to "
                 "me is not just a language lesson. I always try to attract a wider cultural and historical context "
                 "that helps my students understand more about the language and its features. A degree in history "
                 "helps me a lot to create such an intellectual environment in the classroom.For each student, "
                 "I develop an individual curriculum that depends on its goals and needs.",
        "picture": "https://i.pravatar.cc/300?img=30",
        "rating": 3.9,
        "price": 800,
        "goals": ["travel", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
    {
        "id": 6,
        "name": "Eran E",
        "about": "Hello, my name is Eran & I am a friendly native English speaker. I am an experienced English "
                 "teacher with a neutral accent that is easily understood. This is because I have grown up living in "
                 "13 countries across 4 continents. They include England, America, Australia & Japan. Presently, "
                 "I live in Lisbon, Portugal. While I am primarily focused on 1 to 1 tuition, I’ve previously taught "
                 "classes with as many as 50 students at a time. My students have ranged from 12 to 70 years old. "
                 "From Israeli middle schoolers all the way through to Thai Government officials. As a result, "
                 "I’ve learned a wide variety of teaching methods. Currently, I'm taking students with English level: "
                 "B2 onwards, as well as those who are interested in long-term growth and multiple lessons.I "
                 "understand how hard it can be to learn another language. That's why my teaching style is fun, "
                 "constructive & easy-going. Lessons will be tailored to meet your needs & goals. Through my lessons, "
                 "you will gain the confidence to speak English in your daily life.",
        "picture": "https://i.pravatar.cc/300?img=32",
        "rating": 4.5,
        "price": 1200,
        "goals": ["travel", "relocate", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 7,
        "name": "Mr. Mark",
        "about": "My lessons are fun and practical, but most importantly, we are going to be extremely productive. I "
                 "believe that the best way to master English is through EXECUTION. Less theory, more practice. Lots "
                 "of practice. Our goal is to achieve maximum involvement and focus on the subject. Schools trained "
                 "us to be very passive. Sit quietly by yourself, be lectured to, just consume information. THAT is "
                 "not how we are going to learn English.",
        "picture": "https://i.pravatar.cc/300?img=33",
        "rating": 4.5,
        "price": 1100,
        "goals": ["study"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 8,
        "name": "Skye L.",
        "about": "Hello, My name is Skye. I’m from London in the United Kingdom but I am currently living in Japan. I "
                 "have a TEFL certificate which I acquired last year. Since moving to Japan I have been teaching some "
                 "of my Japanese friends English. I think learning should be fun and engaging and even though English "
                 "can be difficult to learn I aim to make it enjoyable.I enjoy watching football and travelling. I do "
                 "a lot of Yoga in my spare time and I can't wait to meet you!",
        "picture": "https://i.pravatar.cc/300?img=35",
        "rating": 5,
        "price": 1700,
        "goals": ["relocate", "work"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 9,
        "name": "Seeta Y.",
        "about": "Hello and welcome to my profile learners of the wonderful world of the English language! I am a "
                 "certified native English teacher with an A in TEFL. Learning something new should be fun and "
                 "exciting and not something you’re dragging your feet into doing which is why I believe a little fun "
                 "and humour plays a huge part in the learning process and also the development of a healthy and "
                 "enjoyable relationship between us.I am also currently trying to learn a new language and so I know "
                 "from my own experience how daunting or sometimes challenging it can be but please remember I’m here "
                 "to work with you and not against you. We can work together on pronunciation, reading, "
                 "conversational English, homework you may have from school or college, slang, in fact on any subject "
                 "area you enjoy or want to develop as when you’re enjoying the learning process you’re learning "
                 "without even realising.",
        "picture": "https://i.pravatar.cc/300?img=36",
        "rating": 4.1,
        "price": 1200,
        "goals": ["work"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 10,
        "name": "Salman S",
        "about": "I motivate and guide students to achieve their goals. It depends on what is the problem they are "
                 "facing. Sometimes they just want to practice speaking to improve their fluency. Sometimes it's more "
                 "complicated which is a language barrier and I need to boost their confidence. Some are coming with "
                 "a specific task to pass an exam like IELTS and TOEFL. Moreover some are seeking to improve their "
                 "business skills and business conversation. Sometimes they need to pass the interview in English. "
                 "According to their requirements I have materials and programs to help them to achieve their desired "
                 "goals. My vast experience of teaching plays a vital role as well.",
        "picture": "https://i.pravatar.cc/300?img=37",
        "rating": 4.7,
        "price": 1100,
        "goals": ["travel", "study", "work"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },

    {
        "id": 11,
        "name": "Andrew G",
        "about": "Hi guys, My name is Andrew and I am an English teacher from the USA currently living now in "
                 "Atlanta, Georgia.My teaching experience ranges from 1 on 1 to groups, children to adults, "
                 "in-person or online. IMPORTANT*** Although I have experience teaching Children, right now I'm only "
                 "teaching Adults through Conversational English. This is my specialty and I do this through focusing "
                 "mainly on Accent Reduction, Pronunciation, Speech Therapy, and improving one's Vocabulary.I have "
                 "been traveling and teaching since 2008 and my travels have really helped me be more culturally "
                 "aware, and relevant. I am fun and unique when it comes to teaching English, you won't that find my "
                 "classes anywhere else.",
        "picture": "https://i.pravatar.cc/300?img=38",
        "rating": 4.2,
        "price": 900,
        "goals": ["travel", "work"],
        "free": {

            "mon": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "tue": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "wed": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "thu": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": True},
            "fri": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
        }
    },
]
