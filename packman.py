from git import Repo
import yaml
import sys, os, shutil

def packman(source):

    # If we're given a github repo
    if "/" in source:
        if yn("Cloning from http://github.com/" + source + ", ok? (y/n)"):
            if os.path.isdir("plugins/" + source.split("/",1)[1]):
                print("Plugin is already installed! You need to delete it (it's in your plugins folder).")
            else:
                try:
                    Repo.clone_from("http://github.com/" + source, "plugins/" + source.split("/",1)[1])
                except:
                    print("Something went wrong in the cloning! Check your repository address.")
                    sys.exit()
                else:
                    print("Success! Now go reference it in your config.yml!")
        else:
            print("Aborting...")
            sys.exit()

    # If we're given a name
    else:
        print("Reading maps...")
        with open('maps.yml', 'r') as f:
        	maps = yaml.load(f)

        if source in maps:
            print("Found key: " + source)
            repo = "http://github.com/" + maps[source]
            print("Cloning from " + repo + "...")
            try:
                Repo.clone_from(repo, "plugins/" + source)
            except:
                print("Something went wrong in the cloning! Check your repository address and make sure that it isn't already installed.")
                sys.exit()
            else:
                print("Success! Now go reference it in your config.yml!")
        else:
            print("No plugin named " + source + " in maps.yml! Check your spelling, and if all else fails, use the actual github repository name.")

def yn(mesg):
    return input(mesg + " ").lower() in ('y','yes')
