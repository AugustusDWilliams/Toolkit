# Elastic Beanstalk Setup

- git init
- touch .gitignore
- open .gitignore
  - add all files and folders which should not be pushed to container
- git add -A
- git commit -m
- git push (if applicable)
- eb init [app_name]
- eb create [env_name]
- open the aws elastic beanstalk console
  - go to configuration > software
    - change the WSGIPath to "run.py"
    - change the static directory from "static/" to "[app_name]/static/"
- eb deploy
