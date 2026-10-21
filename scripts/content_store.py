"""Store reviewed introductions by publication year/month and immutable Naver ID."""
import json
import re
from datetime import datetime
from pathlib import Path


def write_json(path, value):
    path = Path(path)
    text = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    if path.is_file() and path.read_text() == text:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(text)
    temporary.replace(path)


def load_posts(root):
    root = Path(root)
    paths = sorted((root / 'content/posts').rglob('*.json'))
    if paths:
        posts = [json.loads(path.read_text()) for path in paths]
    else:
        legacy = root / 'content/posts.json'
        posts = json.loads(legacy.read_text()) if legacy.is_file() else []
    ids = [p['id'] for p in posts]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate Naver post ID in content/posts')
    return sorted(posts, key=lambda p: p['publishedAt'], reverse=True)


def save_post(root, post):
    root = Path(root)
    if not re.fullmatch(r'\d+', post['id']):
        raise ValueError('Post ID must be numeric')
    stamp = datetime.fromisoformat(post['publishedAt'])
    target = root / 'content/posts' / stamp.strftime('%Y/%m') / (post['id'] + '.json')
    old_paths = list((root / 'content/posts').rglob(post['id'] + '.json'))
    write_json(target, post)
    for old in old_paths:
        if old != target:
            old.unlink()
    return target


def migrate(root):
    root = Path(root)
    legacy = root / 'content/posts.json'
    if not legacy.is_file():
        return
    original = json.loads(legacy.read_text())
    for post in original:
        save_post(root, post)
    if {p['id']: p for p in load_posts(root)} != {p['id']: p for p in original}:
        raise ValueError('Migration validation failed; original kept')
    legacy.unlink()


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    migrate(root)
    print(f'{len(load_posts(root))} introductions stored by year/month/ID.')
