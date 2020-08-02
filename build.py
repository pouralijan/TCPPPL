#!/usr/bin/env python3

import subprocess
import os
import shutil

build_dir = "./CPP_NOTEBOOK_BUILD"

def run_command(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

def cmake():
    cwd = os.getcwd()
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.mkdir(build_dir)
    os.chdir(build_dir)
    res = run_command("cmake .. 2>1")
    os.chdir(cwd)
    return res.returncode

def build():
    if cmake() != 0:
        return False, "Cmake Faild"
    cwd = os.getcwd()
    os.chdir(build_dir)
    res = run_command("make -j 2>1")
    os.chdir(cwd)
    if res.returncode != 0:
        return False, "Make Faild"
    return True, "Make successful"
