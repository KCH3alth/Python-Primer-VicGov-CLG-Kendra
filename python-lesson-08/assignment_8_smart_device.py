class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("\nThis is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name="Test app"):
        print(f"Installing {app_name}...")
        self.app_list.append(app_name) if app_name not in self.app_list else self.app_list
        return self.app_list

    def delete_app(self, app_name):
        print(f"Uninstalling {app_name}...")
        self.app_list.remove(app_name)
        return self.app_list
    
device_a = SmartDevice(98765, 'Smasnug', 7.1)
device_a.report()

device_a.install_app()
device_a.install_app('Wordle')
device_a.install_app('Connections')
device_a.install_app('Wordle')
print(f'\nThe apps currently installed are: {device_a.app_list}.\n')
device_a.delete_app('Test app')
print(f'\nThe apps currently installed are: {device_a.app_list}.\n')