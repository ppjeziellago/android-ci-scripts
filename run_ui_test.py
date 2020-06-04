from os import environ, system
import subprocess

# `environ['PROJECT_LOCATION']` Required
# `environ['IGNORED_MODULES_UI_TEST']` Optional

PROJECT_DIR=environ['PROJECT_LOCATION']

IGNORED_MODULES_UI_TEST=environ['IGNORED_MODULES_UI_TEST']

RUN_INSTRUMENTED_TEST_COMMAND="cd %s; ./gradlew %s"

LIST_INSTRUMENTED_TEST_MODULES = "cd %s; ./gradlew tasks --all | grep connectedDebugAndroidTest"

def run_shell(command):
    print('\n\n[RUNNING] %s' % command)
    return subprocess.Popen(command, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
    ).communicate()

output, error = run_shell(LIST_INSTRUMENTED_TEST_MODULES % PROJECT_DIR)

if error: raise Exception('\n\n[ERROR]\n%s' % error)

modules=[ module.split('-')[0].strip() for module in output.strip().split('.')[:-1] ]

modules_inlined=''

for module in modules: 
    if module not in IGNORED_MODULES_UI_TEST:
        modules_inlined +=' %s' % module

instrumented_test_gradle_task=RUN_INSTRUMENTED_TEST_COMMAND % (PROJECT_DIR, modules_inlined)

_, error = run_shell(instrumented_test_gradle_task)

if error: raise Exception("\n\n[ERROR]\n%s" % error)
