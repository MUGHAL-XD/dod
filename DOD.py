import os
import git
import subprocess
import platform

def upload_to_github(repo_path, file_path, commit_message):
    repo = git.Repo(repo_path)
    repo.git.add(file_path)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

def run_uploaded_file(file_path):
    platform_architecture = platform.architecture()[0]
    if platform_architecture == '64bit':
        subprocess.run(['python', file_path])
    elif platform_architecture == '32bit':
        print("Sorry, 32-bit systems are not supported for this example.")
    else:
        print("Unknown architecture.")

if __name__ == "__main__":
    # Replace these paths and file names with your actual values
    local_file_path = 'xd.py'
    github_repo_path = 'https://github.com/MUGHAL-XD/dod.git'
    commit_message = 'xd.py'

    upload_to_github(github_repo_path, local_file_path, commit_message)
    run_uploaded_file(local_file_path)
