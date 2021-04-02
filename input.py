repo_link = input("Enter the Repository Link: ")
repo_name = repo_link.split('/')[-1]
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
is_descr_required = input("Do you wish to describe about your repository [y/n]: ").lower()
if(is_descr_required=='y' or is_descr_required=='yes'):
  lines.append("## Description\n")
  issue_solved = input("What major issue does your project solve: ")
  use_cases = ["\n\n The project has been prepared keeping in mind these use cases:\n"]
  use_case = input("What are the use cases of this project [type \"quit\" to stop entering or keep writing ]: \n1. ")
  i = 1
  while(use_case != "quit"):
    use_cases.append("\n"+str(i)+". "+use_case)
    i = i+1
    use_case = input(str(i) + ". ")
  unique_things =["\n\n The highlights of the repositories are:\n"]
  unique_thing = input("Unique ideas in this project which is worth mentioning [type \"quit\" to stop entering or keep writing ]: \n1.  ")
  i = 1
  while(unique_thing != "quit"):
    unique_things.append("\n"+str(i)+". "+unique_thing)
    i = i+1
    unique_thing = input(str(i) + ". ")
  lines.append(issue_solved) 
  lines.extend(use_cases)
  lines.extend(unique_things)
  lines.append("\n")

# Installation
if (write_install):
  lines.append("## Installation\n")
  lines.extend(install_steps)

# Usage
lines.append("## Usage\n")
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
name = repo_link.split('/')[-2]
website_link = input("Link to any personal dev blog/website [optional]: ")
acks = ["This project has also been possible due to contribution of these people: "]
ack = input("Acknowledge people who helped you in your project [type \"quit\" to stop entering or keep writing ]: \n1. [Name, Blog page/site link]: ")
i = 1
while(ack != "quit"):
  temp = ack.split(',')
  if(len(temp)==1):
    acks.append("\n"+str(i)+". "+ack)
  else:
    acks.append("\n"+str(i)+". ["+temp[0]+"]("+temp[-1].strip()+")")
  i = i+1
  ack = input(str(i) + ". [Name, Blog page/site link]: ")
lines.append("The author of this repository is " + name + ". Explore more about the author and find related things [here](" + website_link + "). ")
lines.extend(acks)
lines.append("\n")

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
