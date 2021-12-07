from user import User
from post import Post

app_user_one = User("Vanshi@hmail.com", "Vanshika", "skfhiwe", "Web Developer")
app_user_one.get_user_info()

app_user_one.change_job_title("Software Developer")
app_user_one.get_user_info()

app_user_two = User("nandinidharwal@gmail.com", "Nandini", "skfhiwe","Data Scientist")
app_user_two.get_user_info()

new_post = Post("On a secret mission today", app_user_two.name)
new_post.get_post_info()