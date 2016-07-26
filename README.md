# Pythonista and Working Copy

## Working Copy --> Pythonista
[Appex script](http://omz-software.com/pythonista/docs/ios/appex.html) that enables Pythonista to download a git repo, file, or folder from a share sheet from the Working Copy app

Pre requisites:
* [Pythonista for iOS](http://omz-software.com/pythonista/)
* [Working Copy app for iOS](https://workingcopyapp.com)

Workflow:
* In _Working Copy_ open a GitHub repository that you want copied into _Pythonista_
  * if your needs are more modest, you can even select a single file or folder
* Click the Share icon at the upper right corner of the Working Copy screen
* Click Run Pythonista Script
* Click on this script
* Click the run button

When you [return to Pythonista](pythonista://) your files should be in the 'from Working Copy' directory.

## Pythonista --> Working Copy
Working Copy has a "__save to Working Copy__" Share Sheet action (you might have to enable in Share Sheet, More...
This currently only works on a single file basis (e.g. not a whole folder all at once).

Workflow:
* Open the file of interest in the Pythonista editor
* Click the wrench icon at the upper right
* Click the "Share..." button
* Click "Save in Working Copy" button
* Select the repo that you want to save the file into
* Click "Save As..."
* Change the filename if you want to and click "Save As..." again
* Click "Just Save" if you want to bundle multiple files into a single commit --or-- Type your commit message and click "Commit"

__Now we have an end to end workflow: GitHub --> Working Copy --> Pythonista --> Working Copy --> GitHub__

See: https://forum.omz-software.com/topic/2382/git-or-gist-workflow-for-pythonista/24
