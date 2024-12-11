
import passlib.hash


class FilterModule(object):
    def filters(self):
        return {
            'odoo_passwd': self.odoo_passwd,
        }

    def odoo_passwd(self, passwd):
        salt = b'eiPhaenee1eejeuNg4Ki'
        return passlib.hash.pbkdf2_sha512.encrypt(passwd, salt=salt)
