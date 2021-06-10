import praw

reddit = praw.Reddit(
   client_id = "",
   client_secret = "",
   user_agent = "",
   username = "",
   password = ""
)

username = reddit.user.me()
karma = reddit.user.karma()

print("Your reddit breakdown:")
print()

print("Your reddit username is " + str(username))

for key, value in dict.items(karma):
   print("In", key, "you have", value["comment_karma"], 'Comment Karma', "and", value["link_karma"], "Link Karma")