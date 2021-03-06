from django.test import TestCase
from django.test.client import Client
from homesite.models import Blog, QuickMessages, About, Settings


class HomesiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.post = Blog.objects.create(title="test",
                                        text="test"
        )
        self.message = QuickMessages.objects.create(name="test_name",
                                                    email="email",
                                                    message="test_message"
        )
        self.about = About.objects.create(description="test")
        self.settings = Settings.objects.create(facebook="http://test.com",
                                                twitter="http://test.com",
                                                github="http://test.com",
                                                jabber="test@dsfdsf.com",
                                                icq="12123",
                                                email="test@dsfdsf.com",
                                                skype="sfsdf",
                                                cv="",
                                                linkedin="linked.in"
        )

    def test_linkedin(self):
        self.assertEqual(self.settings.linkedin, "linked.in")

    def test_home(self):
        request = self.client.get("/")
        self.assertContains(request, text="portfolio")

    def test_about(self):
        self.assertEqual(self.about.description, "test")

        request = self.client.get("/about/")
        self.assertContains(request, text="about")
        self.assertDictEqual(
            request.context["latest_posts"].values()[0],
                {"text": u"test", "id": 1, "title": u"test"},
        )

    def test_blog(self):
        self.assertEqual(self.post.title, "test")
        self.assertEqual(self.post.text, "test")

        request = self.client.get("/blog/")
        self.assertEqual(request.context["page"], "blog")
        self.assertDictEqual(
            request.context["posts"].object_list.values()[0],
                {"text": u"test", "id": 1, "title": u"test"}
        )

    def test_skills(self):
        request = self.client.get("/skills/")
        self.assertContains(request, text="skills")

    def test_messages(self):
        self.assertEqual(self.message.name, "test_name")
        self.assertEqual(self.message.email, "email")
        self.assertEqual(self.message.message, "test_message")

    def test_send_message_true(self):
        request = self.client.post(
            "/ajax/quick-form",
            {"name": "test", "email": "d1ffuz0r@mail.ru", "message": "msg"},
            **{"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"}
        )
        message = QuickMessages.objects.filter(message="msg").get()
        self.assertEqual(message.email, "d1ffuz0r@mail.ru")
        self.assertEqual(request.content, "Success. your message sended")
