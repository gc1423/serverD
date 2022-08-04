#!/usr/bin/env bash
GIT_COMMAND="/usr/bin/env git"
TEMPLATE_GIT_URI="ssh://git@git.jetbrains.space/gc1423/demos-python/python_template.git"
DEFAULT_PROJECT_NAME="samplemod"
PROJECT_NAME="${1:-samplemod}"
CURRENT_FOLDER=$(pwd)
PROJECT_FOLDER="$CURRENT_FOLDER/$PROJECT_NAME"

echo $PROJECT_NAME
echo $CURRENT_FOLDER
echo $PROJECT_FOLDER


## download template project
$GIT_COMMAND clone $TEMPLATE_GIT_URI $PROJECT_NAME

cd $PROJECT_FOLDER

# change project name
# TODO what about linux?
#  In the version (BSD) of sed that ships with Mac OS X, the -i flag expects a mandatory <extension> argument, which your command is missing. An empty string ("") should follow the -i flag if you want to edit the file in-place with this version of sed.
sed -i "" "s^|\+ABSPATH\+|^$PROJECT_FOLDER^g" supervisord.d/supervisord.conf
sed -i "" "s^|\+PROJECT_NAME\+|^$PROJECT_NAME^g" ./setup.py
# use ^ as separator in case paths go wrong

mv python_template $PROJECT_NAME
mv launch.py "${PROJECT_NAME}_launch.py"

# make the project a new git repo
rm -rf .git

$GIT_COMMAND init
$GIT_COMMAND add .
$GIT_COMMAND commit -m "init"