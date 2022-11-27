### Builds as a private Artifactory

Application Purpose - Will create a random number between 2, 100 and calculate all Prime numbers that come before it.

<hr>
        
#### There are two ways to pip install from a private repository.
##### 1. Create a pip.conf file with your index url specified inside (found within artifactory website). 
```
Linux : Store it on etc/pip.conf
Windows : Store it on %appdata%/roaming/pip/pip.conf
```

##### 2. Specify the url within the pip command using --find-links= command, see example : 
`pip install ganesha_experimental==5.0.0 --find-links=https://awakzdev.jfrog.io/artifactory/`

#### Import using
`from ganesha_experimental.main import *`
