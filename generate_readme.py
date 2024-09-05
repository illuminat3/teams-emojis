import os

GITHUB_REPO_URL = "https://raw.githubusercontent.com/illuminat3/teams-emojis/main"

def generate_markdown(directory, filetype):
    files = os.listdir(directory)
    markdown = f"## {filetype.capitalize()}\n\n"
    for file in files:
        if file.endswith(('.png', '.gif')):
            name = os.path.splitext(file)[0]
            file_url = f"{GITHUB_REPO_URL}/{directory}/{file}"
            markdown += f"![{name}]({file_url})  \n"
    return markdown

def main():
    # Define directories
    gifs_dir = 'gifs'
    images_dir = 'images'

    # Generate markdown sections
    gifs_markdown = generate_markdown(gifs_dir, 'gifs')
    images_markdown = generate_markdown(images_dir, 'images')

    # Create full markdown content
    readme_content = '''# teams-emojis

With the new teams update allowing for custom emojis, here are some of my favorites.

'''

    readme_content += gifs_markdown + '\n' + images_markdown

    # Write to README.md
    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

if __name__ == '__main__':
    main()
