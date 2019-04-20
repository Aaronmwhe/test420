# coding:utf-8
import requests
s =requests.session()

url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
print (s.cookies)
# cook ={
# ".CNBlogsCookie":"D018E49BE4C012B4CFCB8A07171320A394288C04568CB6829D40D92E828CBE6772C86B1CB00D7E3C7D9A57D1F983D3094D30FE32840540EE9F7245F03B600A36BB3FDCCE6B788DCCAA8FA45CFD1F7B14E36A2B05",
# ".Cnblogs.AspNetCore.Cookies":"CfDJ8KlpyPucjmhMuZTmH8oiYTMzhqNXRhLo83foeEM0L4sS6YQBW8i0U8fKNvXBSoo4tJfVe-qDYePt2XMGFr_4tTq5RvD7-nQkRfkFpfvDrpuwsSzE_rPzopLaW21nGCYxlmEaH_Npvg0NDZkVccvCGF9Wgka4i3XNwJJDjH9DpBmyTTfq7RpkD-DnfxVvQZse6b6tP08ZIunxrtFC3tTJ-zffGV2OU-SGgixsAahRu8v0pPttcbMpVdHOtWP3lP2iBUyhuWpUo8MrT___-qFVKnX5BR3RAb2TqGPEUJs6nT5g"
#
#       }
h={
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
}
c =requests.cookies.RequestsCookieJar()
c.set(".CNBlogsCookie","D018E49BE4C012B4CFCB8A07171320A394288C04568CB6829D40D92E828CBE6772C86B1CB00D7E3C7D9A57D1F983D3094D30FE32840540EE9F7245F03B600A36BB3FDCCE6B788DCCAA8FA45CFD1F7B14E36A2B05")
c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8KlpyPucjmhMuZTmH8oiYTMzhqNXRhLo83foeEM0L4sS6YQBW8i0U8fKNvXBSoo4tJfVe-qDYePt2XMGFr_4tTq5RvD7-nQkRfkFpfvDrpuwsSzE_rPzopLaW21nGCYxlmEaH_Npvg0NDZkVccvCGF9Wgka4i3XNwJJDjH9DpBmyTTfq7RpkD-DnfxVvQZse6b6tP08ZIunxrtFC3tTJ-zffGV2OU-SGgixsAahRu8v0pPttcbMpVdHOtWP3lP2iBUyhuWpUo8MrT___-qFVKnX5BR3RAb2TqGPEUJs6nT5g")
# c.set("")
s.cookies.update(c)
print (s.cookies)

r1 = s.get(url,headers=h,verify=False)
print (r1.text)