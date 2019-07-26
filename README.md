# Python Week Of Code, Namibia 2019

[blog/models.py](blog/models.py) has the source code of the database model.

## Task for Instructor

1. Run

   ```
   python manage.py makemigrations
   ```
2. Run

   ```
   python manage.py migrate
   ```
3. Launch the Python shell with

   ```
   python manage.py shell
   ```
4. Create a blog post

   ```
   from blog.models import Post
   post = Post(title="Welcome", text="This is our first blog post.")
   post.save()
   ```
5. Add

   ```
   def __str__(self):
       return self.title
   ```

   to the class `Post`.
6. Create another blog post.

   ```
   from blog.models import Post
   post = Post(title="Models", text="Django uses an abstraction layer for the database")
   post.save()
   ```

## Tasks for Learners

1. Change the `__str__()` function to return a titlecased version of the title.
2. Write one function called `html()` that return the HTML code to be used in the blog.