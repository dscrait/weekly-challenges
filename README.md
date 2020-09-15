# weekly-challenges
One stop for submitting your weekly challenges! 

## How to start contribution?

**1.** Fork [this](https://github.com/dscrait/weekly-challenges.git) repository.

**2.** Clone the forked repository.
```terminal
git clone https://github.com/<your-github-username>/weekly-challenges
```

**3.** Navigate to the project directory.
```terminal
cd weekly-challenges
```

**4.** Navigate to the relevant week.
```terminal
cd week-3
```

**5.** Create a new branch.
```terminal
git checkout -b <your_branch_name>
```

**6.** Make a new directory with your Full_Name.
```terminal
mkdir FirstName_LastName
```
**6.1** Create a file wallpaperChanger.py
```terminal
touch wallpaperChanger.py
```

**7.** Follow the instructions in the challenge README and make changes in source code.

**7.1.** Before commiting your changes add the following commands on your terminal
```terminal 
git remote add upstream https://github.com/dscrait/weekly-challenges.git
```
```terminal
git pull upstream master
```

**8.** Commit your changes.

```terminal
  git add .
  git commit -m "<your_commit_message>"
  
  # If so try to use conventional commit messages using the guide: https://www.conventionalcommits.org/en/v1.0.0/
```

**9.** Push your local branch to the remote repository.
```terminal
git push 
```

**9.** Create a Pull Request! 
