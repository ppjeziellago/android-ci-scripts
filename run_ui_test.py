from os import environ, system
import subprocess

# `environ['PROJECT_LOCATION']` Required
# `environ['IGNORED_MODULES_UI_TEST']` Optional
PROJECT_DIR=environ['PROJECT_LOCATION']

IGNORED_MODULES_UI_TEST=''

try: 
    IGNORED_MODULES_UI_TEST=environ['IGNORED_MODULES_UI_TEST']
    print('[IGNORING MODULES] %s' % IGNORED_MODULES_UI_TEST)
except: pass

RUN_INSTRUMENTED_TEST_COMMAND="cd %s; ./gradlew %s"

LIST_INSTRUMENTED_TEST_MODULES = "cd %s; ./gradlew tasks --all | grep connectedDebugAndroidTest"

def run_shell(command, enable_output):
    print('\n\n[RUNNING] %s' % command)
    return subprocess.Popen(command, 
            shell=True, 
            stdout=subprocess.PIPE if enable_output else None, 
            stderr=subprocess.PIPE
    ).communicate()

output, error = run_shell(LIST_INSTRUMENTED_TEST_MODULES % PROJECT_DIR, True)

if error: raise Exception('\n\n[ERROR]\n%s' % error)

modules=[ module.split('-')[0].strip() for module in output.strip().split('.')[:-1] ]

modules_inlined=''

for module in modules: 
    if (':%s' % module.strip().replace(':connectedDebugAndroidTest','')) not in IGNORED_MODULES_UI_TEST:
        modules_inlined +=' :%s' % module

instrumented_test_gradle_task=RUN_INSTRUMENTED_TEST_COMMAND % (PROJECT_DIR, modules_inlined)

_, error = run_shell(instrumented_test_gradle_task, False)

if error: raise Exception("\n\n[ERROR]\n%s" % error)
