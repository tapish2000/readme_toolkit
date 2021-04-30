# readme-toolkit

There have been many situations where we needed to know what to write and put into readme just before submitting a repository. Well, this tool is just meant for that purpose. 

It is a tool created on Django framwework which is meant to help create a readme file which adheres to a template. You can also use this tool for getting health score of your readme!!

## Use Case

- Developers
- Hobbyists
- School/University submissions
- Users new to Markdown

These are some typical usecases, but overall it can be used by everyone who want the readme to be less of a headache and more of a productive snapshot of their repository.

## Dependency

We have imported various libraris and made several API calls for the purpose of our tool. The main aim was to have an easy workflow and not rebuild everything from scratch:

- APIs
    - [GitHub REST API](https://docs.github.com/en/rest)
    - [MonkeyLearn](https://app.monkeylearn.com/)
    - [Cloudinary](https://cloudinary.com/)
- Libraries
    - nltk
    - django
    - markdown
    - requests

## Features in Current Release
- A very sleek User Experience
- Proper work flow in the tool
- All necessary parts of readme are taken as input
- No extra hassle for inserting author and contributors
- Installation and usage steps preview available
- Output format present as a downloadable file
- Copy to clipboard is also available
- Markdown preview ha salso been included
- Support for inserting images is present

## Motivation

This tool has been an outcome of a semester project under Sofware Engineering course. The main purpose was to implement all the software lifecycle processes and design patterns in a practical solution.

This tool has also been possible because of the continuous feedback by our mentor Akhila.

## Contributors

- [Shubhankar Bhadra](http://github.com/shobhi1310)
- [Tapish Kumar Ojha](http://github.com/tapish2000/)

## Usage

The working link of the tool is present [here](http://tapish2000.pythonanywhere.com/). On clicking the link, you will be welcomed with a starting page where you have to insert the link to your github repository. You can then follow on the basic workflow from the website.

## Development and Contribution

For those who wish to extend it further or reproduce bugs and work on them please follow the following procedure:

First, fork the repository, then clone it into your system using

`git clone https://github.com/{your_user_name}/readme_toolkit`

Move to the `readme_toolkit` directory using `cd readme_toolkit`

The toolkit is created using Django which requires `python 3`. First install python 3 into your system. You can then proceed.

It is highly suggested that you create a virtual environment for deploying these files.

For Ubuntu machine:
```
$ virtualenv venv
$ source venv/bin/activate
```
It will reflect as `(venv)$ `in your terminal implicating that your virtual environment has activated.

You can run the following command independent of virtual machine.
`pip install -r requirements.txt`

This will install all the required dependencies. You can the use `python3 manage.py runserver` to start the server and it will be accessible in your locahost from your web-browser.

Also, add the following content into a file named `config.json` which should be part of your working directory:
```json
{
    "GITHUB_TOKEN" : "YOUR_KEY",
    "DJANGO_SECRET_KEY" : "YOUR_KEY",
    "CLOUDINARY_CLOUD_NAME" : "YOUR_KEY",
    "CLOUDINARY_API_KEY" : "YOUR_KEY",
    "CLOUDINARY_API_SECRET" : "YOUR_KEY",
    "MONKEYLEARN_API_KEY" : "YOUR_KEY",
    "MONKEYLEARN_MODEL_ID" : "YOUR_KEY"
}
```
All the kys will be available in the respective user manuals of their website.

In case you have found any flaws, or want to improve some existing features or you want some new features, create an [issue](https://github.com/tapish2000/readme_toolkit/issues) on this repository.