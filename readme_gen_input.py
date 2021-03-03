def get_repo_name(repo_link):
  temp = repo_link.split('/')
  return temp[-1]



repo_link = input("Enter the Repository Link: ")
repo_name = get_repo_name(repo_link)
maj_lang = input("What is the major language used in the repository: ")
purp_repo = input("What is the purpose of the repository [eg: for timepass]: ")

write_install = False

install_steps = []
usage_steps = []

is_install_req = input("Do you want to add installation steps in the README [y/n]: ").lower()

if (is_install_req == 'y' or is_install_req == 'yes'):
  write_install = True

i = 1
if (is_install_req == 'y' or is_install_req == 'yes'):
  install_code = input("Write the installation of steps [type 'quit' to stop entering]:\n>> Code: ")
  install_desc = input(">> Description of Code: ")
  if (install_desc == ""):
    install_steps.append(str(i) + ". \t```\n\t" + install_code + "\n\t```\n")
  elif (install_code == ""):
    install_steps.append(str(i) + ". " + install_desc + "\n")
  else:
    install_steps.append(str(i) + ". " + install_desc + "\n\t```\n\t" + install_code + "\n\t```\n")
while((is_install_req == 'y' or is_install_req == 'yes') and install_code.lower() != 'quit' and install_desc.lower() != 'quit'):
  install_code = input(">> Code: ")
  if (install_code == 'quit'):
    break
  install_desc = input(">> Description of Code: ")
  if (install_desc == ""):
    install_steps.append(str(i) + ". \t```\n\t" + install_code + "\n\t```\n")
  elif (install_code == ""):
    install_steps.append(str(i) + ". " + install_desc + "\n")
  else:
    install_steps.append(str(i) + ". " + install_desc + "\n\t```\n\t" + install_code + "\n\t```\n")

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
  unique_thing1 = input("Two unique ideas in this project which is worth mentioning: \n1. ")
  unique_thing2 = input("2. ")
  lines.append(issue_solved + "\n\n The project has been prepared keeping in mind these use cases. " + use_cases + "\n\n The highlights of the repositories are:\n\n1. " + unique_thing1 +"\n2. " + unique_thing2 + "\n")

# Installation
if (write_install):
  lines.append("## Installation\n")
  lines.extend(install_steps)

# Usage
lines.append("## Usage\n")
# usage = input("Write the steps to use your project [type 'quit' to stop entering]: \n>> Description: ")
# i = 1
# while(usage.lower() != 'quit'):
#   if (usage == ""):
#     usage_steps.append(str(i) + ". ")
#   else:
#     usage_steps.append(str(i) + ". " + usage + "\n")
#   i += 1
#   usage = input(">> Code: ")
#   if (usage.lower() == 'quit'):
#     break
#   usage_steps.append("\t" + "```\n\t" + usage + "\n\t```\n")
#   usage = input(">> Description: ")
i = 1
usage_code = input("Write the steps to use your project [type 'quit' to stop entering]:\n>> Code: ")
usage_desc = input(">> Description of Code: ")
if (usage_desc == ""):
  usage_steps.append(str(i) + ". \t```\n\t" + usage_code + "\n\t```\n")
elif (usage_code == ""):
  usage_steps.append(str(i) + ". " + usage_desc + "\n")
else:
  usage_steps.append(str(i) + ". " + usage_desc + "\n\t```\n\t" + usage_code + "\n\t```\n")
while(usage_code.lower() != 'quit' and usage_desc.lower() != 'quit'):
  usage_code = input(">> Code: ")
  if (usage_code == 'quit'):
    break
  usage_desc = input(">> Description of Code: ")
  if (usage_desc == ""):
    usage_steps.append(str(i) + ". \t```\n\t" + usage_code + "\n\t```\n")
  elif (usage_code == ""):
    usage_steps.append(str(i) + ". " + usage_desc + "\n")
  else:
    usage_steps.append(str(i) + ". " + usage_desc + "\n\t```\n\t" + usage_code + "\n\t```\n")

lines.extend(usage_steps)

# Authors and Acknowledgment
lines.append("## Authors and Acknowledgment\n")
auth = input("Do you wish to tell more about the author of the project [y/n]: ").lower()
if(auth=='y' or auth=='yes'):
  name = input("Name of the author of this repository: ")
  website_link = input("Link to any personal dev blog/website [optional]: ")
  ack = input("Acknowledge people who helped you in your project: ")
  lines.append("The author of this repository is " + name + ". Explore more about the author and find related things [here](" + website_link + "). This project has also been succesful due to " + ack + "\n\n")

# Contributing
lines.append("## Contributing\n")
lines.append("First fork this repo then clone it into your system. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\n")
# Basic syntax of Markdown
lines.append("\n\n<!--- # for title--->\n")
lines.append("<!--- ## for h1--->\n")
lines.append("<!--- 1. for numberred bullet--->\n")
lines.append("<!--- - for bullet--->\n")
lines.append("<!---  [name](site link) for using as hyperlink--->\n")
lines.append("<!--- ![alt_name](link/source of image) for displaying image--->\n")


readme_f = open("output_readme.md", "w")
readme_f.writelines(lines)
readme_f.close()
