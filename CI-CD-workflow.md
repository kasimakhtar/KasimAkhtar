## Workflow to build static site from gh-pages branch

This workflow pushes content automatically to another branch and can be used to add content to gh-pages when building a site. When writing the script, I had a pelican static site that was built from my gh-pages branch. The workflow was designed so that my gh-pages branch would mirror the output directory of my master branch. The workflow is based on JamesIves/github-pages-deploy-action@3.5.9 however I have adapted it to a pelican static site. 




~~~

name: CI/CD

# Triggered when a file is pushed to master branch
on:
  push:
    branches: 
      - master
 

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Allow workflow to access branch   
      - name: checkout
        uses: actions/checkout@v2
        with:
          persist-credentials: false
      # Install python
      - name: set up python 3.8
        uses: actions/setup-python@v1
        with:
          python-version: 3.8
      # Install pip, pelican, and process pelican content
      - name: Install Pelican
        run:
          python3 -m pip install --upgrade pip
          pip install invoke pelican[markdown]
          pelican content
      # Move files from output folder of master branch, to gh-pages branch
      - name: move Deploy
        uses: JamesIves/github-pages-deploy-action@3.5.9
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          BRANCH: gh-pages
          FOLDER: output
          CLEAN: true
~~~



Overall I found this workflow a useful automation tool as it allowed me to work locally, and see changes directly on the static website.
