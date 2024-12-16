import os

# Define the structure with topics and subtopics
structure = {
    "Server Side topics": [
        "SQL injection",
        "Authentication",
        "Path traversal",
        "Command injection",
        "Business logic vulnerabilities",
        "Information disclosure",
        "Access control",
        "File upload vulnerabilities",
        "Race conditions",
        "Server-side request forgery (SSRF)",
        "XXE injection",
        "NoSQL injection",
        "API testing",
        "Web cache deception",
    ],
    "Client Side topics": [
        "Cross-site scripting (XSS)",
        "Cross-site request forgery (CSRF)",
        "Cross-origin resource sharing (CORS)",
        "Clickjacking",
        "DOM-based vulnerabilities",
        "WebSockets",
    ],
    "Advanced topics": [
        "Insecure deserialization",
        "Web LLM attacks",
        "GraphQL API vulnerabilities",
        "Server-side template injection",
        "Web cache poisoning",
        "HTTP Host header attacks",
        "HTTP request smuggling",
        "OAuth authentication",
        "JWT attacks",
        "Prototype pollution",
        "Essential skills",
    ]
}

# Base directory to create the files and folders
base_dir = '../Vulnerabilities_Topics'

def create_folders_and_files(base_dir, structure):
    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Iterate through the structure and create folders for each topic and subtopic
    for main_topic, subtopics in structure.items():
        # Create a folder for each main topic
        topic_folder = os.path.join(base_dir, main_topic.replace(' ', '_'))
        if not os.path.exists(topic_folder):
            os.makedirs(topic_folder)

        # Create a folder for each subtopic within the topic folder
        for subtopic in subtopics:
            subtopic_folder = os.path.join(topic_folder, subtopic.replace(' ', '_').replace('(', '').replace(')', ''))
            if not os.path.exists(subtopic_folder):
                os.makedirs(subtopic_folder)

            # Create a markdown file inside the subtopic folder
            subtopic_filename = f"{subtopic.replace(' ', '_').replace('(', '').replace(')', '')}.md"
            subtopic_file = os.path.join(subtopic_folder, subtopic_filename)

            with open(subtopic_file, 'w') as f:
                f.write(f"# {subtopic}\n\n")
                f.write("## Overview\n")
                f.write(f"Details for {subtopic} will be added here.\n\n")

# Create the folders and markdown files
create_folders_and_files(base_dir, structure)

print(f"Folders and markdown files created successfully under '{base_dir}'.")
