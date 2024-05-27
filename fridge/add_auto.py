import os
import django

# Djangoの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fridge.settings')
django.setup()

from food.models import Post

# データを追加する
articles_data = [
    {"name": "sample1", "num": "1", "date": "2024年05月26日"},
    {"name": "sample2", "num": "2", "date": "2024年05月26日"},
    {"name": "sample3", "num": "3", "date": "2024年05月26日"},
]

for article_data in articles_data:
    article, created = Post.objects.get_or_create(**article_data)
    if created:
        print(f'Added: {article.name}')
    else:
        print(f'Already exists: {article.name}')
