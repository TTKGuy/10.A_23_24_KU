import random

descriptionss = ["In the next decade", "Astrologers predict that", "Scientists believe that by", "Futurists are certain that", "Economists forecast a time", "Technologists envision a world", "Climatologists warn of", "Historians predict a resurgence", "Space experts anticipate significant", "Biologists foresee a breakthrough", "Artificial intelligence experts say", "Medical researchers predict a cure", "Environmentalists warn of an", "Cultural analysts anticipate a shift", "Epidemiologists project a decline", "Robotics specialists envision robots", "Energy experts forecast a revolution", "Psychologists predict a change", "Sociologists anticipate societal shifts", "Ethicists warn of potential", "Astronomers forecast a cosmic", "Cybersecurity experts predict increased", "Educators foresee a new era", "Geneticists predict a genetic", "Urban planners anticipate city", "Neuroscientists predict advancements in", "Quantum physicists anticipate groundbreaking", "Digital nomads foresee a shift", "Cryptocurrency experts predict a boom", "Agricultural experts forecast innovative"] #divdabja teiciens
descriptionsm = ["In the future, things will change", "Life will present challenges ahead", "People will seek new opportunities", "The world will continue evolving", "Technology will play a role", "Nature will always surprise us", "Societies will face transformations", "Knowledge will expand continuously", "Dreams will shape reality", "Love will remain a constant", "Challenges will test resilience", "Hope will guide many", "Changes will bring both joy and sorrow", "Stories will connect generations", "Wisdom will come from experiences", "Passion will fuel innovations", "Questions will lead to answers", "Moments will define us", "Choices will shape destinies", "Curiosity will drive exploration", "Time will heal wounds", "Adventures will await many", "Growth will be a journey", "Diversity will enrich lives", "Silence will speak volumes", "History will teach lessons", "Destinies will intertwine", "Nature will always find balance", "Journeys will reveal truths", "Mysteries will continue to intrigue", "Memories will linger", "Hopes will be realized", "Fears will be faced", "Strength will be found within", "Bonds will form connections", "Discoveries will inspire awe", "Dreams will inspire action", "Endings will lead to new beginnings", "Every challenge will have a lesson", "Moments of reflection will bring clarity", "Paths will cross", "Every end will have a new chapter", "Echoes will remind us", "New horizons will beckon", "Sunsets will promise a new day", "Every setback will be a setup", "Tales will inspire generations", "Tomorrow will always hold promise", "The journey will be as important as the destination", "Destinies will be shaped by choices", "Nature will continue its dance", "Every voice will have a story", "Time will be a healer and a revealer", "The unknown will beckon explorers", "Innovations will reshape landscapes", "Minds will continue to dream", "Heartbeats will tell tales", "Passages of time will be marked by memories", "Moments of silence will be profound", "Destinations will be the culmination of journeys", "Stars will guide some paths", "The past will inform the future", "Nature's wonders will inspire awe", "Echoes of the past will resonate", "Dreams will light up the night", "Ripples will spread from every action", "Stories will bridge generations", "The universe will hold infinite mysteries", "Time's passage will be marked by tales", "Horizons will expand with every step", "Nature's cycles will continue", "Voices of the past will echo in the present", "The tapestry of life will be intricate", "Journeys will forge bonds", "Memories will be cherished treasures", "Moments will be fleeting yet memorable", "Challenges will be stepping stones", "The symphony of life will play on", "Paths will wind and intertwine", "Nature will always be a muse", "Every dawn will promise possibilities", "The canvas of life will be vast", "Nature's rhythms will be constant", "Voices will echo across time", "Moments of stillness will hold power", "The essence of life will be in moments", "The journey will be worth the destination", "Nature's beauty will be ever-present", "Echoes of laughter will linger", "Every story will have its chapter"] #apgalvojumi
actions = ["embrace the change", "seek understanding", "forge connections", "navigate challenges", "embrace possibilities", "find inner strength", "cherish memories", "cultivate resilience", "celebrate diversity", "pursue passions", "share stories", "learn from experiences", "embrace the journey", "discover new horizons", "build bridges", "foster collaboration", "celebrate achievements", "value every moment", "encourage growth", "honor traditions", "challenge assumptions", "explore new perspectives", "support each other", "create lasting memories", "engage with curiosity", "celebrate diversity", "cherish connections", "cultivate kindness", "foster innovation", "nurture relationships"] #rikojumi
horoscopes = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
full = {
    
}
def defhoroscope(horoscope):
    full[horoscope] = []
    for x in range(0, random.randint(3, 4)):
        temp = random.randint(1, 2)
        if temp == 1:
            tempp = ''
            temp1 = random.randint(0, len(descriptionss)-1)
            tempp += str(descriptionss[temp1])
            tempp += ', '
            descriptionss.pop(temp1)
            temp2 = random.randint(0, len(descriptionsm)-1)
            tempp += str(descriptionsm[temp2])
            tempp += '.'
            descriptionsm.pop(temp2)
            
            full[horoscope].append(tempp)
            
        if temp == 2:
            tempp = ''
            temp1 = random.randint(0, len(descriptionsm)-1)
            tempp += str(descriptionsm[temp1])
            descriptionsm.pop(temp1)
            tempp += ', '
            temp2 = random.randint(0, len(descriptionsm)-1)
            tempp += str(descriptionsm[temp2])
            descriptionsm.pop(temp2)
            tempp += '.'
            full[horoscope].append(tempp)

            
    if random.randint(0, 3):
        temp1 = random.randint(0, len(actions)-1)
        full[horoscope].append(actions[temp1]+'.')  
        actions.pop(temp1)
for i in horoscopes:
    defhoroscope(i)
    print(i, ': ')
    print(' '.join(full[i]))
    



input()