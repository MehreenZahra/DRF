from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


# Create your tests here.
class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(username='test_user1', password='pass')
        test_post = Post.objects.create(
            category_id = 1,
            title='Post Title',
            excerpt='This is a test post excerpt.',
            content='This is a test post content.',
            slug = 'post-title',
            author_id= 1,
            status= 'published'
        )
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'  
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        title = f'{post.title}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'This is a test post content.')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Post Title')
        self.assertEqual(str(cat), 'django')