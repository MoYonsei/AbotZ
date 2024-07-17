import subprocess

def create_emulator():
    try:
        # لا يوجد أمر محدد لإنشاء محاكي في BlueStacks عبر adb مباشرة، نستخدم المحاكي الافتراضي
        emulator_id = "emulator-5554"
        return emulator_id
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to emulator: {e}")
        return None
    

def extract_emulator_id(output):
    # قم بتحليل المخرجات لاستخراج معرف المحاكي
    # تحتاج إلى تعديل هذا بناءً على شكل المخرجات
    for line in output.split('\n'):
        if "Emulator ID" in line:
            return line.split(":")[1].strip()
    return None

def install_app(emulator_id, app_path):
    command = f'adb -s {emulator_id} install {app_path}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def launch_app(emulator_id, package_name):
    command = f'adb -s {emulator_id} shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def stop_app(emulator_id, package_name):
    command = f'adb -s {emulator_id} shell am force-stop {package_name}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr
