from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from forex_python.converter import CurrencyRates

class CurrencyApp(App):
    def build(self):
        # إعداد واجهة المستخدم
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Fetching data...", font_size='40sp')
        self.layout.add_widget(self.label)

        # استدعاء التحديث الأول
        self.update_currency(None)

        # إعداد مؤقت لتحديث السعر كل 5 دقائق (300 ثانية)
        Clock.schedule_interval(self.update_currency, 300)

        return self.layout

    def update_currency(self, dt):
        try:
            c = CurrencyRates()
            # جلب سعر الدولار مقابل اليورو
            rate = c.get_rate('USD', 'EUR')
            self.label.text = f"USD to EUR: {rate:.4f}"
        except Exception as e:
            self.label.text = "Error fetching data"

if __name__ == '__main__':
    CurrencyApp().run()
