Cloned the TerminalWizard repository using the following command.
karthik@karthik-vostro-3500:~/amfoss$ git clone https://github.com/KshitijThareja/TerminalWizard.git

Did the Challenge 1 using the cloned TerminalWizard main branch. Created "codes" folder and added Part-1.txt and also copied Impedimenta.py to "codes".

karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git add .
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git status
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git commit -m "challenge1 done"
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git push -u -f origin main

Did the Challenge 2 using the cloned TerminalWizard main branch. Created Part-2.txt in "codes" and also copied Stupefy.py to "codes".

karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git add .
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git status
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git commit -m "challenge2 done"
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git push -u -f origin main

Used the following command to list the local & remote branches of TerminalWizard
karthik@karthik-vostro-3500:~/amfoss/TerminalWizard$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/defenseAgainstTheDarkArts
  remotes/origin/divination
  remotes/origin/herbology
  remotes/origin/historyOfMagic
  remotes/origin/main
  remotes/origin/potions
  remotes/origin/thegraveyard
  remotes/origin/transfiguration


Copied the spellbook/Riddikulus.py from the TerminalWizard defenseAgainstTheDarkArts branch to the local TerminalWizard main branch
karthik@karthik-vostro-3500:~/amfoss/TerminalWizard$ git checkout defenseAgainstTheDarkArts spellbook/Riddikulus.py
Updated 1 path from 17b678b

Did the Challenge 3 using the spellbook/Riddikulus.py. Created Part-3.txt in "codes" and also copied Riddikulus.py to "codes".


karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git add .
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git status
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git commit -m "challenge3 done"
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git push -u -f origin main

Checked out TerminalWizard thegraveyard branch using the following command
 
karthik@karthik-vostro-3500:~/amfoss/TerminalWizard$ git checkout thegraveyard
A	spellbook/Riddikulus.py
Switched to branch 'thegraveyard'
Your branch is up to date with 'origin/thegraveyard'.

Did the Challenge 4.  Created Part-4.txt in "codes" and also copied Priori Incantatem.py to "codes".

karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git add .
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git status
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git commit -m "challenge4 done"
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git push -u -f origin main

Created finalcode.txt using the codes present in the Part_x.txt files and removed all other files 
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ rm P*.txt
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ rm *.py

karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git add .
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git status
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git commit -m "added finalcode.txt and removed all other files"
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git push -u -f origin main


Decoded the final code using the following command.


karthik@karthik-vostro-3500:~/amfoss/TerminalWizard$ echo <base64EncodedString> | base64 --decode
https://github.com/TheHuntsman4/TheFinalSpell

As per the instructions in the TheFinalSpell repository, checked out TheFinalSpell using following command
karthik@karthik-vostro-3500:~/amfoss$ git clone https://github.com/TheHuntsman4/TheFinalSpell.git
Cloning into 'TheFinalSpell'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 6 (delta 0), reused 6 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.

Ran the python script in the terminal and took the screenshot of the output. - thefinalspell-message.png
Copied the screenshot, thefinalspell-message.png to amfoss-tasks/task-01 and added link to include the screenshot at the end of this page.

We will use the below commands to add, commit and push the new files(SOLUTION.MD & thefinalspell-message.png) to github.

karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git add .
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git status
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git commit -m "added SOLUTION.md and thefinalspell-message.png"
karthik@karthik-vostro-3500:~/amfoss/amfoss-tasks/task-01$ git push -u -f origin main

![The Final Spell Message](/task-01/thefinalspell-message.png "The Final Spell Message")



