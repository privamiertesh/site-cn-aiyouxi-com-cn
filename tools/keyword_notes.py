from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    note: str
    url: str = ""
    tags: Optional[List[str]] = None
    created_at: str = ""
    
    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.tags is None:
            self.tags = []
    
    def display(self) -> str:
        parts = [
            f"关键词: {self.keyword}",
            f"笔记: {self.note}",
            f"URL: {self.url}",
            f"标签: {', '.join(self.tags) if self.tags else '无'}",
            f"创建时间: {self.created_at}"
        ]
        return " | ".join(parts)


@dataclass
class NoteCollection:
    notes: List[KeywordNote]
    
    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)
    
    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if keyword in n.keyword]
    
    def filter_by_tag(self, tag: str) -> List[KeywordNote]:
        result = []
        for note in self.notes:
            if note.tags and tag in note.tags:
                result.append(note)
        return result
    
    def format_summary(self) -> str:
        lines = [f"共 {len(self.notes)} 条笔记"]
        for i, note in enumerate(self.notes, 1):
            lines.append(f"{i}. {note.keyword}: {note.note}")
        return "\n".join(lines)
    
    def display_all(self) -> str:
        return "\n".join(note.display() for note in self.notes)


def create_default_collection() -> NoteCollection:
    notes = [
        KeywordNote(
            keyword="爱游戏",
            note="爱游戏是一个面向游戏爱好者的综合平台，提供资讯、攻略和社区服务。",
            url="https://site-cn-aiyouxi.com.cn",
            tags=["游戏", "社区", "资讯"]
        ),
        KeywordNote(
            keyword="游戏攻略",
            note="爱游戏平台收录了大量热门游戏的详细攻略，帮助玩家快速上手。",
            url="https://site-cn-aiyouxi.com.cn",
            tags=["攻略", "游戏"]
        ),
        KeywordNote(
            keyword="玩家社区",
            note="爱游戏的社区模块允许玩家发布帖子、交流心得。",
            url="https://site-cn-aiyouxi.com.cn",
            tags=["社区", "交流"]
        ),
        KeywordNote(
            keyword="最新资讯",
            note="每日更新游戏行业动态和新游发布消息。",
            url="https://site-cn-aiyouxi.com.cn",
            tags=["资讯", "动态"]
        ),
        KeywordNote(
            keyword="电竞赛事",
            note="爱游戏提供电竞赛事直播和赛事回顾。",
            url="https://site-cn-aiyouxi.com.cn",
            tags=["电竞", "直播"]
        ),
        KeywordNote(
            keyword="游戏评测",
            note="专业评测团队对新游戏进行多维度评价。",
            url="https://site-cn-aiyouxi.com.cn",
            tags=["评测", "新游"]
        ),
    ]
    return NoteCollection(notes)


def format_output(collection: NoteCollection, style: str = "detailed") -> str:
    if style == "summary":
        return collection.format_summary()
    elif style == "detailed":
        return collection.display_all()
    elif style == "keyword_list":
        keywords = [note.keyword for note in collection.notes]
        return "关键词列表: " + ", ".join(keywords)
    else:
        return "未知的输出样式"


if __name__ == "__main__":
    collection = create_default_collection()
    print("=== 详细输出 ===")
    print(format_output(collection, "detailed"))
    print()
    print("=== 摘要输出 ===")
    print(format_output(collection, "summary"))
    print()
    print("=== 关键词列表输出 ===")
    print(format_output(collection, "keyword_list"))
    print()
    print("=== 筛选测试 ===")
    filtered = collection.filter_by_tag("攻略")
    print("筛选标签为'攻略'的笔记:")
    for note in filtered:
        print(note.display())