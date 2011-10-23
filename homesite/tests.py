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
                                                cv=""
        )

        #self.service = Services.objects.create(title="test", description="test").save_base(force_insert=False)
        #self.portfolio = Portfolio.objects.create(title="test", description="desc", type=self.service.id, link="http://fsdf", image="").save()

    def testHome(self):
        request = self.client.get("/")
        self.assertContains(request, text="portfolio")

    def testAbout(self):
        self.assertEqual(self.about.description, "test")

        request = self.client.get("/about/")
        self.assertContains(request, text="about")
        self.assertDictEqual(
            request.context["latest_posts"].values()[0],
                {"text": u"test", "id": 1, "title": u"test"},
        )
        self.assertEqual(request.context["about"].description, "test")

    def testBlog(self):
        self.assertEqual(self.post.title, "test")
        self.assertEqual(self.post.text, "test")

        request = self.client.get("/blog/")
        self.assertEqual(request.context["page"], "blog")
        self.assertDictEqual(
            request.context["posts"].object_list.values()[0],
                {"text": u"test", "id": 1, "title": u"test"}
        )
        
    def testPortfolio(self):
        request = self.client.get("/portfolio/")
        self.assertContains(request, text="portfolio")

    def testSkills(self):
        request = self.client.get("/skills/")
        self.assertContains(request, text="skills")

    def testMessages(self):
        self.assertEqual(self.message.name, "test_name")
        self.assertEqual(self.message.email, "email")
        self.assertEqual(self.message.message, "test_message")

    def testSendMessages(self):
        request = self.client.post(
            "/ajax/quick-form",
            {"name":"test","email":"d1ffuz0r@mail.ru","message":"msg"},
            **{"HTTP_X_REQUESTED_WITH":"XMLHttpRequest"}
        )
        self.assertEqual(QuickMessages.objects.filter(message="msg").get().email, "d1ffuz0r@mail.ru")
        self.assertEqual(request.content,"Success. your message sended")