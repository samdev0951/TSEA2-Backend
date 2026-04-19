from typing import Dict, Any, List
from pathlib import Path
import json
import os

class CourseStore:
    courses_root_path: str = "static/courses"
    content_root_title: str = "content"
    content_file_title: str = "content.json"
    lesson_file_title: str = "lesson.md"
    valid_content_types: List[str] = ["lesson", "quiz", "retrieval"]

    _courses: Dict[str, Any] = {}
    _course_contents: Dict[str, List[Any]] = {}
    _content_contents: Dict[str, Any] = {}

    @classmethod
    def load(cls):
        courses_root = Path(cls.courses_root_path)

        for course_dir in courses_root.iterdir():
            if not course_dir.is_dir():
                continue

            course_slug = course_dir.name
            course = cls._load_json(course_dir / "course.json")

            content_root = course_dir / cls.content_root_title
            if not content_root.exists():
                continue

            course_contents = []

            content_files = list(content_root.iterdir())
            course["contentLength"] = len(content_files)

            for i, content_file in enumerate(content_files):
                content_type, content_slug = content_file.name.split("__")
                content_slug = os.path.splitext(content_slug)[0]

                if content_type not in cls.valid_content_types:
                    raise ValueError(f"Content Type: '{content_type}' is not a valid course content type.")

                if content_type == "lesson" and not content_file.is_dir():
                    raise ValueError(f"Lesson '{content_slug}' must be in a directory format.")

                content_meta = { "type": content_type, "slug": content_slug, "position": i + 1, "previousSlug": None, "nextSlug": None }

                if i + 1 < len(content_files):
                    next_file = content_files[i + 1]
                    _, next_slug = next_file.name.split("__")
                    content_meta["nextSlug"] = os.path.splitext(next_slug)[0]

                if i - 1 >= 0:
                    prev_file = content_files[i - 1]
                    _, prev_slug = prev_file.name.split("__")
                    content_meta["previousSlug"] = os.path.splitext(prev_slug)[0]

                if content_file.is_dir():
                    content_meta = content_meta | cls._load_json(content_file / cls.content_file_title)
                    content_meta["content"] = cls._load_text(content_file / cls.lesson_file_title)
                else:
                    content_meta = content_meta | cls._load_json(content_file)

                stripped_content = content_meta.copy()
                stripped_content.pop("content", None)
                course_contents.append(stripped_content)

                cls._add_content_contents(course_slug, content_slug, content_meta)
                        
            cls._add_course_contents(course_slug, course_contents)
            cls._add_course(course_slug, course)

    @classmethod
    def _add_content_contents(cls, course_slug: str, content_slug: str, content: Any):
        entry_key = cls._content_contents_key(course_slug, content_slug)
        if entry_key in cls._content_contents:
            raise ValueError(f"Contents in the same course cannot have the same slug (found duplicate: '{content_slug}' in course: '{course_slug}')")

        cls._content_contents[cls._content_contents_key(course_slug, content_slug)] = content
    
    @classmethod
    def _add_course_contents(cls, course_slug: str, contents: List[Any]):
        cls._course_contents[course_slug] = contents

    @classmethod
    def _add_course(cls, slug: str, course: Dict[str, Any]):
        cls._courses[slug] = course

    @classmethod
    def _get_course_contents(cls, course_slug: str) -> List[Any]:
        course_contents = cls._course_contents.get(course_slug)
        if course_contents == None:
            return None
        
        return course_contents

    @classmethod
    def _get_content_contents(cls, course_slug: str, content_slug: str) -> Any:
        content_contents_key = cls._content_contents_key(course_slug, content_slug)
        if content_contents_key == None:
            return None

        content_contents = cls._content_contents.get(content_contents_key)
        if content_contents == None:
            return None
        
        return content_contents.copy()

    @classmethod
    def get_course(cls, slug: str) -> Dict[str, Any] | None:
        course = cls._courses.get(slug)
        if course == None:
            return None
        
        return course.copy()
    
    @classmethod
    def get_courses(cls) -> List[Dict[str, Any]]:
        return list(cls._courses.values())

    @classmethod
    def get_course_with_contents_meta(cls, slug: str) -> Dict[str, Any] | None:
        course = cls.get_course(slug)
        if course == None:
            return None

        course["contents"] = cls._get_course_contents(slug)
        return course
    
    @classmethod
    def get_course_content(cls, course_slug: str, content_slug: str) -> Dict[str, Any]:
        return cls._get_content_contents(course_slug, content_slug)

    @staticmethod
    def _content_contents_key(course_slug: str, content_slug: str) -> str:
        return f"{course_slug}:{content_slug}"

    @staticmethod
    def _load_json(path: Path) -> Dict[str, Any]:
        if not path.exists():
            return {}

        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON at {path}: {e}")
            return {}
    
    @staticmethod
    def _load_text(path: Path) -> str:
        if not path.exists():
            return ""
        with open(path, "r", encoding="utf-8") as f:
            return f.read()