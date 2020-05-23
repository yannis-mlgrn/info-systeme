import platform
import socket
import os


dict = {"machine" : platform.machine(), "networkName" : platform.node() , "plat>
print("utilisator : " + os.getlogin())
print("network name : "+ dict.get("networkName"))
print("system : " + dict.get("distribution"))
print("platform : " + dict.get("platform"))

