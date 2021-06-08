import random
import webbrowser

playlists = [
  "https://www.youtube.com/watch?v=cjkFG6bHGNc&feature=youtu.be",
  "https://www.youtube.com/watch?v=UJqzs7-0RXA&feature=youtu.be",
  "https://www.youtube.com/watch?v=CHFif_y2TyM&pbjreload=101",
  "https://www.youtube.com/watch?v=mkgylOJSdhE",
  "https://www.youtube.com/watch?v=mPZkdNFkNps",
  "https://www.youtube.com/watch?v=vLEek3I3wac&feature=youtu.be",
  "https://www.youtube.com/watch?v=mg7netw1JuM&feature=youtu.be",
  "https://www.youtube.com/watch?v=kXUnJ61KxRE",
  "https://www.youtube.com/watch?v=nMfPqeZjc2c",
  "https://www.youtube.com/watch?v=IQui6LE6dCU",
  "https://www.youtube.com/watch?v=wzjWIxXBs_s",
  "https://www.youtube.com/watch?v=C5Gm8UvxKlU",
  "https://www.youtube.com/watch?v=WbEGmghn_jo",
  "https://www.youtube.com/watch?v=gpvznAiKblU",
  "https://www.youtube.com/watch?v=XEBl9ZQXloE",
  "https://www.youtube.com/watch?v=rLdpprJ3jeE",
  "https://www.youtube.com/watch?v=Dz7DSgcZ5Ys",
  "https://www.youtube.com/watch?v=AsD5u6k6dKI",
  "https://www.youtube.com/watch?v=WHPEKLQID4U",
  "https://www.youtube.com/watch?v=PoAeFpUB1hA",
  "https://www.youtube.com/watch?v=btmjDyff6E8",
  "https://www.youtube.com/watch?v=TlgLbFhiBQs",
  "https://www.youtube.com/watch?v=aJaZc4E8Y4U",
  "https://www.youtube.com/watch?v=V1RPi2MYptM",
  "https://www.youtube.com/watch?v=7h0v508F9YA",
  "https://www.youtube.com/watch?v=jfBf-ksVwPQ",
  "https://www.youtube.com/watch?v=-eRebepbGks",
  "https://www.youtube.com/watch?v=HchoJcYNYlU",
  "https://www.youtube.com/watch?v=tnV3TS55TpE",
  "https://www.youtube.com/watch?v=3TNK916Pjto",
  "https://www.youtube.com/watch?v=PVV4-2G0t3k",
  "https://www.youtube.com/watch?v=_FJIH0Yi2Mk",
  "https://www.youtube.com/watch?v=ih4_1FyVjaY",
  "https://www.youtube.com/watch?v=ROPv_2aICHI",
  "https://www.youtube.com/watch?v=4KzFe50RQkQ",
  "https://www.youtube.com/watch?v=X7t--zPZdic",
  "https://www.youtube.com/watch?v=yEn8_X7Ei3A",
  "https://www.youtube.com/watch?v=aT66uumZ0Zo",
  "https://www.youtube.com/watch?v=UgHKb_7884o",
  "https://www.youtube.com/watch?v=5RbrXH6E4OY",
  "https://www.youtube.com/watch?v=zDk8pVOtiVY",
  "https://www.youtube.com/watch?v=RqzGzwTY-6w"
]

if __name__ == "__main__":
  rindex = random.randint(0, len(playlists)-1)
  webbrowser.open((playlists[rindex]), new=1, autoraise=False)