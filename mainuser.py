from user import User
from post import Post

app_user_one = User("jaja@hdh.com", " James", "pwd", "DevOps Engineer")
app_user_one.get_user_info()

""""app_user_one.change_job_title("DevOps trainer")
app_user_one.get_user_info()"""

app_user_two = User("aa.@aa.com", "Eden", "cde", "Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission", app_user_one.name)
new_post.get_post_info()
