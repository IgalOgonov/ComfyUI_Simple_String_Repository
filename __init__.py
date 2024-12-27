from .py.simple_string_repository import SimpleStringRepositorySmall,SimpleStringRepositorySmallCompact, SimpleStringRepository, SimpleStringRepositoryCompact, SimpleStringRepositoryLarge, SimpleStringRepositoryLargeCompact


NODE_CLASS_MAPPINGS = {
    "SimpleStringRepositorySmall": SimpleStringRepositorySmall,
    "SimpleStringRepositorySmallCompact": SimpleStringRepositorySmallCompact,
    "SimpleStringRepository": SimpleStringRepository,
    "SimpleStringRepositoryCompact": SimpleStringRepositoryCompact,
    "SimpleStringRepositoryLarge": SimpleStringRepositoryLarge,
    "SimpleStringRepositoryLargeCompact": SimpleStringRepositoryLargeCompact,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleStringRepositorySmall": "Simple String Repository Small (IO)",
    "SimpleStringRepositorySmallCompact": "Simple String Repository Small Compact (IO)",
    "SimpleStringRepository": "Simple String Repository (IO)",
    "SimpleStringRepositoryCompact": "Simple String Repository Compact (IO)",
    "SimpleStringRepositoryLarge": "Simple String Repository Large (IO)",
    "SimpleStringRepositoryLargeCompact": "Simple String Repository Large Compact (IO)",
}


WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
