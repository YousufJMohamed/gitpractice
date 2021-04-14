from git import Repo

PATH_OF_GIT_REPO = r'C:\Users\mohamed yousuf\Desktop\gitpractice\gitpractice'
 # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comitted'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add('found.txt','today.py')
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
        print("success")
    except:
        print('Some error occured while pushing the code')    

git_push()