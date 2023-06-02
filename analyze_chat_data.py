import matplotlib.pyplot as plt

def analyze_chat_data(file_path):
    participants = {}
    total_messages = 0

    with open('give your path here', 'r', encoding='utf-8') as file:
        for line in file:
            # Example line format: [timestamp] Sender Name: Message
            if ']' in line and ':' in line:
                timestamp, rest = line.split(']', 1)
                sender = rest.split(':', 1)[0].strip()
                
                if sender not in participants:
                    participants[sender] = 1
                else:
                    participants[sender] += 1
                
                total_messages += 1

    activity_levels = {participant: count/total_messages for participant, count in participants.items()}
    
    return activity_levels

def visualize_results(activity_levels):
    participants = activity_levels.keys()
    levels = activity_levels.values()

    plt.bar(participants, levels)
    plt.xlabel('Participants')
    plt.ylabel('Activity Level')
    plt.title('WhatsApp Group Activity Levels')
    plt.xticks(rotation=45)
    plt.show()

# Provide the path to your exported WhatsApp chat file
chat_file_path = 'path/to/your/exported/file.txt'

activity_levels = analyze_chat_data(chat_file_path)
visualize_results(activity_levels)
