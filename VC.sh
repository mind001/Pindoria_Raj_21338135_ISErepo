# Step 1: Initialize a local Git repository
$ git init Pindoria_Raj_21338135_ISErepo
Initialized empty Git repository in /path/to/Pindoria_Raj_21338135_ISErepo/.git/

# Step 2: Change to the repository directory
$ cd Pindoria_Raj_21338135_ISErepo

# Step 3: Create the directory structure
$ mkdir code
$ mkdir documents

# Step 4: Start tracking the directories and files
$ git add code/
$ git add documents/

# Step 5: Make the initial commit
$ git commit -m "Initial commit"
[master (root-commit) 0123456] Initial commit
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 code/.gitkeep
 create mode 100644 documents/.gitkeep

# Step 6: Create a branch for each assessment task
$ git branch task1
$ git branch task2
$ git branch task3
$ git branch task4
$ git branch task5
$ git branch task6
$ git branch task7
$ git branch task8
$ git branch task9
$ git branch task10

# Step 7: Switch to the first branch (task1)
$ git checkout task1
Switched to branch 'task1'

# Step 8: Start working on the task, making changes to code and documents

# Step 9: Commit changes as you work on the task
$ git add code/
$ git add documents/
$ git commit -m "Implemented task1"
[task1 1234567] Implemented task1
 2 files changed, 10 insertions(+), 3 deletions(-)

# Step 10: Repeat steps 7-9 for each task

# Step 11: Merge branches when necessary
$ git checkout main
Switched to branch 'main'
$ git merge task1
Updating 890abcd..1234567
Fast-forward
 code/file1.py       | 5 ++++-
 documents/report.md | 1 +
 2 files changed, 5 insertions(+), 1 deletion(-)
