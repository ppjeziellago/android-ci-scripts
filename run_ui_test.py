from os import environ, system
import subprocess

'''

[REQUIRED] 
Env var `PROJECT_LOCATION` with project dir path

[OPTIONAL]
Env var `IGNORED_MODULES_UI_TEST` with modules to ignore on instrumented tests

Example:
IGNORED_MODULES_UI_TEST=":modulea, :moduleb, :modulec, :libraries:lib"

'''

def run_shell(command, enable_output):
    print('\n\n[RUNNING] {}'.format(command))
    return subprocess.Popen(command, 
            shell=True, 
            stdout=subprocess.PIPE if enable_output else None, 
            stderr=subprocess.PIPE
    ).communicate()

def get_modules(project_dir):
    output, error = run_shell("cd {}; ./gradlew tasks --all | grep connectedDebugAndroidTest".format(project_dir), True)
    if error: raise Exception('\n\n[ERROR]\n{}'.format(error))

    modules=[ module.split('-')[0].strip() for module in output.strip().split('.')[:-1] ]

    modules_with_task=''
    ignored_modules=''

    try: 
        ignored_modules=environ['IGNORED_MODULES_UI_TEST']
        print('[IGNORING MODULES] {}'.format(ignored_modules))
    except: 
        pass

    for module in modules: 
        if ':{}'.format(module.strip().replace(':connectedDebugAndroidTest','')) not in ignored_modules:
            modules_with_task +=' :{}'.format(module)

    return modules_with_task

def run_instrumented_test(project_dir, modules):
    instrumented_test_gradle_task="cd {}; ./gradlew {}".format(project_dir, modules)

    _, error = run_shell(instrumented_test_gradle_task, False)

    if error: raise Exception("\n\n[ERROR]\n{}".format(error))

def main():
    project_dir=environ['PROJECT_LOCATION']

    modules=get_modules(project_dir)

    run_instrumented_test(project_dir, modules)


if __name__ == '__main__':
    main()