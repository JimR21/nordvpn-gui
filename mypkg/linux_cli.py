import enum
import os


class Commands(enum.auto):
    Status = 'nordvpn status'
    Status_status = 'Status'
    Status_current_server = 'Current server'
    Status_country = 'Country'
    Status_city = 'City'
    Status_ip = 'Your new IP'
    Status_technology = 'Current technology'
    Status_protocol = 'Current protocol'
    Status_transfer = 'Transfer'
    Status_uptime = 'Uptime'
    Login = 'nordvpn login'
    Logout = 'nordvpn logout'


class LinuxCli(object):

    def get_status(self, status_command):
        output = self.run_command(Commands.Status)
        lines = output.split('\n')
        for line in lines:
            if status_command in line:
                return line.split(': ')[1]

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

