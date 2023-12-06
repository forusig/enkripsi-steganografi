from stegano import lsb

# Hide message in image
secret = lsb.hide("./wonu.png", "Hello Wonwoo")
secret.save("./new_wonu.png")

# Reveal message from image
clear_message = lsb.reveal("./new_wonu.png")
print(clear_message)
