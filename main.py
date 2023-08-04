from markupsafe import Markup

value = Markup('bobby, <b>hadz</b>!')
print(value)  # 👉️ bobby, <b>hadz</b>!

print(Markup(123))  # 👉️ 123

# 👇️ bobby, &lt;b&gt;hadz&lt;/b&gt;!
print(Markup.escape('bobby, <b>hadz</b>!'))
