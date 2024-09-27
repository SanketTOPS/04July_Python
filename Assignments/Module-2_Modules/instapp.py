import instaloader

instaID=input("Enter your instagram ID:")

insta=instaloader.Instaloader()

insta.download_profile(profile_name=instaID)

print("Profile downloaded successfully!")


