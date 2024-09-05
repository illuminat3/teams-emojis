import os

def generate_markdown(directory, filetype):
    files = os.listdir(directory)
    markdown = f"## {filetype.capitalize()}\n\n"
    for file in files:
        if file.endswith(('.png', '.gif')):
            name = os.path.splitext(file)[0]
            filepath = os.path.join(directory, file)
            # Assuming the files are stored in the root of the repo
            markdown += f"![{name}]({filepath})  \n"
    return markdown

def main():
    # Define directories
    gifs_dir = './gifs'
    images_dir = './images'

    # Generate markdown sections
    gifs_markdown = generate_markdown(gifs_dir, 'gifs')
    images_markdown = generate_markdown(images_dir, 'images')

    # Create full markdown content
    readme_content = '''# teams-emojis

With the new teams update allowing for custom emojis here are some of my favourites.

'''

    readme_content += gifs_markdown + '\n' + images_markdown

    # Write to README.md
    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

if __name__ == '__main__':
    main()