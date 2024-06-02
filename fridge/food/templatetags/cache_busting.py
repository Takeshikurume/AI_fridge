from pathlib import Path

from django import template
from django.conf import settings
from django.templatetags.static import static


register = template.Library()


@register.simple_tag
def static_cache(filepath) -> str:
    """静的ファイルのURLにファイルの更新日時クエリを付加する

    """
    # Django標準機能を使ってhtml埋め込み用のパスを取得
    res_path = static(filepath)
    # mtimeを取得する
    full_filepath = Path(getattr(settings, 'STATIC_ROOT', '')).joinpath(filepath)
    file_mtime = str(int(full_filepath.stat().st_mtime))
    # パスに結合
    res_path += '?v=' + file_mtime
    return res_path
