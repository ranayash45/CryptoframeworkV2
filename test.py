from kivy.app import App
from kivy.lang import Builder

kv = """
<Test@AnchorLayout>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    AsyncImage:
        source: 'https://cloud.githubusercontent.com/assets/5558694/3453129/c8e626a6-01bf-11e4-9ce5-c2dfeaec36ce.gif'
        anim_delay: 0.05
Test:
"""


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    TestApp().run()