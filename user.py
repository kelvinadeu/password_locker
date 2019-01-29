class user:
    """
    This class will contain all details of the user
    """
    def_init_(self,login,password):
      """
      This will create unique details for each of the user class
      """
      self.login = login
      self.password = password

    def_exist(self,password):
      """
      This will use the password to authenticate the user before showing the passwords
      Args:
           the user password
      return:
             boolean
      """
