# <a id="Top-of-Page">How to Use Git Bash with Git Hub</a>
##### Step-by-Step Fundamentals
***
<a id="Contents"></a>
### Cotents:
[1. Create Remote Repository on GitHub](#Create-Repo)<br>
[2. Clone Repository Locally with SSH](#Clone-Repo)<br>
[3. Commit and Push Repository Changes to GitHub](#Commit-Push-Changes-to-GitHub)<br>
[4. Commit to Alternative Branch on GitHub](#Commit-To-Alt-Branch)<br>
[References](#References)<br>
[Bottom of Page](#Bottom-of-Page)<br>
***
### <a id="Create-Repo">1. Create Remote Repository on GitHub:</a>
<div style="text-align: justify">
 - Got to <a href="https://github.com/">github.com</a>
 - In the 'Repositories panel, select `New`.<br>
 
<img src=".\images\NewRepo-GitHub.png" title="github.com" /><br>
 - Fill out the repo name and description.
 - Check `Add a README file` and if needed `Add .gitignore`.
     - A '.gitignore' file allows you to populate filenames and file extensions that you do not wish to be included in your commits to the repository.
     - A common use for this file is to prevent config files that have api keys or passwords stored in them from making their way into your repository.
     -'.gitignore' files come prepopulated with certain files and extension names specific to your programming language, but can be customized to fit your needs.
 - Apply the settings shown in the below image for a standard public repo and click `Create repository`.<br>
 
<img src="images\NewRepoSettings-GitHub.png" title="Create a new repository" /><br>
 - Now you should have a blank repo.<br>
 
<img src="images\NewRepoBlank-GitHub.png" title="New repository" /><br>
[Top of Page](#Top-of-Page)---[Contents](#Contents)---[Bottom of Page](#Bottom-of-Page)<br>
***
### <a id="Clone-Repo">2. Clone Repository Locally with SSH:</a>
 - Copy your GitHub address for SSH cloning.<br>
 
<img src="images\GetAddressForClone-GitHub.png" title="GitHub address for SSH cloning" /><br>
 - In Bash type `git clone <address>`
     - In this case, `<address>` is 'git@github.com:jasonjgarcia24/fintech-challenges.git')
     - If the note "The authenticity of host 'github.com'... can't be established.... Are you sure you want to continue connecting (yes/no)?", type `yes`.
 - Now you have your local repository and can apply changes as needed locally only.<br>
 
<img src="images\CloneRepo-GitHub-Windows.png" title="Repo cloning" /><br>
[Top of Page](#Top-of-Page)---[Contents](#Contents)---[Bottom of Page](#Bottom-of-Page)<br>
***
### <a id="Commit-Push-Changes-to-GitHub">3. Commit and Push Repository Changes to GitHub:</a>
 - In Bash type `cd fintech-challenges` to enter into the 'fintech-challenges' repository.
 - Apply changes to the repo as necessary.
 - In Bash type `git add -A` to stage the changes to the Git repository.
     - This is telling the Git application to add any changes to the staging area, and the `-A` means I want to add all the files in this repository.<br>

<img src="images\AddChangesRepo-GitHub-Windows.png" title="Add changes to the staging area" /><br>
 - In Bash type `git commit -m "<message>"` to commit changes to your remote git. Now you're ready to push the changes.
     - In this case, `<message>` is 'First commit of challenge 01.')
     - Use `-m <message>` to type in a commit message. This message is a descriptive message to document a description of the changes.
 - In Bash type `git push origin main` to push changes to the 'main' GitHub branch.<br>

<img src="images\PushChangesRepo-GitHub-Windows.png" title="Push changes to GitHub" /><br>
 - You can now go to your remote repository on <a href="https://github.com/">github.com</a>, hit refresh, and view the updated repository with the changes applied.<br>

<img src="images\SuccessfulPushToMain-GitHub-Windows.png" title="Updated GitHub repository" /><br>
[Top of Page](#Top-of-Page)---[Contents](#Contents)---[Bottom of Page](#Bottom-of-Page)<br>
***
### <a id="Commit-To-Alt-Branch">4. Commit to Alternative Branch on GitHub:</a>
 - In Bash type `git checkout -b <new branch name>`.
     - The -b means that you will create a new branch that doesn't already exist.
     - In this case, `<new branch name>` will be '01-challenge'.
     - Notice also that the branch name in Bash will change from '(main)' to '(01-challenge)'.
 - Apply changes to the repo as necessary.
 - In Bash type `git add -A` to stage the changes to the Git repository.
     - This is telling the Git application to add any changes to the staging area, and the `-A` means I want to add all the files in this repository.<br>
 - In Bash type `git commit -m "<message>"` to commit changes to your remote git. Now you're ready to push the changes.
     - In this case, `<message>` is 'First commit of challenge 01.')
     - Use `-m <message>` to type in a commit message. This message is a descriptive message to document a description of the changes.
 - In Bash type `git push origin 01-challenge` to push changes to the '01-challenge' GitHub branch.<br>

<img src="images\SuccessfulPushToAltBranch-GitHub-Windows.png" title="Push changes to GitHub" /><br>
 - You can now go to <a href="https://github.com/">github.com</a> and hit refresh. You'll notice the 'main' repository has not been updated but that there is now an additional branch.<br>

<img src="images\NewBranch-GitHub-Windows.png" title="Updated GitHub branch" /><br>
 - In the dropdown menu next to the number of branches, switch to your new branch (in this case '1-challenge').
 - In the '01-challenge' branch page, click on `Compare & pull request`.<br>

<img src="images\NewBranchPage-GitHub-Windows.png" title="New GitHub branch page" /><br>
 - Now you've opened a new "pull request" page.
     - Notice the comment for this branch is the same as what was entered in the Bash window with the `git commit -m "<message>"` command.<br>

<img src="images\NewBranchPullRequest-GitHub-Windows.png" title="New GitHub branch page" /><br>
 - Click `Create pull request`.
 - Since this repo is all yours, you can just merge this pull request right into 'main' by clicking `Merge pull request` and then `Confirm merge`.<br>

<img src="images\NewBranchMerge-GitHub-Windows.png" title="Merge new GitHub branch" /><br>
 - You should now see some form of the message 'Pull request successfully merged and closed'. You can now leave the branch or delete it, it's your preference.
 - Navigate back to the repo's homepage and you can see your alternative branches merged file(s) have been added to the 'main' branch.<br>

<img src="images\SuccessfulNewBranchMerge-GitHub-Windows.png" title="Successful merge of new branch to remote repo on GitHub" /><br>
[Top of Page](#Top-of-Page)---[Contents](#Contents)---[Bottom of Page](#Bottom-of-Page)<br>
***
### <a id="References">References:</a>

 - <a href="https://www.youtube.com/channel/UC2SYjKBTEOCtLEjVC6ixISw/featured">The Boot Camp</a>, "Git and GitHub" <i>YouTube</i>, commentary by GitHub user <a href="https://github.com/hannahpatellis">hannahpatellis</a>, 19 Jan. 2019, https://youtu.be/seICQOd2qsY.<br><br>
</div>
***
<a id="Bottom-of-Page"></a>
[Top of Page](#Top-of-Page)<br>
[Contents](#Contents)<br>
[1. Create Remote Repository on GitHub](#Create-Repo)<br>
[2. Clone Repository with SSH](#Clone-Repo)<br>
[3. Commit and Push Repository Changes to GitHub](#Commit-Push-Changes-to-GitHub)<br>
[4. Commit to Alternative Branch on GitHub](#Commit-To-Alt-Branch)<br>
[References](#References)