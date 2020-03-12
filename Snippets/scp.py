import os
from smb import smb_structs
from smb.SMBConnection import SMBConnection

smb_structs.SUPPORT_SMB2 = False


class SCP:

    def __init__(self, user, pwd, client, server):
        self.conn = SMBConnection(user, pwd, client, server, use_ntlm_v2=True)
        self.conn.connect(server, 139)

    def get_file(self, share, folder, filename):
        remote_file = os.path.join(folder, filename)
        local_file = open(filename, "wb")
        self.conn.retrieveFile(share, remote_file, local_file)
        print("Retrieved {}".format(remote_file))

    def send_file(self, share, folder, filename):
        local_file = os.path.join(folder, filename)
        remote_file = open(filename, "rb")
        self.conn.storeFile(share, local_file, remote_file)
        print("Uploaded {}".format(local_file))


if __name__ == "__main__":
    username = "[ChemDAQ Username]"
    password = "[ChemDAQ Password]"
    remote_name = username
    server = "chemdaqserver"
    share = "Users"
    target_dir = "Dan Williams"
    target_file = "CM-401-B-3.00 ChemDAQ SafeCide User's Manual March 23 2017.docx"
    conn = SCP(username, password, remote_name, server)
    conn.get_file(share, target_dir, target_file)
