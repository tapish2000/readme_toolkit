def get_repo_name(repo_link):
  temp = repo_link.split('/')
  return temp[-1]



repo_link = input("Enter the Repository Link: ")
repo_name = get_repo_name(repo_link)
maj_lang = input("What is the major language used in the repository: ")
purp_repo = input("What is the purpose of the repository [eg: for timepass]: ")

install_steps = []
is_install_req = input("Do you want to add installation steps in the README [y/n]: ").lower()
write_install = False
if (is_install_req == 'y' or is_install_req == 'yes'):
  write_install = True
i = 1
while(is_install_req == 'y' or is_install_req == 'yes'):
  step_desc = input("Write a description for the step [Optional]: ")
  step_command = input("Write a command associated with the step [Optional]: ")

  if (step_command == ""):
    install_steps.append(str(i) + ". " + step_desc + "\n")
  elif (step_desc == ""):
    install_steps.append(str(i) + ". ```\n" + step_command + "\n```\n")
  else:
    install_steps.append(str(i) + ". " + step_desc + "\n\t```\n\t" + step_command + "\n\t```\n")
  i += 1

  is_install_req = input("Do you want to add more steps to the Installation in the README[y/n]: ").lower()


readme_f = open("output_readme.md", "w")
lines = []

# Repository name and tagline
lines.append("# " + repo_name + "\n")
lines.append("The " + repo_name + " is a " + maj_lang + " repository " + purp_repo + ".\n\n")

# Repository description
lines.append("## Description\n")
is_descr_required = input("Do you wish to describe about your repository [y/n]: ").lower()
if(is_descr_required=='y' or is_descr_required=='yes'):
  issue_solved = input("What major issue does your project solve: ")
  use_cases = input("What are the use cases of this project: ")
  unique_thing1 = input("2 unique ideas in this project which is worth mentioning: \n1. ")
  unique_thing2 = input("2. ")
  lines.append(issue_solved + "\n\n" + use_cases + "\n\n The highlights of the repositories are:\n\n1. " + unique_thing1 +"\n2. " + unique_thing2 + "\n")

# Installation
if (write_install):
  lines.append("## Installation\n")
  lines.extend(install_steps)

# Usage
lines.append("## Usage\n")

# Authors and Acknowledgment
lines.append("## Authors and Acknowledgment\n")
auth = input("Do you wish to tell more about the author of the project [y/n]: ").lower()
if(auth=='y' or auth=='yes'):
  name = input("Name of the author of this repository: ")
  website_link = input("Link to any personal dev blog/website [optional]: ")
  ack = input("Acknowledge people who helped you in your project")
  lines.append("The author of this repository is " + name + ". Explore more about the author and find related things [here](" + website_link + "). This project has also been succesful due to " + ack + "\n\n")

# Contributing
lines.append("## Contributing\n")
lines.append("First fork this repo then clone it into your system. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\n")
# Basic syntax of Markdown
lines.appned("\n\n")
lines.append("<!--- # for title--->\n")
lines.append("<!--- ## for h1--->\n")
lines.append("<!--- 1. for numberred bullet--->\n")
lines.append("<!--- - for bullet--->\n")
lines.append("<!---  [name](site link) for using as hyperlink--->\n")
lines.append("<!--- ![alt_name](link/source of image) for displaying image--->\n")

readme_f.writelines(lines)
readme_f.close()