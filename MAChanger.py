import subprocess
import re
import optparse

class Mac_changer:

    

        def __init__(self):
            self.MAC = ""

        def get_MAC(self, iface):
            output = subprocess.run(['/sbin/ifconfig', iface], shell=False, capture_output=True)

            cmd_result = output.stdout.decode('utf-8')

            pattern = r'ether\s[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}:[\da-f]{2}'
            
            regex = re.compile(pattern)

            
            ans = regex.search(cmd_result)

            

            

            

            current_mac = ans.group().split(" ")[1]

            self.MAC = current_mac

            return current_mac

            

                



                

            
        
        def change_mac(self, iface, new_mac):
                    print("\n[+] Current MAC Address is, ", self.get_MAC(iface))

                    output = subprocess.run(["/sbin/ifconfig", iface, "down"], shell=False, capture_output=True)

                    print(output.stderr.decode("utf-8"))

                    output = subprocess.run(["/sbin/ifconfig", iface, "hw", "ether", new_mac], shell=False, capture_output=True)

                    print(output.stderr.decode("utf-8"))

                    output = subprocess.run(["/sbin/ifconfig", iface, "up"], shell=False, capture_output=True)

                    print(output.stderr.decode("utf-8"))

                    print("\n[+]New MAC Address: ", self.get_MAC(iface), "\n")

                    return self.get_MAC(iface)

class color:
    green = "\033[92m"

    red = "\033[91m"

    end = "\033[0m"

parser = optparse.OptionParser()

parser.add_option("-i", "--iface", dest="interface", help="Interface that you would like to change the MAC address of. (i.e. eth0) HOW TO USE: MACchange.exe -i eth0 -m 00:1a:2b:3c:4d:5e")

parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address you want to have set to your current MAC address. (i.e. 00:1a:2b:3c:4d:5e  Note: you can only use letters A - F) HOW TO USE: MACchange.exe -i eth0 -m 00:1a:2b:3c:4d:5e")

(options, arguments) = parser.parse_args()

interface = str(options.interface)

new_mac = str(options.new_mac)

if not options.interface:
    print("\nNo interface was provided.")

if not options.new_mac:
    print("\nNo new MAC address was provided.")

if __name__ == "__main__":
    try:
        mc = Mac_changer()

        mac = mc.get_MAC(interface)

        print(mac)

        ## ONLY LETTERS A - F ##

        curr_mac = mc.change_mac(interface, new_mac)

        print(color.green, "<----Successfully changed MAC address---->", color.end, "\n")

    except AttributeError:

        print(color.red, "\nERROR: No 'ether' value in interface\n", color.end)

    except:

        print(color.red, "\nERROR: Could not successfully change MAC Address\n", color.end)
