'''
This is the driver code which acts as the interactive CLI
and asks user for the various granular questions.

'''
import markdown

def integrate(details, install_steps, usage_steps):
    readme_text = []
    readme_html = ""

    repo_link = details['repo-link']
    repo_name = repo_link.split('/')[-1]

    # Repo Name
    readme_text.append(("# " + repo_name))
    readme_html += ("# " + repo_name + "\n")

    maj_lang = details['meta-data']['language']
    purpose = details['purpose']

    # One-liner
    readme_text.append(("The " + repo_name + " is a " + maj_lang[0] + " repository."))
    readme_html += ("The " + repo_name + " is a " + maj_lang[0] + " repository.\n\n")
    readme_text.append(None)

    # Descriptiom
    readme_text.append("## Description")
    readme_html += ("## Description\n")
    ### Purpose
    if purpose.split()[0].lower() in ['for', 'in', 'to'] or purpose.split()[0][-3:].lower() == 'ing':
        readme_text.append("The major purpose of this project is " + purpose[0].lower() + purpose[1:])
        readme_html += ("The major purpose of this project is " + purpose[0].lower() + purpose[1:] + "  \n")
    else:
        readme_text.append(purpose)
        readme_html += (purpose + "  \n")
    if details['genre']:
        ### Genres
        readme_html += ("\n")
        if details['genre'] != ["Other"] and len(details['genre']) > 0:
            if len(details['genre']) == 1:
                readme_text.append("This is a " + details['genre'][0] + " project.")
                readme_html += ("This is a " + details['genre'][0] + " project.\n")
            else:
                readme_text.append("The project is based on the following genres: ")
                readme_html += ("The project is based on the following genres: \n")
                for genre in details['genre']:
                    if genre != "Other":
                        readme_text.append("* " + genre)
                        readme_html += ("* " + genre + "\n")
                    else:
                        readme_text.append("* And some other genres as well...")
                        readme_html += ("* And some other genres as well...\n")
    if details['usecase']:
        ### Usecases
        readme_html += ("\n")
        if details['usecase'] != ["Other"] and len(details['usecase']) > 0:
            if len(details['usecase']) == 1:
                readme_text.append("This project is useful in the " + details['usecase'][0] + " domain.")
                readme_html += ("This project is useful in the " + details['usecase'][0] + " domain.\n")
            else:
                readme_text.append("This project is useful in the following domains: ")
                readme_html += ("This project is useful in the following domains: \n")
                for usecase in details['usecase']:
                    if usecase != "Other":
                        readme_text.append("* " + usecase + " Domain")
                        readme_html += ("* " + usecase + " Domain\n")
                    else:
                        readme_text.append("* And some other domains as well...")
                        readme_html += ("* And some other domains as well...\n")
    if details['images']:
        ### Images
        readme_html += ("\n")
        for image_url in details['images']:
            readme_text.append("![Image](" + image_url + ")")
            readme_html += ("![Image](" + image_url + ")\n")
    readme_text.append(None)
    readme_html += ("\n")

    if install_steps:
        # Installation Steps
        if len(install_steps) != 0:
            readme_text.append(("## Installation Steps"))
            readme_html += ("## Installation Steps\n")
            step_no = 1
        
            for step in install_steps:
                desc = step['description']
                code = step['code']
                if desc and code:
                    readme_text.append(str(step_no) + '. ' + desc)
                    readme_html += (str(step_no) + '. ' + desc + "\n")
                    readme_text.append("    ```")
                    readme_html += ("\t```\n")
                    readme_text.append("    " + code)
                    readme_html += ("\t" + code + "\n")
                    readme_text.append("    ```")
                    readme_html += ("\t```\n")
                else:
                    if desc:
                        readme_text.append(str(step_no) + '. ' + desc)
                        readme_html += (str(step_no) + '. ' + desc + "\n")
                    elif code:
                        readme_text.append(str(step_no) + ".    ```")
                        readme_html += (str(step_no) + ".\t```\n")
                        readme_text.append("    " + code)
                        readme_html += ("\t" + code + "\n")
                        readme_text.append("    ```")
                        readme_html += ("\t```\n")
                step_no += 1
            readme_text.append(None)
            readme_html += ("\n")

    if usage_steps:
        # Usage Steps
        if len(usage_steps) != 0:
            readme_text.append("## Usage Steps")
            readme_html += ("## Usage Steps\n")
            step_no = 1

            for step in usage_steps:
                desc = step['description']
                code = step['code']
                if desc and code:
                    readme_text.append(str(step_no) + '. ' + desc)
                    readme_html += (str(step_no) + '. ' + desc + "\n")
                    readme_text.append("    ```")
                    readme_html += ("\t```\n")
                    readme_text.append("    " + code)
                    readme_html += ("\t" + code + "\n")
                    readme_text.append("    ```")
                    readme_html += ("\t```\n")
                else:
                    if desc:
                        readme_text.append(str(step_no) + '. ' + desc)
                        readme_html += (str(step_no) + '. ' + desc + "\n")
                    elif code:
                        readme_text.append(str(step_no) + ".    ```")
                        readme_html += (str(step_no) + ".\t```\n")
                        readme_text.append("    " + code)
                        readme_html += ("\t" + code + "\n")
                        readme_text.append("    ```")
                        readme_html += ("\t```\n")
                step_no += 1
            readme_text.append(None)
            readme_html += ("\n")

    # Authors and Acknowledgement
    readme_text.append("## Authors and Acknowledgement")
    readme_html += ("## Authors and Acknowledgement\n")
    readme_text.append("The following are the collaborators of the project:  ")
    readme_html += ("The following are the collaborators of the project:  \n")
    for collaborator in details['meta-data']['collaborators']:
        if not collaborator['name']:
            collaborator['name'] = collaborator['username']
        readme_text.append("- [" + collaborator['name'] + "](https://github.com/" + collaborator['username'] + ")  ")
        readme_html += ("- [" + collaborator['name'] + "](https://github.com/" + collaborator['username'] + ")  \n")
    readme_text.append(None)
    readme_html += "\n"

    # Contributing
    readme_text.append("## Contributing")
    readme_html += ("## Contributing\n")
    readme_text.append("First fork this repo then clone it into your system. Pull requests are welcome. For major changes, please open an \
    # issue first to discuss what you would like to change.")
    readme_html += ("First fork this repo then clone it into your system. Pull requests are welcome. For major changes, please open an \
    # issue first to discuss what you would like to change.\n\n")
    readme_text.append(None)

    if details['license-name'] and details['license-url']:
        # License
        if not details['license-name']:
            details['license-name'] = details['license-url']
        readme_text.append("## License")
        readme_html += ("## License\n")
        readme_text.append("Licensing under [" + details['license-name'] + "](" + details['license-url'] + ")")
        readme_html += ("Licensing under [" + details['license-name'] + "](" + details['license-url'] + ")\n\n")
        readme_text.append(None)

    # Basic markdown syntax to use
    readme_text.append("<!-- BASIC SYNTAX OF MARKDOWN FOR YOU TO USE -->")
    readme_text.append("<!-- # : For Title or h1 heading -->")
    readme_text.append("<!-- ## : For h2 heading and so on... -->")
    readme_text.append("<!-- 1. : For ordered list -->")
    readme_text.append("<!-- *  or -  : For unordered list -->")
    readme_text.append("<!-- [name][link]: For hyperlinks -->")
    readme_text.append("<!-- ![alt_name](link/source of image): For displaying image -->")
    readme_text.append(None)

    output_file = open("readme_toolkit/readme_form/templates/readme_form/output_README.md", "w")
    output_file.write(readme_html)
    output_file.close()

    return readme_text, markdown.markdown(readme_html).splitlines()

def customize_profile(profile):
    new_profile = []
    
    # Health Percentage
    new_profile.append("Health Percentage: " + str(profile['health_percentage']))
    # print(profile['files'])
    for key, value in profile['files'].items():
        if value:
            new_profile.append(key.replace('_', ' ') + ' : Present')
        else:
            new_profile.append(key.replace('_', ' ') + ' : Not Present')
    
    return new_profile
