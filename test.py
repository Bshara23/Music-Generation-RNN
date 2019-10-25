import os
import subprocess

# Command to execute
# Using Windows OS command
cmd1 = 'timw32g'
cmd2 = './prog/abc2wav.sh'
#subprocess.call()
# Using os.system() method
#os.system(cmd)

abc_file = 'tmp.abc'
path_to_tool = './prog/abc2wav.sh'
test = 'GREPDB="echo 123"; /bin/bash -c "$GREPDB"'
cmd = "{} {}".format(path_to_tool, abc_file)
test2 = "abc2midi " + abc_file + " -o \"aaa.mid\""
#os.system(test2)
print(subprocess.call(test2, shell=True))

