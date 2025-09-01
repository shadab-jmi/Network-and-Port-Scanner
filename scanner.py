import argparse
import nmap
import requests
import socket

def argument_parser():
    parser = argparse.ArgumentParser(description="TCP Port Scanner will accept Hostname/IP Address along with a list of port ot scan.")
    parser.add_argument("-o","--host",nargs="?",help="Host IP Address")
    parser.add_argument("-p","--ports",nargs="?",help="Comma Seperated port list. Example: '22,80,443,8080'")
    var_args = vars(parser.parse_args())
    return var_args

def nmap_scan(host_id, port_num):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id,port_num)
    state= nm_scan[host_id]['tcp'][int(port_num)]['state']
    name= nm_scan[host_id]['tcp'][int(port_num)]['name']
    version= nm_scan[host_id]['tcp'][int(port_num)]['version']
    extrainfo= nm_scan[host_id]['tcp'][int(port_num)]['extrainfo']
    result= f"[*] {host} tcp/{port} {state} {name} {version} {extrainfo}"
    return result

if __name__=='__main__':
    try:
        users_args=argument_parser()
        host = users_args["host"]
        
        # print(r)
        try:
            gethostby_=socket.gethostbyname(host)
            r=requests.get("http://"+gethostby_)
#            host=gethostby_
            if r.status_code:
                print("The IP Address of the Website "+ host + " is: "+gethostby_)
                host=gethostby_
                print(f"Successfully connected to {host}.")
                ports = users_args['ports'].split(",")
                for port in ports:
                    print(nmap_scan(host, port.strip()))
            else:
                print("Machine not reachable.")
        except requests.exceptions.RequestException:
            print("Machine not reachable.")
    except AttributeError:
        print("ERROR in input, Please provide the command line arguments before running the script.")
