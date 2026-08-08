#!/usr/bin/env python3
"""Repository-bound input policy for the GigaChat advisory integration."""

from pathlib import Path

GENERATED_SUFFIX = ".gigachat-opinion.md"
MAX_INPUT_BYTES = 128 * 1024


class InputPathError(ValueError):
    """Raised when a requested lyrics path violates the repository policy."""


def repository_root() -> Path:
    """Return the repository root from this module's stable location."""

    return Path(__file__).resolve().parents[2]


def resolve_lyrics_path(
    raw_path: str, *, repo_root: Path | None = None
) -> tuple[Path, Path]:
    """Resolve a safe Markdown input and its adjacent opinion output path.

    The canonical source must be a regular Markdown file inside the repository.
    Resolving before the boundary check rejects both ``..`` traversal and
    symlink escapes. Git metadata and generated opinion reports are never valid
    inputs. A pre-existing output symlink is rejected before the caller writes.
    """

    if not raw_path:
        raise InputPathError("путь не задан")
    if any(ord(char) < 32 or ord(char) == 127 for char in raw_path):
        raise InputPathError("управляющие символы в пути запрещены")

    raw = Path(raw_path)
    if raw.is_absolute():
        raise InputPathError("нужен относительный путь внутри репозитория")
    if any(part.lower() == ".git" for part in raw.parts):
        raise InputPathError("git metadata нельзя отправлять во внешний API")

    root = (repo_root or repository_root()).resolve(strict=True)
    try:
        source = (root / raw).resolve(strict=True)
    except (FileNotFoundError, OSError, RuntimeError) as exc:
        raise InputPathError("файл не существует или путь недоступен") from exc

    try:
        relative = source.relative_to(root)
    except ValueError as exc:
        raise InputPathError("путь выходит за пределы репозитория") from exc

    if any(part.lower() == ".git" for part in relative.parts):
        raise InputPathError("git metadata нельзя отправлять во внешний API")
    if not source.is_file():
        raise InputPathError("путь должен указывать на обычный файл")
    if source.suffix.lower() != ".md":
        raise InputPathError("поддерживаются только Markdown-файлы (.md)")
    if source.name.lower().endswith(GENERATED_SUFFIX):
        raise InputPathError("сгенерированный GigaChat-отчёт нельзя подать на вход")
    if source.stat().st_size > MAX_INPUT_BYTES:
        raise InputPathError(f"файл превышает лимит {MAX_INPUT_BYTES} байт")

    output = source.with_name(f"{source.stem}{GENERATED_SUFFIX}")
    if output.is_symlink():
        raise InputPathError("выходной путь не может быть символической ссылкой")
    if output.exists() and not output.is_file():
        raise InputPathError("выходной путь занят не-файлом")

    return source, output
