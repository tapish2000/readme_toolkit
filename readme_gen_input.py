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

# Installation
if (write_install):
  lines.append("## Installation\n")
  lines.extend(install_steps)

# Usage
lines.append("## Usage\n")

# Authors and Acknowledgment
lines.append("## Authors and Acknowledgment\n")

# Contributing
lines.append("## Contributing\n")

# Basic syntax of Markdown


readme_f.writelines(lines)
readme_f.close()