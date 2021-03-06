import enum
import os


class Commands(enum.auto):
    Status = 'nordvpn status'
    Login = 'nordvpn login'
    Logout = 'nordvpn logout'
    Account = 'nordvpn account'
    Connect = 'nordvpn connect '
    Disconnect = 'nordvpn disconnect'
    Settings = 'nordvpn settings'
    Set = 'nordvpn set'


class Options(enum.auto):
    autoconnect = 'autoconnect'
    cybersec = 'cybersec'
    killswitch = 'killswitch'
    notify = 'notify'
    obfuscate = 'obfuscate'
    protocol = 'protocol'
    technology = 'technology'


class LinuxCli(object):

    def get_status(self):
        return self.run_command(Commands.Status)

    def get_account(self):
        return self.run_command(Commands.Account)

    def is_user_logged_in(self):
        output = self.run_command(Commands.Login)
        return 'You are already logged in' in output

    def login(self, username, password):
        output = self.run_command(Commands.Login + ' -u ' + username + ' -p ' + password)
        return 'Welcome to NordVPN!' in output

    def logout(self):
        output = self.run_command(Commands.Logout)
        return 'You are logged out' in output

    def is_update_available(self):
        output = self.run_command(Commands.Status)
        return 'A new version of NordVPN is available!' in output

    def connect(self, server):
        output = self.run_command(Commands.Connect + server)
        return 'You are connected to' in output

    def disconnect(self):
        output = self.run_command(Commands.Disconnect)
        return 'You are disconnected from NordVPN' in output

    def get_settings(self):
        return self.run_command(Commands.Settings)

    def set_auto_connect(self, argument):
        return self.set(Options.autoconnect, argument)

    def set_cybersec(self, argument):
        return self.set(Options.cybersec, argument)

    def set_killswitch(self, argument):
        return self.set(Options.killswitch, argument)

    def set_notify(self, argument):
        return self.set(Options.notify, argument)

    def set_obfuscate(self, argument):
        return self.set(Options.obfuscate, argument)

    def set_protocol(self, argument):
        return self.set(Options.protocol, argument)

    def set_technology(self, argument):
        return self.set(Options.technology, argument)

    def set(self, option, argument):
        if argument:
            argument = 'on'
        if not argument:
            argument = 'off'
        output = self.run_command(Commands.Set + " " + option + " " + argument)
        return 'successfully.' in output

    def run_command(self, command):
        return os.popen(command).read()


# cli = LinuxCli()
# print(cli.getStatus(Commands.Status_status))
# print(cli.getStatus(Commands.Status_current_server))
# print(cli.getStatus(Commands.Status_country))
# print(cli.getStatus(Commands.Status_city))
# print(cli.getStatus(Commands.Status_ip))
# print(cli.getStatus(Commands.Status_technology))
# print(cli.getStatus(Commands.Status_protocol))
# print(cli.getStatus(Commands.Status_transfer))
# print(cli.getStatus(Commands.Status_uptime))
# print(cli.isUserLoggedIn())
# print(cli.isUpdateAvailable())

